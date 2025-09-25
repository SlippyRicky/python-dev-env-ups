# 🚀 GitHub Setup Guide

## Step 1: Create a Private Repository on GitHub

### Via GitHub Website (Recommended)
1. **Go to GitHub**: [https://github.com](https://github.com)
2. **Sign in** to your account
3. **Click the "+" icon** in the top-right corner
4. **Select "New repository"**

### Repository Settings:
- **Repository name**: `python-dev-env-ups` (or your preferred name)
- **Description**: `Cross-platform Python development environment for UPS M1 SGM coursework`
- **Visibility**: ✅ **Private** (keep this checked for your personal coursework)
- **Initialize repository**: ❌ Leave all checkboxes unchecked (we already have our files)
- **Click "Create repository"**

## Step 2: Connect Your Local Repository

GitHub will show you setup instructions. Use this command sequence:

```bash
# Add the remote repository (replace USERNAME with your GitHub username)
git remote add origin https://github.com/USERNAME/python-dev-env-ups.git

# Push your code to GitHub
git push -u origin main
```

### Alternative: Using SSH (More Secure)
If you have SSH keys set up:
```bash
git remote add origin git@github.com:USERNAME/python-dev-env-ups.git
git push -u origin main
```

## Step 3: Verify the Upload

1. **Refresh your GitHub repository page**
2. **You should see all your files**:
   - ✅ README.md with the project description
   - ✅ All scripts (activate_env.sh, setup_env.sh, etc.)
   - ✅ Source code (src/, tests/)
   - ✅ Documentation files
   - ❌ No venv/ directory (ignored by .gitignore)

## Step 4: Set Up Your Development Workflow

### For Your Mac (Current System):
```bash
# Clone to a new location (optional)
git clone https://github.com/USERNAME/python-dev-env-ups.git
cd python-dev-env-ups

# Set up the environment
./setup_env.sh
source activate_env.sh
```

### For School Windows Computers:
1. **Install Git for Windows** (if not available)
2. **Clone the repository**:
   ```bash
   git clone https://github.com/USERNAME/python-dev-env-ups.git
   cd python-dev-env-ups
   ```
3. **Activate environment**:
   ```cmd
   activate_env.bat
   ```

### For Linux Systems:
```bash
git clone https://github.com/USERNAME/python-dev-env-ups.git
cd python-dev-env-ups
./check_platform.sh
./setup_env.sh
source activate_env.sh
```

## Step 5: Daily Workflow

### When Starting Work:
```bash
# Update from GitHub (get latest changes)
git pull

# Activate your environment
source activate_env.sh  # macOS/Linux
# or
activate_env.bat        # Windows
```

### When Finishing Work:
```bash
# Add your changes
git add .

# Commit with a descriptive message
git commit -m "Add: homework exercise 3 - data analysis with pandas"

# Push to GitHub
git push
```

## Common Git Commands for Your Coursework

### Basic Operations:
```bash
# Check status of your files
git status

# See what changes you've made
git diff

# View commit history
git log --oneline

# Add specific files
git add src/homework1.py tests/test_homework1.py

# Commit with message
git commit -m "Complete homework 1: basic statistics functions"
```

### Working with Branches (Advanced):
```bash
# Create a new branch for an assignment
git checkout -b homework-2

# Work on your assignment...

# Switch back to main branch
git checkout main

# Merge your completed work
git merge homework-2
```

## Repository Management Tips

### 📁 Organizing Your Coursework:
```
python-dev-env-ups/
├── assignments/
│   ├── week1/
│   ├── week2/
│   └── ...
├── projects/
│   ├── project1/
│   └── project2/
├── src/           # Keep the original example
├── tests/         # Keep the original tests
└── notebooks/     # Jupyter notebooks
```

### 🏷️ Good Commit Message Examples:
```bash
git commit -m "Add: Week 3 assignment - numpy array operations"
git commit -m "Fix: error handling in data validation function"
git commit -m "Update: documentation for statistics module"
git commit -m "Complete: final project - data visualization dashboard"
```

### 🔒 Keeping It Private:
- Your repository is **private** - only you can see it
- Perfect for coursework and assignments
- You can add collaborators (like project partners) if needed
- GitHub provides unlimited private repositories for students

## Troubleshooting

### If remote origin already exists:
```bash
git remote remove origin
git remote add origin https://github.com/USERNAME/python-dev-env-ups.git
```

### If you get authentication errors:
1. **Use HTTPS with token**: Generate a Personal Access Token in GitHub settings
2. **Set up SSH keys**: More secure for regular use
3. **Use GitHub CLI**: `gh auth login`

### If you need to change repository name later:
1. Go to repository **Settings** on GitHub
2. Scroll to **Repository name** section
3. Change the name and **confirm**

## Next Steps

1. **✅ Create the GitHub repository** using the instructions above
2. **✅ Push your code** to GitHub
3. **🔄 Test cloning** on a different system (if available)
4. **📚 Start adding your coursework** to organized folders
5. **🔗 Share the repository** with professors if required (add as collaborators)

## Benefits of Using Git + GitHub for Coursework

- 📚 **Version Control**: Never lose your work
- 🔄 **Sync Everywhere**: Access your code on any computer
- 🕒 **History**: See how your coding skills improve over time
- 🤝 **Collaboration**: Work with classmates on group projects
- 💼 **Portfolio**: Showcase your work to potential employers
- 🔒 **Backup**: Your work is safely stored in the cloud

---

**Happy Coding with Git! 🎓**