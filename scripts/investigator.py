from burp import IBurpExtender
from burp import IScannerCheck
from burp import IScanIssue

class BurpExtender(IBurpExtender, IScannerCheck):

    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.registerScannerCheck(self)
        
    def doPassiveScan(self, baseRequestResponse):
        issues = []

        # Get Request and Response Information
        requestInfo = self._helpers.analyzeRequest(baseRequestResponse)
        responseInfo = self._helpers.analyzeResponse(baseRequestResponse.getResponse())

        # Headers
        response_headers = responseInfo.getHeaders()
        header_names = [header.split(":")[0] for header in response_headers]
        
        # Missing Security Headers
        important_headers = ["Strict-Transport-Security", "Content-Security-Policy", "X-Content-Type-Options"]
        for ih in important_headers:
            if ih not in header_names:
                issues.append(self.generateIssue(baseRequestResponse, f"Missing {ih} Header", "High"))

        # Clickjacking: Missing X-Frame-Options header
        if "X-Frame-Options" not in header_names:
            issues.append(self.generateIssue(baseRequestResponse, "Missing X-Frame-Options Header", "Medium"))

        # Rate Limiting: Checking for the absence of 'Retry-After' header
        if responseInfo.getStatusCode() == 429 and "Retry-After" not in header_names:
            issues.append(self.generateIssue(baseRequestResponse, "Missing Retry-After Header for Rate Limiting", "Medium"))

        # Cookies
        for header in response_headers:
            if header.startswith("Set-Cookie"):
                # Cookie Poisoning: Check if Secure and HttpOnly flags are set
                if "Secure" not in header or "HttpOnly" not in header:
                    issues.append(self.generateIssue(baseRequestResponse, "Insecure Cookie Settings", "High"))

        # TODO: Add checks for .htaccess, hotlinking, etc.
        # These would likely require more active scanning techniques or specialized payloads.

        return issues if len(issues) > 0 else None

    def generateIssue(self, baseRequestResponse, issue_name, severity):
        return CustomScanIssue(
            baseRequestResponse.getHttpService(),
            self._helpers.analyzeRequest(baseRequestResponse).getUrl(),
            [self._callbacks.applyMarkers(baseRequestResponse, None, None)],
            issue_name,
            "The application's HTTP response did not include important security measures.",
            severity
        )

class CustomScanIssue(IScanIssue):
    def __init__(self, http_service, url, http_messages, name, detail, severity):
        self._http_service = http_service
        self._url = url
        self._http_messages = http_messages
        self._name = name
        self._detail = detail
        self._severity = severity

    # Implement IScanIssue methods (getHttpMessages, getUrl, etc.)