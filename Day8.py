import time  # Import the time module for time-related operations
from watchdog.observers import Observer  # Import Observer class from watchdog module
from watchdog.events import FileSystemEventHandler  # Import FileSystemEventHandler class from watchdog module
import os  # Import the os module for operating system related functionalities

# Define a custom event handler class for critical files
class CriticalFileEventHandler(FileSystemEventHandler):
    def __init__(self, files_to_watch):
        self.files_to_watch = files_to_watch

    # Define method to handle file modification event
    def on_modified(self, event):
        if event.src_path in self.files_to_watch:
            print(f'File modified: {event.src_path}')

    # Define method to handle file creation event
    def on_created(self, event):
        if event.src_path in self.files_to_watch:
            print(f'File created: {event.src_path}')

    # Define method to handle file deletion event
    def on_deleted(self, event):
        if event.src_path in self.files_to_watch:
            print(f'File deleted: {event.src_path}')

# Define function to monitor critical files
def monitor_files(files_to_watch):
    event_handler = CriticalFileEventHandler(files_to_watch)  # Create an instance of the custom event handler
    observer = Observer()  # Create an observer object

    # Determine the directories to watch
    directory_to_watch = set()
    for file in files_to_watch:
        directory_to_watch.add(os.path.dirname(file))

    # Schedule event handler for each directory
    for directory in directory_to_watch:
        observer.schedule(event_handler, directory, recursive=False)

    # Start the observer
    observer.start()
    print(f"Monitoring {', '.join(files_to_watch)} for changes...")

    try:
        # Keep the script running until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Stop the observer if interrupted
        observer.stop()

    # Wait for the observer to terminate
    observer.join()

# Main section of the script
if __name__ == "__main__":
    # List of critical files to monitor
    files_to_watch = [
        './file1.txt',
        './file2.txt',
        './file3.txt'
    ]
    # Convert file paths to absolute paths
    files_to_watch = [os.path.abspath(file) for file in files_to_watch]

    # Call the function to monitor critical files
    monitor_files(files_to_watch)