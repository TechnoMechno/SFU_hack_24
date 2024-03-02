#!/bin/bash

install_virtualenv() {
    echo "Installing Python virtual environment..."
    python3 -m venv backend/.venv
}

install_dependencies() {
    echo "Installing Flask and OpenAPI dependencies..."
    pip install Flask
    pip install openapi
    pip install python-dotenv
}

activate_env() {
    # Create and activate virtual environment
    echo "Creating and activating virtual environment..."
    source backend/.venv/bin/activate
}


if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "Detected macOS."
    install_virtualenv
    source backend/.venv/bin/activate
    install_dependencies
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "Detected Linux. Make sure you have Python and pip installed."
    install_virtualenv
    source backend/.venv/bin/activate
    install_dependencies
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    echo "Detected Windows. This script does not support Windows."
    install_virtualenv
    source backend/.venv/Scripts/activate
    install_dependencies
else
    echo "Unsupported operating system."
    exit 1
fi

# # Install dependencies inside the virtual environment
# echo "Installing Python dependencies..."
# pip install -r requirements.txt

# Run main.py
echo "Running main.py..."
python3 backend/main.py
