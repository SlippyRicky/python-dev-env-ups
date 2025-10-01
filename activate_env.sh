#!/bin/bash
# Universal Python Environment Setup Script
# Compatible with macOS, Linux, and Windows (WSL/Git Bash)
# Usage: ./setup_env.sh or bash setup_env.sh
set -e  # Exit on any error

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color
BOLD='\033[1m'
UNDERLINE='\033[4m'

# Function to print colored output with emojis
print_status() {
    echo -e "${BLUE}ℹ️  [INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}✅  [SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️  [WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}❌  [ERROR]${NC} $1"
}

print_header() {
    echo -e "${PURPLE}${BOLD}=== $1 ===${NC}"
}

print_question() {
    echo -e "${CYAN}❓  [QUESTION]${NC} $1"
}

# Detect operating system
detect_os() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="Linux"
        DISTRO=$(lsb_release -si 2>/dev/null || echo "Unknown")
        VERSION=$(lsb_release -sr 2>/dev/null || echo "Unknown")
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macOS"
        DISTRO="macOS"
        VERSION=$(sw_vers -productVersion)
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
        OS="Windows"
        DISTRO="Windows (Unix-like)"
        VERSION="Unknown"
    else
        OS="Unknown"
        DISTRO="Unknown"
        VERSION="Unknown"
    fi
}

# Check if Python 3 is available
check_python() {
    print_status "Checking Python installation..."

    # Try different Python commands
    PYTHON_CMD=""
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        # Check if it's Python 3
        if python -c "import sys; exit(0 if sys.version_info >= (3, 6) else 1)" 2>/dev/null; then
            PYTHON_CMD="python"
        fi
    fi

    if [ -z "$PYTHON_CMD" ]; then
        print_error "Python 3.6+ is required but not found!"
        print_status "Please install Python 3.6+ and try again."

        # Provide installation suggestions based on OS
        case $OS in
            "Linux")
                echo "  🐧 Ubuntu/Debian: sudo apt-get install python3 python3-venv python3-pip"
                echo "  🐧 CentOS/RHEL: sudo yum install python3 python3-venv python3-pip"
                echo "  🐧 Fedora: sudo dnf install python3 python3-venv python3-pip"
                ;;
            "macOS")
                echo "  🍎 Install with Homebrew: brew install python"
                echo "  🍎 Or download from: https://www.python.org/downloads/"
                ;;
            "Windows")
                echo "  🪟 Download from: https://www.python.org/downloads/"
                echo "  🪟 Or install via Microsoft Store"
                ;;
        esac
        exit 1
    fi

    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    print_success "Found $PYTHON_VERSION at $(which $PYTHON_CMD)"
}

# Create virtual environment
create_venv() {
    print_status "Creating virtual environment..."

    if [ -d "venv" ]; then
        print_question "Virtual environment already exists. Overwrite? (y/n) "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Skipping virtual environment creation."
            return
        fi
        rm -rf venv
    fi

    $PYTHON_CMD -m venv venv

    if [ $? -eq 0 ]; then
        print_success "Virtual environment created successfully"
    else
        print_error "Failed to create virtual environment"
        print_status "You may need to install python3-venv package:"
        case $OS in
            "Linux")
                echo "  🐧 Ubuntu/Debian: sudo apt-get install python3-venv"
                echo "  🐧 CentOS/RHEL: sudo yum install python3-venv"
                ;;
        esac
        exit 1
    fi
}

# Activate virtual environment and install packages
setup_packages() {
    print_status "Activating virtual environment and installing packages..."

    # Activate virtual environment
    source venv/bin/activate

    # Upgrade pip first
    print_status "Upgrading pip..."
    python -m pip install --upgrade pip

    # Install packages
    print_status "Installing required packages..."
    pip install pytest black flake8 jupyter numpy pandas matplotlib requests

    # Generate requirements.txt
    print_status "Generating requirements.txt..."
    pip freeze > requirements.txt

    print_success "All packages installed successfully"
}

# Make scripts executable
setup_scripts() {
    print_status "Setting up activation scripts..."

    # Make shell script executable
    chmod +x activate_env.sh

    # Create a platform-specific quick-start script
    case $OS in
        "Linux"|"macOS")
            cat > quick_start.sh << 'EOF'
#!/bin/bash
# Quick start script - detects if environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating Python environment..."
    source activate_env.sh
else
    echo "Environment already activated!"
    echo "Python: $(which python)"
fi
EOF
            chmod +x quick_start.sh
            ;;
    esac

    print_success "Scripts configured"
}

# Check for proxy settings
check_proxy() {
    print_status "Checking for proxy settings..."
    if [ -z "$HTTP_PROXY" ] && [ -z "$HTTPS_PROXY" ]; then
        print_question "Do you need to set a proxy? (y/n) "
        read -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_question "Enter HTTP proxy (e.g., http://proxy.university.edu:8080): "
            read proxy
            export HTTP_PROXY=$proxy
            export HTTPS_PROXY=$proxy
            print_success "Proxy settings applied."
        fi
    fi
}

# Check for environment modules
check_modules() {
    if command -v module &> /dev/null; then
        print_status "Environment modules detected. Load a Python module if needed."
        echo "  Example: module load python/3.9"
        print_question "Press Enter to continue or Ctrl+C to load a module manually..."
        read -n 1 -r
        echo
    fi
}

# Main setup function
main() {
    print_header "Python Environment Setup for UPS M1 SGM"

    # Detect OS
    detect_os
    print_status "Operating System: $OS ($DISTRO $VERSION)"

    # Check for environment modules
    check_modules

    # Check Python
    check_python

    # Check for proxy settings
    check_proxy

    # Create virtual environment
    create_venv

    # Setup packages
    setup_packages

    # Setup scripts
    setup_scripts

    # Final success message
    print_header "Setup Complete!"
    print_success "Python environment is ready to use!"
    echo ""
    print_status "To activate the environment:"

    case $OS in
        "Linux"|"macOS")
            echo "  🐧 Linux/macOS: source activate_env.sh"
            echo "  🐧 Linux/macOS: # or"
            echo "  🐧 Linux/macOS: ./quick_start.sh"
            ;;
        "Windows")
            echo "  🪟 Windows: activate_env.bat  (in Command Prompt)"
            echo "  🪟 Windows: source activate_env.sh  (in Git Bash/WSL)"
            ;;
    esac

    echo ""
    print_status "After activation, you can:"
    echo "  • Run the example: python src/example.py"
    echo "  • Run tests: pytest tests/"
    echo "  • Start Jupyter: jupyter notebook"
    echo "  • Format code: black src/"
    echo "  • Check code style: flake8 src/"
    echo ""
    print_status "Check README.md for detailed instructions!"
}

# Run main function
main
