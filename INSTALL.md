# Installation Guide

This guide provides detailed instructions for installing Custom Image Classifier on various platforms.

## Table of Contents

- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [GPU Setup](#gpu-setup)
- [Troubleshooting](#troubleshooting)
- [Verification](#verification)

---

## System Requirements

### Minimum Requirements

- **OS:** Windows 10+, macOS 10.15+, or Linux (Ubuntu 20.04+)
- **Python:** 3.8 or higher
- **RAM:** 4GB
- **Disk Space:** 2GB free space
- **Internet:** Required for installation

### Recommended Requirements

- **OS:** Windows 11, macOS 13+, or Linux (Ubuntu 22.04+)
- **Python:** 3.10 or higher
- **RAM:** 8GB or more
- **Disk Space:** 10GB free space
- **GPU:** NVIDIA GPU with CUDA support (for faster training)
- **Internet:** Required for installation

---

## Installation Methods

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier

# Run the installation script (coming soon)
./install.sh
```

### Method 2: Manual Install

```bash
# Clone the repository
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### Method 3: Docker (Coming Soon)

```bash
docker pull iad1tya/custom-image-classifier:latest
docker run -p 5000:5000 iad1tya/custom-image-classifier
```

---

## Platform-Specific Instructions

### macOS

#### Prerequisites

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11

# Verify installation
python3 --version
```

#### Installation

```bash
# Clone repository
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### Troubleshooting macOS

**Issue: "command not found: python"**
```bash
# Use python3 instead
python3 -m venv venv
```

**Issue: SSL certificate error**
```bash
# Install certificates
/Applications/Python\ 3.11/Install\ Certificates.command
```

### Linux (Ubuntu/Debian)

#### Prerequisites

```bash
# Update package list
sudo apt update

# Install Python and pip
sudo apt install python3 python3-pip python3-venv

# Install system dependencies
sudo apt install build-essential libssl-dev libffi-dev python3-dev

# Verify installation
python3 --version
```

#### Installation

```bash
# Clone repository
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### Troubleshooting Linux

**Issue: "ModuleNotFoundError: No module named '_tkinter'"**
```bash
sudo apt install python3-tk
```

**Issue: Permission denied**
```bash
chmod +x install.sh
```

### Windows

#### Prerequisites

1. **Install Python:**
   - Download from [python.org](https://www.python.org/downloads/)
   - Check "Add Python to PATH" during installation
   - Verify: Open CMD and run `python --version`

2. **Install Git:**
   - Download from [git-scm.com](https://git-scm.com/download/win)
   - Use default settings

#### Installation

```cmd
REM Clone repository
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
venv\Scripts\activate

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
pip install -r requirements.txt

REM Run the application
python app.py
```

#### Troubleshooting Windows

**Issue: "python is not recognized"**
- Add Python to PATH manually
- Settings → System → Advanced → Environment Variables
- Add Python installation directory

**Issue: Long path errors**
```cmd
REM Enable long paths in Windows
reg add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

---

## GPU Setup

### NVIDIA GPU (CUDA)

#### Check GPU Compatibility

```bash
# Check if NVIDIA GPU is available
nvidia-smi
```

#### Install CUDA Toolkit

**Linux:**
```bash
# Add NVIDIA package repositories
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.0-1_all.deb
sudo dpkg -i cuda-keyring_1.0-1_all.deb
sudo apt-get update

# Install CUDA
sudo apt-get install cuda
```

**Windows:**
- Download CUDA Toolkit from [NVIDIA](https://developer.nvidia.com/cuda-downloads)
- Follow installer instructions

#### Install PyTorch with CUDA

```bash
# CUDA 11.8
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
```

#### Verify GPU Installation

```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU: {torch.cuda.get_device_name(0)}")
```

### AMD GPU (ROCm) - Linux Only

```bash
# Install ROCm
wget https://repo.radeon.com/amdgpu-install/latest/ubuntu/focal/amdgpu-install_21.50.50000-1_all.deb
sudo apt-get install ./amdgpu-install_21.50.50000-1_all.deb
sudo amdgpu-install --usecase=rocm

# Install PyTorch for ROCm
pip install torch torchvision --index-url https://download.pytorch.org/whl/rocm5.4.2
```

### Apple Silicon (M1/M2/M3)

PyTorch automatically uses Metal Performance Shaders (MPS):

```bash
# Standard installation
pip install torch torchvision

# Verify MPS
python -c "import torch; print(f'MPS available: {torch.backends.mps.is_available()}')"
```

---

## Troubleshooting

### Common Issues

#### 1. Import Errors

**Error:** `ModuleNotFoundError: No module named 'torch'`

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install PyTorch
pip install torch torchvision
```

#### 2. Memory Errors

**Error:** `RuntimeError: CUDA out of memory`

**Solution:**
```python
# Reduce batch size in config.py
DEFAULT_BATCH_SIZE = 16  # or 8
```

#### 3. Port Already in Use

**Error:** `OSError: [Errno 48] Address already in use`

**Solution:**
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9  # macOS/Linux

# Or use a different port
python app.py --port 5001
```

#### 4. OpenCV Errors

**Error:** `ImportError: libGL.so.1: cannot open shared object file`

**Solution (Linux):**
```bash
sudo apt install libgl1-mesa-glx
```

#### 5. Permission Errors

**Error:** `PermissionError: [Errno 13] Permission denied`

**Solution:**
```bash
# Don't use sudo with pip in virtual environment
# Make sure you own the directory
sudo chown -R $USER:$USER ~/custom-image-classifier
```

### Getting Help

If you encounter issues:

1. Check [existing issues](https://github.com/iad1tya/custom-image-classifier/issues)
2. Search [discussions](https://github.com/iad1tya/custom-image-classifier/discussions)
3. Create a new issue with:
   - Your OS and version
   - Python version
   - Full error message
   - Steps to reproduce

---

## Verification

### Verify Installation

```bash
# Activate virtual environment
source venv/bin/activate

# Check Python version
python --version

# Check installed packages
pip list | grep -E "torch|flask|opencv"

# Run test script
python -c "
import torch
import flask
import cv2
print('✓ All dependencies installed successfully!')
print(f'PyTorch: {torch.__version__}')
print(f'Flask: {flask.__version__}')
print(f'OpenCV: {cv2.__version__}')
print(f'CUDA: {torch.cuda.is_available()}')
"
```

### Run Application

```bash
# Start the application
python app.py

# Expected output:
# * Running on http://127.0.0.1:5000
# * Press CTRL+C to quit
```

### Test CLI

```bash
# Test CLI
python cli.py list

# Expected output:
# No projects found. Create one first!
```

---

## Next Steps

After successful installation:

1. Read [Getting Started Guide](GETTING_STARTED.md)
2. Follow [Dataset Guide](DATASET_GUIDE.md) to prepare your data
3. Create your first project
4. Train your first model

---

## Updating

### Update to Latest Version

```bash
# Pull latest changes
git pull origin main

# Update dependencies
pip install --upgrade -r requirements.txt
```

### Check for Updates

```bash
# Check current version
python -c "from app import __version__; print(__version__)"

# Check for updates
git fetch
git status
```

---

**Happy Installing! 🚀**

If you need help, check our [troubleshooting guide](#troubleshooting) or [open an issue](https://github.com/iad1tya/custom-image-classifier/issues).
