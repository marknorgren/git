# git-binary-lfs-hook

Automatically detect and track binary files with Git LFS, regardless of their file extension.

This pre-commit hook analyzes file content to determine if it's binary and automatically configures Git LFS tracking when needed.

## Features

- Content-based binary detection (not extension-based)
- Automatic Git LFS configuration
- Handles files without extensions
- Prevents accidental commits of untracked binary files
- Comprehensive test suite
- CI/CD integration

## Installation

1. Install Git LFS if you haven't already:
```bash
# macOS
brew install git-lfs

# Ubuntu/Debian
apt-get install git-lfs

# Windows (with Chocolatey)
choco install git-lfs
```

2. Install the hook:
```bash
# Option 1: Using curl
curl -o .git/hooks/pre-commit https://raw.githubusercontent.com/marknorgren/git/git-binary-lfs-hook/src/pre-commit
chmod +x .git/hooks/pre-commit

# Option 2: Clone and copy
git clone https://github.com/marknorgren/git/git-binary-lfs-hook.git
cp git-binary-lfs-hook/src/pre-commit .git/hooks/
chmod +x .git/hooks/pre-commit
```

## Usage

The hook works automatically once installed. When you try to commit files:

1. Each staged file is analyzed for binary content
2. If a binary file is detected:
   - It's automatically added to Git LFS tracking
   - The .gitattributes file is updated
   - You'll need to commit again to include these changes

Example:
```bash
# Stage some files
git add .

# Try to commit
git commit -m "Add files"

# If binary files are detected, you'll see:
# "Binary files detected and added to Git LFS.
#  Please commit again to include these changes."

# Commit again
git commit -m "Add files"
```

## Development

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/git-binary-lfs-hook.git
cd git-binary-lfs-hook
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

```bash
pytest -v
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run the tests
5. Submit a pull request

All PRs must:
- Pass all tests
- Include tests for new functionality
- Follow the existing code style
- Update documentation as needed

## License

MIT License - see LICENSE file for details

## Troubleshooting

### Common Issues

1. **Hook not executing**: Make sure it's executable (`chmod +x pre-commit`)
2. **'file' command not found**: Install the `file` package for your OS
3. **Git LFS not initialized**: Run `git lfs install` in your repository

### Getting Help

- Open an issue on GitHub
- Check existing issues for solutions
- Include your OS and Git version when reporting issues

## Acknowledgments

[Claude](https://claude.ai) helped with this solution. 😀
