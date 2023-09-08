# Cleaner Guide

## How it Works:
- Configure Logging: Logs all scanning activity and saves it in the home directory.
- Patterns: The patterns are regular expressions that the script will look for. Add more patterns as needed.
- Scan File: This function reads each file and scans for the patterns. If a pattern is found, it logs a warning.
- Scan URL: This function fetches the content of a URL and scans it for the patterns. If a pattern is found, it logs a warning.
- Scanning: It starts scanning both the files in the WordPress installation directory and URLs specified.
- Quarantine Feature: Added a quarantine_file function to move suspicious files into a "QuarantineFiles" folder in the home directory.
- PDF Report: Used the reportlab library to generate a PDF report. The report will be saved as Quarantine_Report.pdf in the home directory and will include the name of the file, location, the symptom that triggered the quarantine, and the timestamp.
- In-Depth File Scan: Scanning more file types now ('.php', '.js', '.html', '.htaccess').
- Deeper URL Scan: Included URLs that point to files in the wp-content/uploads directory for deeper scanning.
- Logging: Enhanced logging to record found patterns, errors, and the scan's completion status.

## Prerequisite

```
pip install reportlab
pip install requests

```

## Notes
1. Remember, this is a rudimentary script that performs basic scans and may generate false positives or miss actual malware. 
2. For robust security, consider using specialized tools and services. As this scripts is only 1/5 of actual. If you want a full solution, please purchase and support the author.
3. Run with caution, make sure to test throughly before do it in production, add more regular expression to catch variety of potential malware pattern, including shell commands and suspicious comments. 
4. Make sure to have proper authorization before scanning any WordPress site.


