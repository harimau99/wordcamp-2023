# Comprehensive Tweak Set #2 - .htacces

### **Set a Content Security Policy**

This is an enhancement to the previously mentioned **`Content-Security-Policy`** header. This one is a bit more defined.

```
Header set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; img-src 'self' data:; style-src 'self' 'unsafe-inline';"

```

### **Protect Against Clickjacking with ALLOW-FROM**

You can specify which domains are allowed to embed your site.

```
Header set X-Frame-Options "ALLOW-FROM https://example.com/"

```

Replace **`https://example.com/`** with your domain.

### **Set Referrer-Policy**

This header controls how much referrer information should be included with requests.

```
Header set Referrer-Policy "no-referrer-when-downgrade"

```

### **HTTP Strict Transport Security (HSTS)**

This tells the browser to request your site using HTTPS even if the protocol isn't specified.

```
Header set Strict-Transport-Security "max-age=31536000" env=HTTPS

```

### **Secure Cookies**

Make sure that WordPress sets cookies securely.

```
Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure;SameSite=Strict

```

### **6. Limit Request Methods**

Allow only necessary HTTP methods like GET and POST to be used on your site.

```
<LimitExcept GET POST>
  Deny from all
</LimitExcept>

```

### **7. Preventing Image Hotlinking**

This saves bandwidth and prevents other websites from displaying your images.

```
RewriteEngine on
RewriteCond %{HTTP_REFERER} !^$
RewriteCond %{HTTP_REFERER} !^http(s)?://(www\.)?yourwebsite.com [NC]
RewriteRule \.(jpg|jpeg|png|gif)$ - [NC,F,L]

```

Replace **`yourwebsite.com`** with your domain.

### **8. GeoIP Blocking**

If you have the GeoIP module enabled, you can block or allow access based on geographic location.

```
SetEnvIf GEOIP_COUNTRY_CODE CN BlockCountry
Deny from env=BlockCountry

```

In this example, all IPs from China (CN) would be blocked.

### **9. Rate Limiting**

You can rate-limit the access to your site to prevent abuse.

```
IfModule mod_evasive24.c>
  DOSHashTableSize 2048
  DOSPageCount 10
  DOSSiteCount 100
  DOSPageInterval 2
  DOSSiteInterval 2
  DOSBlockingPeriod 10
</IfModule>

```

### **10. Require Strong SSL Ciphers**

```
SSLProtocol ALL -SSLv3 -TLSv1 -TLSv1.1
SSLCipherSuite EECDH+AESGCM:EDH+AESGCM

```

Once you've added these configurations to your **`.htaccess`** file, don't forget to **restart your Apache server** and test all features of your website to ensure they are working correctly. Always keep a backup before making changes to your **`.htaccess`** file, as misconfigurations can break your website or make it unavailable.