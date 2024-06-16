import re

# Function to validate the password based on given criteria
def validate_password(password):
    # Minimum length of the password
    min_length = 8
    
    # Check if the password contains at least one uppercase letter
    contains_uppercase = re.search(r'[A-Z]', password)
    
    # Check if the password contains at least one lowercase letter
    contains_lowercase = re.search(r'[a-z]', password)
    
    # Check if the password contains at least one digit
    contains_digit = re.search(r'[0-9]', password)
    
    # Check if the password contains at least one special character
    contains_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)
    
    # Initialize an empty list to store error messages
    errors = []

    # Check if the password meets the minimum length requirement
    if len(password) < min_length:
        errors.append(f"Password must be at least {min_length} characters long.")
    
    # Check if the password contains an uppercase letter
    if not contains_uppercase:
        errors.append("Password must contain at least one uppercase letter.")
    
    # Check if the password contains a lowercase letter
    if not contains_lowercase:
        errors.append("Password must contain at least one lowercase letter.")
    
    # Check if the password contains a digit
    if not contains_digit:
        errors.append("Password must contain at least one digit.")
    
    # Check if the password contains a special character
    if not contains_special:
        errors.append("Password must contain at least one special character.")

    # Return validation result and corresponding messages
    if errors:
        return False, errors
    else:
        return True, "Password is valid."

# Main function to run the password validation
if __name__ == "__main__":
    # Prompt the user to enter a password for validation
    password = input("Enter a password to validate: ")
    
    # Validate the entered password
    is_valid, feedback = validate_password(password)

    # Print the validation result
    if is_valid:
        print(feedback)
    else:
        print("Password is not valid:")
        for error in feedback:
            print(f"- {error}")
