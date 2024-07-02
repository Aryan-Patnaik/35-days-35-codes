import re
from urllib.parse import urlparse

# List of suspicious words commonly found in phishing URLs
suspicious_words = [
    'login', 'verify', 'update', 'account', 'secure', 'webscr', 'banking', 'signin', 'confirm'
]

# Function to check if URL contains an IP address
def has_ip_address(url):
    ip_pattern = re.compile(
        r'http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}.*'  # Regular expression pattern to match IP address in URL
    )
    return bool(ip_pattern.match(url))

# Function to check if URL's domain contains suspicious words
def has_suspicious_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    for word in suspicious_words:
        if word in domain:
            return True
    return False

# Function to check if URL contains excessive special characters
def has_excessive_special_chars(url):
    special_char_count = sum(1 for char in url if not char.isalnum() and char not in ('.', ':', '/', '-', '_'))
    return special_char_count > 5

# Function to check if URL's length is unusually long
def has_unusual_length(url):
    return len(url) > 75

# Function to determine if a URL is suspicious based on various criteria
def is_suspicious(url):
    if has_ip_address(url):
        print(f"Suspicious: URL contains an IP address: {url}")
        return True
    if has_suspicious_domain(url):
        print(f"Suspicious: URL contains suspicious domain words: {url}")
        return True
    if has_excessive_special_chars(url):
        print(f"Suspicious: URL contains excessive special characters: {url}")
        return True
    if has_unusual_length(url):
        print(f"Suspicious: URL length is unusual: {url}")
        return True
    return False

# Function to analyze a list of URLs and print whether each one is safe or suspicious
def analyze_urls(urls):
    for url in urls:
        if is_suspicious(url):
            print(f"Potential phishing URL detected: {url}")
        else:
            print(f"URL appears to be safe: {url}")

# Main function to test the analysis with a set of example URLs
if __name__ == "__main__":
    test_urls = [
        "http://192.168.1.1/login",
        "http://secure-bank.com/verify",
        "http://example.com/update_account_information",
        "http://normal-website.com/home",
        "http://phishing-site.com?sessionid=1234567890&user=login"
    ]
    
    analyze_urls(test_urls)
