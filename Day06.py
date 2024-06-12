import secrets  # Import the 'secrets' module for generating random tokens
import string   # Import the 'string' module for accessing ASCII characters

class CSRFTokenManager:
    def __init__(self):
        self.token_length = 32  # Length of the CSRF token

    def generate_token(self):
        alphabet = string.ascii_letters + string.digits  # Define the character set for the token
        csrf_token = ''.join(secrets.choice(alphabet) for _ in range(self.token_length))  # Generate the CSRF token
        return csrf_token  # Return the generated token

class FormWithCSRF:
    def __init__(self, form_action):
        self.form_action = form_action  # Form action URL
        self.csrf_token_manager = CSRFTokenManager()  # Instantiate the CSRF token manager

    def generate_form_with_csrf(self):
        csrf_token = self.csrf_token_manager.generate_token()  # Generate CSRF token

        form_html = f'''  # Define the HTML form with f-string formatting
        <form action="{self.form_action}" method="POST">  <!-- Start of the form -->
            <input type="hidden" name="csrf_token" value="{csrf_token}">  <!-- CSRF token input field -->
            <!-- Other form fields -->
            <input type="submit" value="Submit">  <!-- Submit button -->
        </form>  <!-- End of the form -->
        '''
        return form_html  # Return the generated HTML form

if __name__ == "__main__":
    form = FormWithCSRF("/submit_form")  # Instantiate FormWithCSRF with form action URL
    form_with_csrf = form.generate_form_with_csrf()  # Generate form with CSRF token
    print(form_with_csrf)  # Print the generated form HTML
