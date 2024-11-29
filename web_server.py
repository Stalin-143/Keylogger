from flask import Flask, render_template_string, send_file, request, Response
import os
from functools import wraps

print(r"""
             __        __   _       ____                           
             \ \      / /__| |__   / ___|  ___ _ ____   _____ _ __ 
              \ \ /\ / / _ \ '_ \  \___ \ / _ \ '__\ \ / / _ \ '__|
               \ V  V /  __/ |_) |  ___) |  __/ |   \ V /  __/ |   
                \_/\_/ \___|_.__/  |____/ \___|_|    \_/ \___|_|   


Github:https://github.com/Stalin-143
""")





app = Flask(__name__)


# Specify the location of the log file (this should be provided by the user)
log_file_path = input("Enter the file path: ")
 # Change this as needed

# Basic Authentication
USERNAME = 'admin'
PASSWORD = 'admin'

# Function to prompt for username and password if not authenticated
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

# Function to require authentication for routes
def authenticate():
    return Response(
        'Unauthorized Access. Please log in with correct credentials.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})

# Decorator to enforce authentication
def requires_auth(f):
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
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Log File: {{ log_file_path }}</h1>

    <h2>Log File Contents:</h2>
    <pre>{{ log_contents }}</pre>

    <a href="{{ url_for('download_log') }}" class="button">Download Log File</a>
</body>
</html>
'''

# Route to display the log file contents and provide a download link
@app.route('/')
@requires_auth
def home():
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as file:
            log_contents = file.read()
    else:
        log_contents = "Log file not found."

    return render_template_string(HTML_TEMPLATE, log_file_path=log_file_path, log_contents=log_contents)

# Route to download the log file
@app.route('/download')
@requires_auth
def download_log():
    if os.path.exists(log_file_path):
        return send_file(log_file_path, as_attachment=True)
    return "Log file not found."

if __name__ == '__main__':
    app.run(debug=True)
