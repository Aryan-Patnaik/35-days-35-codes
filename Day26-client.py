import socket  # Import the socket module for network communication
import threading  # Import the threading module for handling multiple threads
from tkinter import *  # Import all classes and functions from the Tkinter module for GUI
from PIL import Image, ImageTk  # Import the Image and ImageTk classes from PIL for image processing
from io import BytesIO  # Import the BytesIO module for handling byte data

class RemoteDesktopClient:
    def __init__(self, master):
        self.master = master  # Set the master (root) window
        self.master.title("Remote Desktop Client")  # Set the title of the window
        self.label = Label(master)  # Create a label widget for displaying the screen image
        self.label.pack()  # Pack the label widget into the window
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
        self.client.connect(('server_ip_address', 9999))  # Connect to the server at the specified IP address and port
        self.update_screen()  # Start the screen update process

    def update_screen(self):
        try:
            screen_size = int.from_bytes(self.client.recv(4), 'big')  # Receive the size of the screen data
            screen_data = self.client.recv(screen_size)  # Receive the screen data

            screen_image = Image.open(BytesIO(screen_data))  # Convert the byte data to an image
            screen_photo = ImageTk.PhotoImage(screen_image)  # Convert the image to a format suitable for Tkinter
            self.label.config(image=screen_photo)  # Update the label with the new image
            self.label.image = screen_photo  # Keep a reference to the image to prevent garbage collection

            self.master.after(100, self.update_screen)  # Schedule the next screen update after 100 milliseconds

        except Exception as e:
            print(f"Error: {e}")  # Print an error message if an exception occurs

    def send_command(self, command):
        command_data = command.encode('utf-8')  # Encode the command as a UTF-8 byte string
        self.client.sendall(len(command_data).to_bytes(4, 'big') + command_data)  # Send the length and byte data of the command to the server

if __name__ == "__main__":
    root = Tk()  # Create the main Tkinter window
    client = RemoteDesktopClient(root)  # Create an instance of the RemoteDesktopClient class
    root.mainloop()  # Start the Tkinter main event loop
