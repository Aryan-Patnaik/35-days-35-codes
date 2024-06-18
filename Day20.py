import re  # Importing the 're' module for regular expressions

def detect_credit_card_leak(data):
    # Regular expression pattern to match credit card numbers
    credit_card_pattern = r'\b(?:\d[ -]*?){13,16}\b'

    # Finding all matches of the credit card pattern in the data
    matches = re.findall(credit_card_pattern, data)

    # If matches are found, log potential leakage and return True
    if matches:
        log_potential_leak(data, matches)
        return True
    else:
        return False

def log_potential_leak(data, matches):
    # Logging function to print details of potential data leakage
    print("Potential data leakage detected:")
    print(f"Data: {data}")  # Printing the original data
    print(f"Matches found: {matches}")  # Printing the credit card numbers found
    print("---")  # Printing a separator

def main():
    sensitive_data1 = "Here is a credit card number: 1234-5678-9876-5432"
    sensitive_data2 = "No sensitive information here."

    # Checking for potential data leakage in sensitive_data1
    if detect_credit_card_leak(sensitive_data1):
        print("Potential data leakage detected.")
    else:
        print("No potential data leakage.")

    # Checking for potential data leakage in sensitive_data2
    if detect_credit_card_leak(sensitive_data2):
        print("Potential data leakage detected.")
    else:
        print("No potential data leakage.")

if __name__ == "__main__":
    main()
