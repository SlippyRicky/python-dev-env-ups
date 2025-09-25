#!/bin/bash
# Cross-platform activation script for Unix-like systems (Mac/Linux)
# Usage: source activate_env.sh

# Detect the operating system
OS="Unknown"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS="Linux"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macOS"
elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
    OS="Windows (Unix-like)"
fi

echo "=== Python Environment Activation ==="
echo "Operating System: $OS"
echo "Activating Python virtual environment..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Error: Virtual environment 'venv' not found!"
    echo "Please run the setup script first or create the virtual environment manually."
    return 1
fi

# Activate the virtual environment
source venv/bin/activate

# Check if activation was successful
if [ $? -eq 0 ]; then
    echo "✅ Virtual environment activated successfully!"
    echo ""
    echo "📊 Environment Information:"
    echo "  Python version: $(python --version)"
    echo "  Pip version: $(pip --version | cut -d' ' -f1-2)"
    echo "  Virtual env path: $(which python)"
    echo ""
    echo "📁 Current directory: $(pwd)"
    echo ""
    echo "🔧 Common commands:"
    echo "  • Run example: python src/example.py"
    echo "  • Run tests: pytest tests/"
    echo "  • Start Jupyter: jupyter notebook"
    echo "  • Format code: black src/"
    echo "  • Check style: flake8 src/"
    echo ""
    echo "🚪 To deactivate: deactivate"
else
    echo "❌ Error: Failed to activate virtual environment!"
    return 1
fi
