#!/bin/bash
# Platform Detection Utility
# Shows detailed information about the current system and Python environment
# Usage: ./check_platform.sh

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'

print_header() {
    echo -e "${PURPLE}=== $1 ===${NC}"
}

print_info() {
    echo -e "${BLUE}$1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Detect operating system
detect_system() {
    print_header "System Information"
    
    # Basic OS detection
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="Linux"
        print_info "Operating System: $OS"
        
        # Try to get Linux distribution info
        if command -v lsb_release &> /dev/null; then
            DISTRO=$(lsb_release -si)
            VERSION=$(lsb_release -sr)
            CODENAME=$(lsb_release -sc)
            print_info "Distribution: $DISTRO $VERSION ($CODENAME)"
        elif [ -f /etc/os-release ]; then
            source /etc/os-release
            print_info "Distribution: $NAME $VERSION_ID"
        elif [ -f /etc/redhat-release ]; then
            print_info "Distribution: $(cat /etc/redhat-release)"
        else
            print_warning "Could not determine Linux distribution"
        fi
        
        # Architecture
        print_info "Architecture: $(uname -m)"
        
        # Kernel
        print_info "Kernel: $(uname -r)"
        
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macOS"
        print_info "Operating System: $OS"
        print_info "Version: $(sw_vers -productVersion)"
        print_info "Build: $(sw_vers -buildVersion)"
        print_info "Architecture: $(uname -m)"
        
    elif [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "msys" ]]; then
        OS="Windows (Unix-like)"
        print_info "Operating System: $OS"
        print_info "Environment: $OSTYPE"
        
        # Try to get Windows version if available
        if command -v cmd.exe &> /dev/null; then
            WIN_VERSION=$(cmd.exe /c ver 2>/dev/null | head -1 || echo "Unknown")
            print_info "Windows Version: $WIN_VERSION"
        fi
        
    else
        OS="Unknown"
        print_warning "Unknown operating system: $OSTYPE"
    fi
}

# Check Python installation
check_python() {
    print_header "Python Environment"
    
    # Check for python3
    if command -v python3 &> /dev/null; then
        PYTHON3_PATH=$(which python3)
        PYTHON3_VERSION=$(python3 --version)
        print_success "Python 3 found: $PYTHON3_VERSION at $PYTHON3_PATH"
    else
        print_error "python3 command not found"
    fi
    
    # Check for python
    if command -v python &> /dev/null; then
        PYTHON_PATH=$(which python)
        PYTHON_VERSION=$(python --version)
        print_info "Python found: $PYTHON_VERSION at $PYTHON_PATH"
        
        # Check if it's Python 3
        if python -c "import sys; exit(0 if sys.version_info >= (3, 0) else 1)" 2>/dev/null; then
            print_success "Python command points to Python 3"
        else
            print_warning "Python command points to Python 2"
        fi
    else
        print_error "python command not found"
    fi
    
    # Check pip
    if command -v pip3 &> /dev/null; then
        PIP3_VERSION=$(pip3 --version)
        print_success "pip3 found: $PIP3_VERSION"
    else
        print_error "pip3 not found"
    fi
    
    if command -v pip &> /dev/null; then
        PIP_VERSION=$(pip --version)
        print_info "pip found: $PIP_VERSION"
    else
        print_error "pip not found"
    fi
}

# Check virtual environment
check_venv() {
    print_header "Virtual Environment Status"
    
    if [ -d "venv" ]; then
        print_success "Virtual environment 'venv' directory exists"
        
        # Check if currently activated
        if [ -n "$VIRTUAL_ENV" ]; then
            print_success "Virtual environment is currently ACTIVATED"
            print_info "Active environment: $VIRTUAL_ENV"
            print_info "Python in use: $(which python)"
            print_info "Python version in venv: $(python --version)"
            
            # Check installed packages
            echo ""
            print_info "Installed packages in virtual environment:"
            pip list | head -10
            if [ $(pip list | wc -l) -gt 10 ]; then
                echo "... (showing first 10 packages, use 'pip list' for complete list)"
            fi
        else
            print_warning "Virtual environment exists but is NOT activated"
            print_info "To activate: source activate_env.sh"
        fi
    else
        print_error "Virtual environment 'venv' directory not found"
        print_info "To create: run ./setup_env.sh"
    fi
}

# Check project structure
check_project() {
    print_header "Project Structure"
    
    # Check for essential files
    essential_files=("README.md" "requirements.txt" "src/example.py" "tests/test_example.py")
    
    for file in "${essential_files[@]}"; do
        if [ -f "$file" ]; then
            print_success "$file exists"
        else
            print_error "$file missing"
        fi
    done
    
    # Check directories
    essential_dirs=("src" "tests")
    
    for dir in "${essential_dirs[@]}"; do
        if [ -d "$dir" ]; then
            print_success "$dir/ directory exists"
        else
            print_error "$dir/ directory missing"
        fi
    done
    
    # Check scripts
    scripts=("activate_env.sh" "activate_env.bat" "setup_env.sh")
    
    echo ""
    print_info "Activation scripts:"
    for script in "${scripts[@]}"; do
        if [ -f "$script" ]; then
            if [ -x "$script" ]; then
                print_success "$script (executable)"
            else
                print_warning "$script (not executable)"
            fi
        else
            print_error "$script missing"
        fi
    done
}

# Provide recommendations
provide_recommendations() {
    print_header "Recommendations"
    
    case $OS in
        "Linux")
            echo "📋 For Linux systems:"
            echo "   • Make sure you have python3-venv installed:"
            echo "     Ubuntu/Debian: sudo apt-get install python3-venv"
            echo "     CentOS/RHEL: sudo yum install python3-venv"
            echo "     Fedora: sudo dnf install python3-venv"
            echo "   • Install development tools if needed:"
            echo "     Ubuntu/Debian: sudo apt-get install build-essential"
            ;;
        "macOS")
            echo "📋 For macOS:"
            echo "   • Install Homebrew if not already installed:"
            echo "     /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            echo "   • Install Python via Homebrew: brew install python"
            ;;
        "Windows (Unix-like)")
            echo "📋 For Windows (WSL/Git Bash):"
            echo "   • Make sure Python is in your PATH"
            echo "   • Consider using Windows Subsystem for Linux (WSL) for better compatibility"
            ;;
    esac
    
    echo ""
    echo "🚀 Quick start:"
    echo "   1. If virtual environment doesn't exist: ./setup_env.sh"
    echo "   2. To activate environment: source activate_env.sh"
    echo "   3. To test everything: python src/example.py && pytest tests/"
}

# Main function
main() {
    echo -e "${CYAN}╔══════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║          Python Environment Platform Check          ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    detect_system
    echo ""
    check_python
    echo ""
    check_venv
    echo ""
    check_project
    echo ""
    provide_recommendations
}

# Run main function
main