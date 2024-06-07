# Import the bleach library for HTML sanitization
import bleach

# Define the allowed HTML tags
ALLOWED_TAGS = ['b', 'i', 'u', 'em', 'strong', 'a', 'p', 'ul', 'ol', 'li', 'br']

# Define the allowed attributes for the 'a' tag
ALLOWED_ATTRIBUTES = {'a' : ['href', 'title']}

# Define the allowed protocols for links
ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']

# Define a function to sanitize user input to prevent XSS
def sanitize_input(user_input):
    # Use the bleach library to clean the user input
    sanitized_input = bleach.clean(
        user_input,
        tags = ALLOWED_TAGS,
        attributes = ALLOWED_ATTRIBUTES,
        protocols = ALLOWED_PROTOCOLS,
        strip = True
    )
    return sanitized_input

# Main function to demonstrate usage
if __name__ == '__main__':
    # Example of raw user input containing a potential XSS attack
    raw_input = '<script>alert("XSS Attack!");</script><b>Valid Input</b>'
    print("Raw Input:", raw_input)
    
    # Sanitize the input
    safe_input = sanitize_input(raw_input)
    
    # Print the sanitized input
    print("Sanitized Input:", safe_input)
