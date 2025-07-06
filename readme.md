# DermaVision 🔬

An advanced AI-powered web application for skin condition analysis and face recognition. DermaVision leverages deep learning to analyze various skin conditions and maintains user profiles through facial recognition.

## 🌟 Key Features

- **Skin Condition Analysis**
  - Acne detection and severity assessment
  - Pigmentation analysis
  - Dark circles detection
  - Healthy skin verification

- **Smart User Management**
  - Facial recognition for user identification
  - Secure user profiles
  - Historical analysis tracking

- **Data Management**
  - Persistent storage of analysis results
  - User history tracking
  - Secure data handling

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.7 or higher
- MongoDB installed and running
- Webcam access (for face recognition)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/iad1tya/Dermavision
   cd Dermavision
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure MongoDB is running on your system

4. Launch the application:
   ```bash
   python app.py
   ```

5. Access the web interface at `http://localhost:5000`

## 💻 Technology Stack

### Backend
- **Flask**: Python web framework for robust backend services
- **PyTorch**: Deep learning framework for skin condition analysis
- **OpenCV & Dlib**: Advanced face detection and recognition

### Database
- **MongoDB**: NoSQL database for flexible data storage

### AI/ML
- Custom trained models for skin condition analysis
- Face recognition algorithms for user identification

## 📁 Project Structure

```
├── app.py              # Main application entry point
├── face_detection.py   # Face detection utilities
├── skin_analysis.py    # Skin condition analysis logic
├── models/            # AI model files
├── templates/         # HTML templates
├── static/           # Static assets
└── database/         # Database operations
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## ⚠️ Disclaimer

**Important Notice**: DermaVision is an academic project developed for educational purposes. It is not intended for medical diagnosis or treatment. Always consult qualified healthcare professionals for medical advice.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Aditya Yadav

---

*This project was developed as part of an academic curriculum and serves as a demonstration of AI applications in healthcare technology.*
