# 🐍 Cross-Platform Python Development Environment

A comprehensive, cross-platform Python development environment designed for **UPS M1 SGM** programming coursework. Works seamlessly on **macOS**, **Linux**, and **Windows**.

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Purpose

This repository provides a ready-to-use Python development environment that works consistently across different operating systems, perfect for academic coursework where you might need to work on:

- 🍎 **Personal Mac** (with Terminal and IntelliJ)
- 🐧 **Linux systems** (university servers, personal installations)
- 💻 **Windows computers** (school labs with Emacs)

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd python-dev-env
./check_platform.sh    # Check system compatibility
./setup_env.sh         # Automatic setup
```

### 2. Activate Environment
```bash
# macOS/Linux
source activate_env.sh

# Windows Command Prompt
activate_env.bat
```

### 3. Start Coding
```bash
python src/example.py   # Run example
pytest tests/          # Run tests
jupyter notebook        # Start Jupyter
```

## 📋 Features

### ✨ Cross-Platform Compatibility
- **Automatic OS detection** (macOS, Linux distributions, Windows)
- **Smart Python detection** (python3, python, py commands)
- **Platform-specific installation guides**
- **Consistent workflow** across all systems

### 🛠️ Development Tools
- **Testing**: pytest with example test suite
- **Code Quality**: black (formatter) + flake8 (linter)
- **Interactive Development**: Jupyter notebooks
- **Data Science**: numpy, pandas, matplotlib
- **Web Development**: requests library

### 🔧 Utility Scripts
- `setup_env.sh` - Universal environment setup
- `activate_env.sh` - Enhanced activation (Unix)
- `activate_env.bat` - Windows activation
- `check_platform.sh` - System diagnostics

## 📁 Project Structure

```
python-dev-env/
├── 📜 Scripts
│   ├── activate_env.sh         # Unix activation
│   ├── activate_env.bat        # Windows activation
│   ├── setup_env.sh           # Universal setup
│   └── check_platform.sh      # Platform diagnostics
├── 📚 Documentation
│   ├── README.md              # Main documentation
│   └── CROSS_PLATFORM_GUIDE.md # Detailed platform guide
├── 🐍 Python Code
│   ├── src/
│   │   └── example.py         # Example Python script
│   ├── tests/
│   │   └── test_example.py    # Unit tests
│   └── example_notebook.ipynb # Jupyter example
└── ⚙️ Configuration
    ├── requirements.txt        # Python dependencies
    └── .gitignore             # Git ignore rules
```

## 🖥️ Platform Support

### 🍎 macOS
- **Shells**: zsh (default), bash
- **IDEs**: IntelliJ IDEA, PyCharm, VS Code
- **Package Manager**: Homebrew compatible
- **Architecture**: Intel & Apple Silicon (M1/M2/M3)

### 🐧 Linux
- **Distributions**: Ubuntu, Debian, CentOS, RHEL, Fedora, Arch
- **Package Managers**: apt, yum, dnf, pacman
- **Desktop Environments**: GNOME, KDE, XFCE, i3
- **Editors**: Emacs, Vim, VS Code

### 💻 Windows
- **Native**: Command Prompt, PowerShell
- **Unix-like**: WSL, Git Bash, Cygwin
- **IDEs**: VS Code, PyCharm, Emacs
- **Terminals**: Windows Terminal, ConEmu

## 📦 Installation

### Prerequisites

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip build-essential
```

#### CentOS/RHEL/Fedora:
```bash
sudo dnf install python3 python3-venv python3-pip gcc gcc-c++ make
```

#### macOS:
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python
```

#### Windows:
- Download Python from [python.org](https://www.python.org/downloads/)
- Or install from Microsoft Store
- Consider using WSL for better compatibility

## 🔧 Usage Examples

### Basic Development Workflow
```bash
# Activate environment
source activate_env.sh

# Install additional packages
pip install requests beautifulsoup4

# Update requirements
pip freeze > requirements.txt

# Format code
black src/

# Check code style
flake8 src/

# Run tests
pytest tests/ -v

# Start Jupyter for data analysis
jupyter notebook
```

### Working with Different Platforms
```bash
# Check your system setup
./check_platform.sh

# Platform-specific activation:
source activate_env.sh      # macOS/Linux
activate_env.bat            # Windows CMD
source activate_env.sh      # Git Bash/WSL
```

## 🧪 Testing

The environment includes a comprehensive test suite:

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src

# Run specific test
pytest tests/test_example.py::test_basic_statistics -v
```

## 🔧 Troubleshooting

### Common Issues

**Environment not activating?**
```bash
./check_platform.sh  # Check system status
./setup_env.sh       # Recreate environment
```

**Python not found?**
- macOS: `brew install python`
- Linux: `sudo apt install python3` (or equivalent)
- Windows: Download from python.org

**Permission errors on Linux?**
```bash
chmod +x *.sh
```

See [detailed troubleshooting guide](README.md#troubleshooting) for platform-specific solutions.

## 📚 Documentation

- [`README.md`](README.md) - Comprehensive usage guide
- [`CROSS_PLATFORM_GUIDE.md`](CROSS_PLATFORM_GUIDE.md) - Platform-specific features
- [Example Notebook](example_notebook.ipynb) - Jupyter tutorial

## 🤝 Contributing

This is a personal academic repository, but feel free to:
1. Fork for your own coursework
2. Adapt for different subjects
3. Suggest improvements via issues

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Academic Context

Created for **Université Paris Saclay (UPS) M1 SGM** programming coursework. Designed to provide a consistent development environment across different computing environments encountered in academic settings.

---

**Happy Coding! 🚀**

> *"Write once, run everywhere" - now for Python development environments too!*
