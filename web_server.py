from flask import Flask, render_template, send_file, request, Response, redirect, url_for, make_response, render_template_string
import os
import pyfiglet

# Use pyfiglet for CLI art
ascii_banner = pyfiglet.figlet_format("Web Server")
print(ascii_banner)

app = Flask(__name__, static_folder="Sign in")

# Ask user where the log file is
log_file_path = input("Enter the full path for the log file (e.g., /path/to/logfile.txt): ")

# Secret key for sessions
app.secret_key = 'your_super_secret_key_here'

# Serve login/signup page
@app.route('/login')
def login():
    return send_file('Sign in/index.html')

# Handle login form submission
@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username and password:
        resp = make_response(redirect(url_for('home')))
        resp.set_cookie('session_id', 'authenticated_user', max_age=3600, httponly=True)
        return resp
    return 'Invalid Credentials', 401

@app.route('/')
def home():
    session_id = request.cookies.get('session_id')

    if session_id == 'authenticated_user':
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as file:
                log_contents = file.read()
        else:
            log_contents = "Log file not found."
        return render_template_string(HTML_TEMPLATE, log_file_path=log_file_path, log_contents=log_contents)
    return redirect(url_for('login'))

@app.route('/download')
def download_log():
    session_id = request.cookies.get('session_id')
    if session_id == 'authenticated_user':
        if os.path.exists(log_file_path):
            return send_file(log_file_path, as_attachment=True)
        return "Log file not found."
    return redirect(url_for('login'))

# Logout
@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login')))
    resp.set_cookie('session_id', '', expires=0)
    return resp

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keylogger Log Viewer</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f0f0f0; margin: 0; padding: 20px; }
        h1 { color: #333; }
        pre { background-color: #fff; padding: 15px; border: 1px solid #ccc; max-height: 400px; overflow-y: scroll; }
        .button { padding: 10px 15px; background-color: #4CAF50; color: white; text-align: center; border: none; cursor: pointer; margin-top: 20px; text-decoration: none; }
        .button:hover { background-color: #45a049; }
        .logout { background-color: #f44336; margin-left: 10px; }
        .logout:hover { background-color: #d32f2f; }
    </style>
</head>
<body>
    <h1>Log File: {{ log_file_path }}</h1>
    <h2>Log File Contents:</h2>
    <pre>{{ log_contents }}</pre>
    <a href="{{ url_for('download_log') }}" class="button">Download Log File</a>
    <a href="{{ url_for('logout') }}" class="button logout">Logout</a>
</body>
</html>
'''

if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
