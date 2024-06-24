import requests  # Import the requests library for making HTTP requests
import hashlib   # Import hashlib for hashing operations
import os        # Import os module for operating system related operations
import sys       # Import sys module for system-specific parameters and functions

# Configuration variables for the firmware update process
FIRMWARE_URL = 'https://example.com/firmware/latest.bin'  # URL to download the latest firmware binary
CHECKSUM_URL = 'https://example.com/firmware/latest_checksum.txt'  # URL to fetch the checksum of the latest firmware
FIRMWARE_PATH = '/path/to/firmware.bin'        # Local path where the downloaded firmware will be saved
BACKUP_PATH = '/path/to/backup_firmware.bin'    # Local path where the current firmware will be backed up

def download_file(url, destination):
    """Download a file from a URL to a local destination."""
    try:
        response = requests.get(url, stream=True)  # Send a GET request to the specified URL
        response.raise_for_status()                # Raise an exception for bad response status (4xx or 5xx)
        with open(destination, 'wb') as f:         # Open the destination file in binary write mode
            for chunk in response.iter_content(chunk_size=8192):  # Iterate over response content in chunks
                f.write(chunk)                     # Write each chunk to the destination file
        print(f"Downloaded {url} to {destination}")  # Print a success message
    except requests.RequestException as e:
        print(f"Failed to download {url}: {e}")    # Print an error message if download fails
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

def get_checksum(url):
    """Get the checksum from a URL."""
    try:
        response = requests.get(url)               # Send a GET request to the specified URL
        response.raise_for_status()                # Raise an exception for bad response status (4xx or 5xx)
        checksum = response.text.strip()           # Get the checksum from the response and strip any whitespace
        return checksum                            # Return the checksum
    except requests.RequestException as e:
        print(f"Failed to download checksum from {url}: {e}")  # Print an error message if checksum download fails
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

def verify_checksum(file_path, expected_checksum):
    """Verify the checksum of a file."""
    sha256 = hashlib.sha256()                     # Create a new SHA-256 hash object
    try:
        with open(file_path, 'rb') as f:           # Open the file in binary read mode
            for chunk in iter(lambda: f.read(4096), b""):  # Read the file in chunks
                sha256.update(chunk)               # Update the hash object with each chunk
        calculated_checksum = sha256.hexdigest()   # Get the hexadecimal digest of the hash
        return calculated_checksum == expected_checksum  # Compare calculated checksum with expected checksum
    except FileNotFoundError as e:
        print(f"File not found: {file_path}")      # Print an error message if file is not found
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

def backup_current_firmware(current_firmware_path, backup_path):
    """Backup the current firmware."""
    try:
        if os.path.exists(current_firmware_path):  # Check if the current firmware file exists
            os.rename(current_firmware_path, backup_path)  # Rename/move the current firmware file to backup path
            print(f"Backed up current firmware to {backup_path}")  # Print a success message
    except OSError as e:
        print(f"Failed to backup firmware: {e}")   # Print an error message if backup fails
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

def install_firmware(firmware_path, install_path):
    """Install the new firmware."""
    try:
        os.rename(firmware_path, install_path)     # Rename/move the downloaded firmware to install path
        print(f"Installed new firmware from {firmware_path} to {install_path}")  # Print a success message
    except OSError as e:
        print(f"Failed to install firmware: {e}")  # Print an error message if installation fails
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

def main():
    # Backup current firmware
    backup_current_firmware(FIRMWARE_PATH, BACKUP_PATH)

    # Download new firmware
    download_file(FIRMWARE_URL, FIRMWARE_PATH)

    # Download and verify checksum
    expected_checksum = get_checksum(CHECKSUM_URL)
    if verify_checksum(FIRMWARE_PATH, expected_checksum):
        print("Firmware verification succeeded.")  # Print a success message if firmware verification passes
    else:
        print("Firmware verification failed. Aborting update.")  # Print an error message if verification fails
        sys.exit(1)                               # Exit the script with a non-zero status code on failure

    # Install new firmware
    install_firmware(FIRMWARE_PATH, '/path/to/device_firmware.bin')  # Example path where firmware will be installed

if __name__ == '__main__':
    main()  # Run the main function if the script is executed directly
