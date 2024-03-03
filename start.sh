#!/bin/bash


install_dependencies() {
    echo "Installing Flask and OpenAPI dependencies..."
    pip install --upgrade pip
    pip install flask
    pip install openai
    pip install python-dotenv
}

activate_env() {
    # Create and activate virtual environment
    echo "Creating and activating virtual environment..."
    source .venv/bin/activate
}


if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    echo "Detected macOS."
    echo "Creating and activating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    install_dependencies
    echo "Running main.py..."
    cd backend
    python3 main.py
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    echo "Detected Linux. Make sure you have Python and pip installed."
    echo "Creating and activating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    install_dependencies
    echo "Running main.py..."
    cd backend
    python3 main.py
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows
    echo "Detected Windows. This script does not support Windows."
    echo "Creating and activating virtual environment..."
    python -m venv .venv
    ./.venv/Scripts/activate
    install_dependencies
    echo "Running main.py..."
    cd backend
    python main.py
else
    echo "Unsupported operating system."
    exit 1
fi

# # Install dependencies inside the virtual environment
# echo "Installing Python dependencies..."
# pip install -r requirements.txt

# Run main.py
