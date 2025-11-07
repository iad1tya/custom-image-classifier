# Contributing to Custom Image Classifier

First off, thank you for considering contributing to Custom Image Classifier! It's people like you that make this project better for everyone.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Community](#community)

---

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the [existing issues](https://github.com/iad1tya/custom-image-classifier/issues) to avoid duplicates.

**When you create a bug report, please include:**

- A clear and descriptive title
- Detailed steps to reproduce the issue
- Expected behavior vs. actual behavior
- Screenshots (if applicable)
- Your environment (OS, Python version, PyTorch version)
- Any relevant error messages or logs

**Bug Report Template:**

```markdown
## Bug Description
A clear description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g., macOS 13.0, Ubuntu 22.04]
- Python Version: [e.g., 3.9.7]
- PyTorch Version: [e.g., 2.1.0]
- Browser (if applicable): [e.g., Chrome 118]

## Additional Context
Any other context about the problem.
```

### 💡 Suggesting Enhancements

Enhancement suggestions are welcome! Please:

- Use a clear and descriptive title
- Provide a detailed description of the proposed feature
- Explain why this enhancement would be useful
- Include examples of how the feature would work
- List any potential drawbacks or challenges

### 📝 Improving Documentation

Documentation improvements are always appreciated! You can help by:

- Fixing typos or grammatical errors
- Adding examples or clarifications
- Creating tutorials or guides
- Improving API documentation
- Translating documentation

### 💻 Contributing Code

We love code contributions! Here's how to get started:

1. **Find an issue to work on** or create a new one
2. **Comment on the issue** to let others know you're working on it
3. **Fork the repository** and create a branch
4. **Write your code** following our style guidelines
5. **Test your changes** thoroughly
6. **Submit a pull request**

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- Basic knowledge of PyTorch and Flask

### Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/your-username/custom-image-classifier.git
cd custom-image-classifier

# Add the upstream repository
git remote add upstream https://github.com/iad1tya/custom-image-classifier.git
```

---

## Development Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

### 2. Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -r requirements-dev.txt
```

**Development dependencies include:**
- pytest - Testing framework
- black - Code formatter
- flake8 - Linter
- mypy - Type checker
- pre-commit - Git hooks
- pytest-cov - Coverage reporting

### 3. Install Pre-commit Hooks

```bash
pre-commit install
```

This will automatically run checks before each commit.

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

**Branch naming conventions:**
- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation updates
- `refactor/` - Code refactoring
- `test/` - Test additions or modifications

---

## Pull Request Process

### 1. Make Your Changes

- Write clean, readable code
- Follow the style guidelines below
- Add tests for new functionality
- Update documentation as needed

### 2. Test Your Changes

```bash
# Run all tests
pytest

# Run tests with coverage
pytest --cov=. --cov-report=html

# Run specific tests
pytest tests/test_model.py

# Check code style
black . --check
flake8 .

# Type checking
mypy .
```

### 3. Commit Your Changes

```bash
git add .
git commit -m "feat: add new feature"
```

See [Commit Message Guidelines](#commit-message-guidelines) below.

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 5. Create a Pull Request

- Go to your fork on GitHub
- Click "New Pull Request"
- Select your branch
- Fill out the PR template
- Submit the pull request

**Pull Request Checklist:**

- [ ] Code follows the style guidelines
- [ ] All tests pass
- [ ] New tests added (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] Commit messages follow the guidelines
- [ ] PR description clearly explains the changes
- [ ] No merge conflicts
- [ ] Linked to related issue (if applicable)

### 6. Code Review

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged!

---

## Style Guidelines

### Python Code Style

We follow [PEP 8](https://pep8.org/) with some modifications:

```python
# Use Black for automatic formatting
black .

# Maximum line length: 100 characters
# Use 4 spaces for indentation (no tabs)
# Use double quotes for strings
# Add docstrings to all functions and classes
```

**Example:**

```python
def train_model(
    project_name: str,
    epochs: int = 10,
    batch_size: int = 32,
    learning_rate: float = 0.001
) -> dict:
    """
    Train a model for a given project.
    
    Args:
        project_name: Name of the project
        epochs: Number of training epochs
        batch_size: Training batch size
        learning_rate: Learning rate for optimizer
        
    Returns:
        Dictionary containing training metrics
        
    Raises:
        ValueError: If project doesn't exist
    """
    # Implementation here
    pass
```

### JavaScript Code Style

- Use ES6+ features
- Use 2 spaces for indentation
- Use semicolons
- Use camelCase for variables and functions
- Add comments for complex logic

### HTML/CSS Style

- Use 2 spaces for indentation
- Use semantic HTML5 elements
- Keep CSS organized and commented
- Mobile-first responsive design

---

## Commit Message Guidelines

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat:** New feature
- **fix:** Bug fix
- **docs:** Documentation changes
- **style:** Code style changes (formatting, missing semicolons, etc.)
- **refactor:** Code refactoring
- **test:** Adding or updating tests
- **chore:** Maintenance tasks

### Examples

```bash
# Feature
feat(training): add early stopping support

# Bug fix
fix(api): handle missing image parameter

# Documentation
docs(readme): update installation instructions

# Refactor
refactor(model): simplify CNN architecture

# Test
test(predictor): add unit tests for image preprocessing
```

### Rules

- Use present tense ("add feature" not "added feature")
- Use imperative mood ("move cursor to..." not "moves cursor to...")
- Keep subject line under 50 characters
- Capitalize the subject line
- No period at the end of subject line
- Separate subject from body with blank line
- Wrap body at 72 characters
- Explain what and why, not how

---

## Testing Guidelines

### Writing Tests

- Write tests for all new functionality
- Maintain or improve code coverage
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

**Example:**

```python
def test_model_training():
    """Test that model training completes successfully."""
    # Arrange
    project_name = "test_project"
    epochs = 2
    
    # Act
    result = train_model(project_name, epochs=epochs)
    
    # Assert
    assert result["success"] is True
    assert result["epochs_trained"] == epochs
```

### Running Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_model.py

# Run tests matching a pattern
pytest -k "train"

# Generate coverage report
pytest --cov=. --cov-report=html
```

---

## Documentation Guidelines

### Code Documentation

- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Include type hints
- Provide examples for complex functions

### README Updates

- Keep README.md up to date with new features
- Add examples for new functionality
- Update installation instructions if needed

### Changelog

- Update CHANGELOG.md for significant changes
- Follow [Keep a Changelog](https://keepachangelog.com/) format
- Group changes by type (Added, Changed, Fixed, etc.)

---

## Community

### Getting Help

- **GitHub Issues:** For bugs and feature requests
- **GitHub Discussions:** For questions and general discussion
- **Email:** For private inquiries

### Recognition

Contributors are recognized in:
- README.md acknowledgments
- CHANGELOG.md for significant contributions
- GitHub contributors page

---

## License

By contributing to Custom Image Classifier, you agree that your contributions will be licensed under the MIT License.

---

## Questions?

If you have any questions about contributing, please:

1. Check the [documentation](README.md)
2. Search [existing issues](https://github.com/iad1tya/custom-image-classifier/issues)
3. Open a new [discussion](https://github.com/iad1tya/custom-image-classifier/discussions)
4. Contact the maintainers

---

**Thank you for contributing! 🎉**

Your time and effort make this project better for everyone. We appreciate you!
