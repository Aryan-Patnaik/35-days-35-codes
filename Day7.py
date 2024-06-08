from flask import Flask, make_response, request  # Import necessary Flask modules

app = Flask(__name__)  # Create a Flask application instance

@app.after_request
def add_security_headers(response):
    # Add security headers to the response
    response.headers['X-Content-Type-Options'] = 'nosniff'  # Prevent MIME-sniffing attacks
    response.headers['X-Frame-Options'] = 'DENY'  # Prevent clickjacking attacks
    response.headers['X-XSS-Protection'] = '1; mode=block'  # Enable XSS protection in modern browsers
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'  # Enforce HTTPS for a period of time

    return response  # Return the modified response with security headers

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':  # Check if the request method is POST
        user_input = request.form.get('user_input', '')  # Get user input from the form
        return f'You entered: {user_input}'  # Display the user input
    else:
        # Display a form for the user to input text
        return '''
        <form method="POST">
            <label for="user_input">Enter your text:</label><br>
            <input type="text" id="user_input" name="user_input"><br>
            <input type="submit" value="Submit">
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
