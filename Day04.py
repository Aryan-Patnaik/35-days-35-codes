import bcrypt  # Import the bcrypt library for password hashing

# Define a function to hash the password
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()  # Generate a salt for hashing
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)  # Hash the password with the salt
    return hashed_password.decode('utf-8')  # Decode the hashed password to a string and return it

# Define a function to check if a password matches the hashed password
def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))  # Compare the password and hashed password

# Main block of the program
if _name_ == "_main_":
    print("User Sign-Up")  # Print a message for user sign-up
    original_password = input("Enter a password to sign up: ")  # Prompt the user to enter a password for sign-up
    hashed = hash_password(original_password)  # Hash the entered password
    print("Your password has been securely stored.")  # Inform the user that the password has been stored securely

    print("\nUser Login")  # Print a message for user login
    entered_password = input("Enter your password to log in: ")  # Prompt the user to enter their password for login
    is_correct = check_password(entered_password, hashed)  # Check if the entered password matches the stored hashed password

    # Check if the login was successful
    if is_correct:
        print("Login successful! The password matches.")  # Print a success message if the password matches
    else:
        print("Login failed! The password does not match.")  # Print an error message if the password does not match
