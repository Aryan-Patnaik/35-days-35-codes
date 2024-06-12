import os
import mimetypes

# Define a list of allowed MIME types
ALLOWED_MIME_TYPES = [
    'image/jpeg',      # JPEG images
    'image/png',       # PNG images
    'application/pdf', # PDF documents
    'text/plain',      # Plain text files
]

def is_allowed_file(file_path):
    # Guess the MIME type of the file based on its file extension
    mime_type, _ = mimetypes.guess_type(file_path)
    
    # Check if the guessed MIME type is in the list of allowed MIME types
    if mime_type in ALLOWED_MIME_TYPES:
        return True  # Return True if the file type is allowed
    else:
        return False # Return False if the file type is not allowed

def main():
    # Define the path to the file to check
    file_path = '/file1.txt'

    # Check if the file is allowed based on its MIME type
    if is_allowed_file(file_path):
        # Print a message if the file is allowed
        print(f'The file "{os.path.basename(file_path)}" is allowed.')
    else:
        # Print a message if the file is not allowed
        print(f'The file "{os.path.basename(file_path)}" is not allowed.')

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
