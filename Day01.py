# Script to scan open ports on a given IP address

import socket  # Importing the socket module for performing network communication

# Function for validating the IP address
def is_valid_ip(ip):
    ip_parts = ip.split('.')  # Splitting the IP address into parts using the dot '.' as the delimiter
    if len(ip_parts) != 4:  # Checking if the number of parts in the IP address is exactly 4
        print("Length more than 4")  # If not, print a message indicating the issue
        return False  # Return False indicating the IP address is invalid
    for part in ip_parts:  # Iterating over each part of the IP address
        if not part.isdigit():  # Checking if the part contains only digits
            print("Non-digit found")  # If not, print a message indicating the issue
            return False  # Return False indicating the IP address is invalid
        if int(part) > 255 or int(part) < 0:  # Checking if the part is within the valid range (0-255)
            print("Value out of range")  # If not, print a message indicating the issue
            return False  # Return False indicating the IP address is invalid
    return True  # If all checks pass, return True indicating the IP address is valid

# Function for extracting and validating the port range
def extract_port_range(port_range):
    ports = port_range.split('-')  # Splitting the port range into start and end parts using the hyphen '-'
    if len(ports) != 2:  # Checking if there are exactly two parts in the port range
        print("More than 2")  # If not, print a message indicating the issue
        return False  # Return False indicating the port range is invalid
    if not ports[0].isdigit() or not ports[1].isdigit():  # Checking if both parts are digits
        print("Not digit")  # If not, print a message indicating the issue
        return False  # Return False indicating the port range is invalid
    if int(ports[0]) > int(ports[1]):  # Checking if the start port is greater than the end port
        print("Start is greater than end")  # If so, print a message indicating the issue
        return False  # Return False indicating the port range is invalid
    if int(ports[0]) < 0 or int(ports[0]) > 65535 or int(ports[1]) < 0 or int(ports[1]) > 65535:  # Checking if the ports are within the valid range (0-65535)
        print("Out of bound")  # If not, print a message indicating the issue
        return False  # Return False indicating the port range is invalid
    return True  # If all checks pass, return True indicating the port range is valid

# Prompt the user to input the IP address and port range
IP_PORT = input("Enter the IP address and port range (Eg. 127.0.0.1 75-85): ")

# Split the user input into the IP address and port range
IP, PORT = IP_PORT.split(' ')

# Print the provided IP address and port range for confirmation
print("Given IP:", IP)
print("Given port range:", PORT)

# Initialize a list to store open ports
open_ports = []

# Extract the starting and ending ports from the provided port range and convert them to integers
start, end = map(int, PORT.split('-'))

# Loop through each port in the specified range
for port in range(start, end + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object for IPv4 and TCP connections
        s.settimeout(0.5)  # Set the timeout for the socket to 0.5 seconds
        s.connect((IP, port))  # Attempt to connect to the specified IP address and port
        open_ports.append(port)  # If the connection is successful, add the port to the list of open ports
        s.close()  # Close the socket connection
    except:  # If an error occurs (e.g., connection timeout or refused), continue to the next port
        pass

# Print the list of open ports
print("Open ports: ", end='')
for port in open_ports:
    print(port, end=' ')

# Enter the IP address and port range (Eg. 127.0.0.1 75-85): 142.250.194.14 75-85
# Given IP: 142.250.194.14
# Given port range: 75-85
# Open ports: 80
