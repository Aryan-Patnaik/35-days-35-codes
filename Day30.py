import requests  # Importing the requests library to handle HTTP requests
import json  # Importing the JSON library to handle JSON data
import time  # Importing the time library to handle sleep intervals

# Constants for AbuseIPDB API
ABUSEIPDB_API_KEY = '*********************************************************************************'  # Your AbuseIPDB API key
ABUSEIPDB_ENDPOINT = 'https://****************.com/api/v2/blacklist'  # AbuseIPDB API endpoint for fetching blacklist data

# Constants for SIEM API
SIEM_API_ENDPOINT = 'https://your_siem_endpoint/api/threat-intelligence'  # SIEM API endpoint for sending threat intelligence data
SIEM_API_KEY = '*********************************************************************************'  # Your SIEM API key

def fetch_threat_intelligence():
    """
    Fetches threat intelligence data from the AbuseIPDB API.
    """
    headers = {
        'Key': ABUSEIPDB_API_KEY,  # Set the API key in the request header
        'Accept': 'application/json'  # Set the Accept header to 'application/json'
    }

    response = requests.get(ABUSEIPDB_ENDPOINT, headers=headers)  # Send a GET request to the AbuseIPDB API endpoint
    
    if response.status_code == 200:  # Check if the response status code is 200 (OK)
        return response.json()  # Return the JSON response data
    else:
        print(f"Failed to fetch threat intelligence data: {response.status_code}")  # Print an error message if the request failed
        return None  # Return None if the request failed

def format_data_for_siem(data):
    """
    Formats the fetched threat intelligence data to be compatible with the SIEM API.
    """
    formatted_data = []  # Initialize an empty list to store formatted data

    for entry in data['data']:  # Iterate over each entry in the data
        formatted_entry = {
            'ip': entry['ipAddress'],  # Extract the IP address
            'threat_score': entry['abuseConfidenceScore'],  # Extract the threat score
            'last_reported': entry['lastReportedAt']  # Extract the last reported date
        }
        formatted_data.append(formatted_entry)  # Append the formatted entry to the list

    return formatted_data  # Return the formatted data list

def send_to_siem(formatted_data):
    """
    Sends the formatted threat intelligence data to the SIEM API.
    """
    headers = {
        'Content-Type': 'application/json',  # Set the Content-Type header to 'application/json'
        'Authorization': f'Bearer {SIEM_API_KEY}'  # Set the Authorization header with the SIEM API key
    }

    response = requests.post(SIEM_API_ENDPOINT, headers=headers, data=json.dumps(formatted_data))  # Send a POST request with the formatted data

    if response.status_code == 200:  # Check if the response status code is 200 (OK)
        print("Threat intelligence data successfully sent to SIEM.")  # Print a success message
    else:
        print(f"Failed to send data to SIEM: {response.status_code} - {response.text}")  # Print an error message if the request failed

def main():
    """
    Main function that runs the data fetching, formatting, and sending process in a loop.
    """
    while True:  # Infinite loop to keep the process running
        print("Fetching threat intelligence data...")  # Print a message indicating data fetching
        data = fetch_threat_intelligence()  # Fetch the threat intelligence data

        if data:  # Check if data fetching was successful
            print("Formatting data for SIEM...")  # Print a message indicating data formatting
            formatted_data = format_data_for_siem(data)  # Format the fetched data

            print("Sending data to SIEM...")  # Print a message indicating data sending
            send_to_siem(formatted_data)  # Send the formatted data to SIEM
        
        # Wait for a specific interval before fetching the data again (e.g., every hour)
        time.sleep(3600)  # Sleep for 3600 seconds (1 hour)

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
