import os  # Import the os module for interacting with the operating system

# Define the directory paths for ModSecurity configuration and rules
modsec_conf_dir = "/etc/modsecurity"
modsec_rules_dir = "/etc/modsecurity/rules"

# Define the file paths for the main ModSecurity configuration and custom rules
modsec_main_conf = os.path.join(modsec_conf_dir, "modsecurity.conf")
custom_rules_file = os.path.join(modsec_rules_dir, "custom_rules.conf")

# Create the directories for ModSecurity configuration and rules if they don't exist
os.makedirs(modsec_conf_dir, exist_ok=True)
os.makedirs(modsec_rules_dir, exist_ok=True)

# Define the content for the main ModSecurity configuration file
modsec_conf_content = """
# Load basic rules and enable ModSecurity
Include /usr/local/modsecurity/etc/modsecurity.d/modsecurity.conf
Include /usr/local/modsecurity/etc/modsecurity.d/owasp-modsecurity-crs/crs-setup.conf
Include /usr/local/modsecurity/etc/modsecurity.d/owasp-modsecurity-crs/rules/*.conf

# Load custom rules
Include /etc/modsecurity/rules/custom_rules.conf
"""

# Write the main ModSecurity configuration content to the file
with open(modsec_main_conf, "w") as f:
    f.write(modsec_conf_content)

# Define the content for the custom rules file
custom_rules_content = """
# Enable ModSecurity
SecRuleEngine On

# Basic SQL Injection protection
SecRule ARGS "\\b(select|union|insert|update|delete|drop|alter)\\b" \
    "id:1001,phase:2,deny,log,status:403,msg:'SQL Injection Attempt'"

# Basic XSS protection
SecRule ARGS "<(script|img|svg|iframe|body|link|style|div|object|embed|applet|meta)\\b" \
    "id:1002,phase:2,deny,log,status:403,msg:'XSS Attempt'"

# Basic CSRF protection
SecRule REQUEST_HEADERS:Referer "!@contains /yourdomain.com/" \
    "id:1003,phase:2,deny,log,status:403,msg:'Possible CSRF Attack'"

# Block access to sensitive files
SecRule REQUEST_FILENAME "\\.(htaccess|htpasswd|ini|phps|fla|psd|log|sh)$" \
    "id:1004,phase:2,deny,log,status:403,msg:'Access to sensitive file blocked'"

# Block common file upload vulnerabilities
SecRule FILES_NAMES "(htaccess|htpasswd|ini|php|phps|fla|psd|log|sh)$" \
    "id:1005,phase:2,deny,log,status:403,msg:'Illegal file upload attempt'"
"""

# Write the custom rules content to the custom rules file
with open(custom_rules_file, "w") as f:
    f.write(custom_rules_content)

# Print a success message indicating the configuration is complete
print("ModSecurity WAF configuration completed successfully.")
