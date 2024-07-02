import socket
import requests
from urllib.parse import urlparse

# List of common ports to check for openness
COMMON_PORTS = [80, 443, 21, 22, 23, 25, 110, 143, 3306, 3389]

# List of common misconfiguration files to check for accessibility
COMMON_FILES = [
    'robots.txt',
    'wp-admin/install.php',
    'phpinfo.php',
    '.git/config'
]

# Dictionary of outdated software indicators based on headers
OUTDATED_SOFTWARE = {
    'Server': ['Apache/2.2', 'nginx/1.10'],
    'X-Powered-By': ['PHP/5.4', 'PHP/5.5']
}

def check_open_ports(host):
    # Check common ports to see if they are open
    open_ports = []
    for port in COMMON_PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
    return open_ports

def check_outdated_software(headers):
    # Check headers to see if they indicate outdated software
    outdated = []
    for header, versions in OUTDATED_SOFTWARE.items():
        if header in headers:
            for version in versions:
                if version in headers[header]:
                    outdated.append(f"{header}: {headers[header]}")
    return outdated

def check_misconfigurations(url):
    # Check for common misconfiguration files
    misconfigurations = []
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
    for file in COMMON_FILES:
        try:
            response = requests.get(f"{base_url}/{file}", timeout=3)
            if response.status_code == 200:
                misconfigurations.append(f"{file} is accessible")
        except requests.RequestException:
            pass
    return misconfigurations

def scan_url(url):
    # Perform the scan on the provided URL
    print(f"Scanning {url}...")

    parsed_url = urlparse(url)
    host = parsed_url.netloc

    # Check for open ports on the host
    open_ports = check_open_ports(host)
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No common open ports found.")

    try:
        # Send a request to get headers from the URL
        response = requests.get(url, timeout=5)
        headers = response.headers

        # Check headers for indicators of outdated software
        outdated_software = check_outdated_software(headers)
        if outdated_software:
            print("Outdated software detected:")
            for item in outdated_software:
                print(f"  - {item}")
        else:
            print("No outdated software detected.")

        # Check for accessible misconfiguration files
        misconfigurations = check_misconfigurations(url)
        if misconfigurations:
            print("Misconfigurations detected:")
            for item in misconfigurations:
                print(f"  - {item}")
        else:
            print("No misconfigurations detected.")

    except requests.RequestException as e:
        # Handle connection errors
        print(f"Failed to connect to {url}: {e}")

if __name__ == "__main__":
    # Ask the user to input the website URL
    url = input("Enter the website URL (http://example.com): ")

    # Validate URL format
    if urlparse(url).scheme and urlparse(url).netloc:
        scan_url(url)
    else:
        print("Invalid URL format. Please enter a valid URL.")
