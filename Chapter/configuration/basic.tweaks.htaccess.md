# Basic Tweak Set #1 - .htaccess

### **Prohibit Directory Browsing**

Preventing users from being able to see the files in your directories.

```
Options -Indexes
```

### **Block Access to wp-config.php**

This file contains sensitive information like database credentials.

```
<Files wp-config.php>
  order allow,deny
  deny from all
</Files>
```

### **Block Access to .htaccess Itself**

Ensure that no one can read or write to your **`.htaccess`** file.

```
<Files .htaccess>
  order allow,deny
  deny from all
</Files>
```

### **Secure Directories by Disabling Script Execution**

In directories where there shouldn't be any script execution, you can add this:

```
Options -ExecCGI
AddHandler cgi-script .php .pl .py .jsp .asp .htm .shtml .sh .cgi

```

### **Limit File Uploads**

If you have a directory for uploads (usually **`/wp-content/uploads`**), you can limit the types of files that can be uploaded for added security.

```
<FilesMatch "\.(php|php\.)$">
  Order Allow,Deny
  Deny from All
</FilesMatch>

```

### **Block Access by IP**

If you know the specific IPs that should have admin access, you can limit access to specific directories like **`/wp-admin/`**.

```
<Directory "/wp-admin">
  Order Deny,Allow
  Deny from all
  Allow from xxx.xxx.xxx.xxx
</Directory>

```

Replace **`xxx.xxx.xxx.xxx`** with your IP address.

### **HTTP Security Headers**

Security headers help protect against cross-site scripting (XSS), clickjacking, and other code injection attacks.

```
Header set Content-Security-Policy "default-src 'self';"
Header set X-Content-Type-Options "nosniff"
Header set X-Frame-Options "SAMEORIGIN"
Header set X-XSS-Protection "1; mode=block"

```

### **Disable Server Signature**

Disabling server signature prevents attackers from identifying what Apache modules you are running.

```
ServerSignature Off

```

### **Force HTTPS**

Always use HTTPS instead of HTTP.

```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]

```

After making these changes, **restart your Apache server** for the new **`.htaccess`** rules to take effect. Always test thoroughly to make sure your site functions as expected. A poorly configured **`.htaccess`** file can result in downtime or unintended behaviors.

Remember, **`.htaccess`** is a powerful tool but it's part of a layered security approach. It should be used in conjunction with other security measures for maximum effectiveness.