<div align="center">

![Custom Image Classifier](custom_image_classifier.png)

# Custom Image Classifier

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.1.0-red.svg)](https://pytorch.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Train custom image classification models without writing code**

[Quick Start](#quick-start) •
[Features](#features) •
[Documentation](#documentation) •
[Contributing](#contributing)

</div>

---

## Overview

A complete framework for building custom image classification models through an intuitive web interface. Perfect for students, researchers, and developers who need fast ML prototyping.

**Key Capabilities:**
- Upload datasets and train models via web UI or CLI
- Support for any number of classes
- Automatic data augmentation and validation
- REST API for integration
- Real-time training monitoring

---

## Quick Start

```bash
# Clone and install
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run
python app.py
```

Open `http://localhost:5000` in your browser.

---

## Features

### Core Features
- **Web Interface** - Upload datasets, train models, make predictions
- **CLI Tool** - Command-line interface for automation (\`cli.py\`)
- **REST API** - Integration endpoints for training and prediction
- **GPU Support** - CUDA acceleration for faster training
- **Multiple Projects** - Manage multiple models simultaneously

### Technical Features
- Custom CNN architecture optimized for image classification
- Automatic data preprocessing and augmentation
- Real-time training progress monitoring
- Model checkpointing and versioning
- Confidence score visualization

---

## Usage

### Web Interface

1. **Create Project** - Click "New Project" and enter a name
2. **Upload Dataset** - Organize images by class folders, upload as ZIP
   \`\`\`
   my_dataset/
   ├── class1/
   │   ├── image1.jpg
   │   └── image2.jpg
   └── class2/
       └── image1.jpg
   \`\`\`
3. **Train** - Click "Train", configure parameters (epochs, batch size)
4. **Predict** - Upload test images or use webcam

### CLI

```bash
# List projects
python cli.py list

# Create project
python cli.py create my_project

# Train model
python cli.py train my_project --epochs 20
```

### API

```bash
# Train model
curl -X POST http://localhost:5000/api/train \
  -H "Content-Type: application/json" \
  -d '{"project_name": "my_project", "epochs": 10}'

# Make prediction
curl -X POST http://localhost:5000/api/predict \
  -F "project_name=my_project" \
  -F "image=@test.jpg"
```

---

## Architecture

**Stack:** Flask (backend) + PyTorch (ML) + OpenCV (vision)

**Model:** Custom CNN with 3 conv layers, max pooling, batch normalization, dropout (50%)

**Project Structure:**
```
├── app.py              # Flask application
├── cli.py              # Command-line interface
├── config.py           # Configuration
├── models/model.py     # CNN architecture
├── scripts/train_model.py
├── templates/          # Web UI
└── utils/predictor.py
```

---

## Configuration

Edit \`config.py\`:

```python
DEFAULT_EPOCHS = 10
DEFAULT_BATCH_SIZE = 32
DEFAULT_LEARNING_RATE = 0.001
IMAGE_SIZE = (128, 128)
USE_CUDA = True  # GPU acceleration
```

---

## Documentation

- **[Getting Started](GETTING_STARTED.md)** - Detailed setup guide
- **[Dataset Guide](DATASET_GUIDE.md)** - How to prepare datasets
- **[Installation](INSTALL.md)** - Platform-specific instructions
- **[Contributing](CONTRIBUTING.md)** - Development guidelines
- **[Changelog](CHANGELOG.md)** - Version history

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Setup development environment
pip install -r requirements-dev.txt
pre-commit install

# Run tests
pytest
```

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Acknowledgments

Built with [PyTorch](https://pytorch.org/), [Flask](https://flask.palletsprojects.com/), and [OpenCV](https://opencv.org/).

