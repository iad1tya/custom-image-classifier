# Changelog

All notable changes to the Custom Image Classifier project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Transfer learning with pre-trained models (ResNet, VGG, etc.)
- Model ensemble support
- Advanced data augmentation options
- Model interpretability with Grad-CAM
- Experiment tracking with MLflow
- Docker containerization
- Mobile app for predictions

---

## [1.0.0] - 2025-11-07

### Added

- Initial release of Custom Image Classifier
- Web-based interface for model training and predictions
- Command-line interface (CLI) for project management
- RESTful API for integration
- Support for custom image datasets
- CNN model architecture with configurable hyperparameters
- Project-based organization system
- Multiple project support
- Real-time training progress monitoring
- GPU acceleration support (CUDA)
- Data augmentation pipeline
- Webcam integration for predictions
- ZIP file upload support
- Individual image upload support
- Confidence score visualization
- Training history tracking
- Dataset statistics and class distribution
- Model checkpointing
- Comprehensive documentation (README, GETTING_STARTED, DATASET_GUIDE)

### Features

#### Web Interface
- Project creation and management
- Dataset upload (ZIP and individual files)
- Model training with configurable parameters
- Real-time prediction interface
- Webcam capture support
- Project deletion

#### CLI Tool
- `list` - List all projects
- `info` - Show project details
- `create` - Create new project
- `train` - Train project model

#### API Endpoints
- `POST /api/create_project` - Create a new project
- `POST /api/upload_dataset` - Upload dataset
- `POST /api/train` - Start model training
- `POST /api/predict` - Make predictions
- `GET /api/projects` - List all projects
- `GET /api/projects/<name>` - Get project details
- `DELETE /api/delete_project/<name>` - Delete project

#### Model Features
- Custom CNN architecture
- 3 convolutional layers with ReLU activation
- MaxPooling for spatial reduction
- Batch normalization
- Dropout regularization (50%)
- Fully connected layers
- Softmax output for classification
- Adam optimizer
- Cross-entropy loss

#### Data Processing
- Automatic image resizing (128×128)
- Random horizontal flips
- Random rotations (±10°)
- Color jittering (brightness, contrast, saturation)
- Normalization
- Train/validation split

### Configuration

- Configurable epochs (default: 10)
- Configurable batch size (default: 32)
- Configurable learning rate (default: 0.001)
- Configurable image size (default: 128×128)
- Configurable dropout rate (default: 0.5)
- Optional MongoDB integration for history tracking

### Documentation

- Comprehensive README with badges and examples
- Getting Started guide with step-by-step instructions
- Dataset preparation guide with examples
- API documentation with curl examples
- Contributing guidelines
- MIT License
- Code of Conduct

### Dependencies

- Flask 3.0.0 - Web framework
- PyTorch 2.1.0 - Deep learning
- torchvision 0.16.0 - Computer vision utilities
- OpenCV 4.8.1.78 - Image processing
- Pillow 10.1.0 - Image handling
- NumPy 1.26.2 - Numerical computing
- Werkzeug 3.0.1 - WSGI utilities
- requests 2.31.0 - HTTP library
- pymongo 4.6.0 - MongoDB driver (optional)

---

## [0.9.0] - 2025-10-15

### Added

- Beta release for testing
- Core functionality implementation
- Basic web interface
- Model training pipeline
- Prediction interface

### Known Issues

- No CLI support
- Limited documentation
- No API documentation
- No error handling for edge cases

---

## [0.5.0] - 2025-09-01

### Added

- Alpha release
- Proof of concept
- Basic CNN model
- Flask application skeleton
- Simple file upload

### Known Issues

- No project management
- Single model only
- No web interface
- Command-line only

---

## Version History Summary

| Version | Release Date | Status | Highlights |
|---------|-------------|---------|-----------|
| 1.0.0 | 2025-11-07 | Stable | Full release with web UI, CLI, API |
| 0.9.0 | 2025-10-15 | Beta | Testing phase |
| 0.5.0 | 2025-09-01 | Alpha | Initial proof of concept |

---

## Migration Guides

### Upgrading from 0.9.0 to 1.0.0

No breaking changes. All 0.9.0 projects are compatible with 1.0.0.

**New features available:**
- CLI tool (`cli.py`)
- API endpoints
- Enhanced documentation
- Better error handling

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for information on how to contribute to this project.

---

## Links

- [Repository](https://github.com/iad1tya/custom-image-classifier)
- [Issues](https://github.com/iad1tya/custom-image-classifier/issues)
- [Discussions](https://github.com/iad1tya/custom-image-classifier/discussions)
- [Releases](https://github.com/iad1tya/custom-image-classifier/releases)

---

**Legend:**
- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Vulnerability fixes

---

*This changelog is maintained by the Custom Image Classifier team.*
