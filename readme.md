# DermaVision

**DermaVision** is an advanced AI-powered web application for intelligent skin condition analysis and facial recognition. It integrates deep learning and computer vision to deliver comprehensive skin health assessments while maintaining secure, personalized user profiles through facial recognition technology.

---

## Overview

DermaVision enables users to perform automated skin assessments and track progress over time. It leverages convolutional neural networks (CNNs), transfer learning, and real-time computer vision to ensure high accuracy and efficient processing.

---

## Core Features

### Skin Analysis

* **Multi-Condition Detection**

  * Acne detection with severity classification
  * Pigmentation pattern recognition
  * Dark circle identification
  * Healthy skin verification
  * Real-time visual feedback

### Intelligent User System

* **Facial Recognition**

  * Biometric user authentication
  * Secure profile management
  * Multi-angle facial detection

### Data Analytics

* **Comprehensive Tracking**

  * Historical data storage
  * Progress and trend monitoring
  * Encrypted data handling

---

## Technical Architecture

### AI/ML Components

* **Deep Learning Models**

  * Custom CNN architecture for skin condition classification
  * Transfer learning for enhanced model accuracy
  * Real-time inference and result generation

### Backend Infrastructure

* **Framework:** Flask (Python)
* **Computer Vision:** OpenCV, Dlib
* **Deep Learning Framework:** PyTorch
* **Database:** MongoDB (NoSQL)

### Security

* Encrypted data storage and transfer
* Secure user authentication mechanisms
* Privacy-by-design implementation

---

## Project Structure

```
├── app.py              # Main application and routing
├── face_detection.py   # Facial recognition logic
├── face_utils.py       # Face processing utilities
├── skin_analysis.py    # Skin condition analysis engine
├── config.py           # Configuration settings
├── models/             # Model architectures and weights
├── database/           # Database schemas and operations
├── dataset/            # Training and validation data
│   ├── Acne/
│   ├── DarkCircles/
│   ├── HealthySkin/
│   └── Pigmentation/
├── scripts/            # Utility scripts
├── static/             # Frontend assets (CSS, JS, images)
├── templates/          # HTML templates
└── requirements.txt    # Project dependencies
```

---

## Setup Guide

### System Requirements

* Python 3.7 or higher
* MongoDB 4.0 or higher
* CUDA-compatible GPU (recommended)
* Webcam (for face recognition features)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/iad1tya/Dermavision.git
cd Dermavision
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Unix/macOS
.\venv\Scripts\activate   # Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Configure the Database

* Install and start MongoDB
* Update connection details in `config.py`

#### 5. Launch the Application

```bash
python app.py
```

Access the web interface at: [http://localhost:5000](http://localhost:5000)

---

## Testing

```bash
# Run all unit tests
python -m pytest tests/

# Run a specific test suite
python -m pytest tests/test_skin_analysis.py
```

---

## Performance Metrics

| Feature                     | Accuracy |
| --------------------------- | -------- |
| Face Detection              | ~98%     |
| Acne Detection              | ~95%     |
| Pigmentation Classification | ~93%     |
| Dark Circles Identification | ~91%     |

---

## Contributing

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature/YourFeatureName
   ```
5. Open a Pull Request

---

## Disclaimer

DermaVision is developed for **research and educational purposes only**.
It is **not intended for medical diagnosis or treatment**.
Users should consult qualified healthcare professionals for medical advice.

---

## License

This project is licensed under the **MIT License**.
Refer to the [LICENSE](LICENSE) file for details.

---

## Team

**Lead Developer:** Aditya Yadav
