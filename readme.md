# DermaVision 🔬

An advanced AI-powered web application for intelligent skin condition analysis and facial recognition. DermaVision combines state-of-the-art deep learning models with computer vision to provide comprehensive skin health analysis while maintaining personalized user profiles through facial recognition technology.

## 🎯 Core Features

### 🔍 Skin Analysis Capabilities
- **Multi-Condition Detection**
  - Acne analysis with severity classification
  - Pigmentation pattern recognition
  - Dark circles identification
  - Healthy skin verification
  - Real-time analysis feedback

### 👤 Intelligent User System
- **Advanced Face Recognition**
  - Biometric user identification
  - Secure profile management
  - Multi-angle face detection

### 📊 Data Analytics
- **Comprehensive Tracking**
  - Historical analysis storage
  - Progress monitoring
  - Trend analysis
  - Secure data encryption

## 🛠️ Technical Architecture

### AI/ML Components
- **Deep Learning Models**
  - Custom CNN architecture for skin condition classification
  - Transfer learning implementation for enhanced accuracy
  - Real-time processing capabilities

### Backend Infrastructure
- **Framework**: Flask (Python)
- **Computer Vision**: OpenCV & Dlib
- **Deep Learning**: PyTorch
- **Database**: MongoDB (NoSQL)

### Security Features
- Encrypted data storage
- Secure user authentication
- Privacy-focused design

## 📦 Project Structure

```
├── app.py              # Application entry point & routing
├── face_detection.py   # Facial recognition implementation
├── face_utils.py       # Face processing utilities
├── skin_analysis.py    # Skin condition analysis engine
├── config.py           # Configuration settings
├── models/             # AI model architectures and weights
├── database/           # Database operations & schemas
├── dataset/            # Training and validation datasets
│   ├── Acne/          # Acne condition images
│   ├── DarkCircles/    # Dark circles dataset
│   ├── HealthySkin/    # Normal skin samples
│   └── Pigmentation/   # Pigmentation cases
├── scripts/            # Utility scripts
├── static/             # Frontend assets
├── templates/          # HTML views
└── requirements.txt    # Project dependencies
```

## 🚀 Setup Guide

### System Requirements
- Python 3.7+
- MongoDB 4.0+
- CUDA-compatible GPU (recommended)
- Webcam for face recognition

### Installation Steps

1. **Clone Repository**
   ```bash
   git clone https://github.com/iad1tya/Dermavision.git
   cd Dermavision
   ```

2. **Create Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Unix/macOS
   .\venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   - Install MongoDB
   - Start MongoDB service
   - Configure connection in `config.py`

5. **Launch Application**
   ```bash
   python app.py
   ```

6. Access the web interface at `http://localhost:5000`

## 🧪 Testing

```bash
# Run unit tests
python -m pytest tests/

# Run specific test suite
python -m pytest tests/test_skin_analysis.py
```

## 📈 Performance Metrics

- Face Detection Accuracy: ~98%
- Skin Condition Classification:
  - Acne Detection: ~95%
  - Pigmentation: ~93%
  - Dark Circles: ~91%

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## ⚠️ Disclaimer

**Important Notice**: DermaVision is an academic project developed for research and educational purposes. It is not intended for medical diagnosis or treatment. Always consult qualified healthcare professionals for medical advice.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- **Lead Developer**: Aditya Yadav

## 📚 Documentation

For detailed documentation, API references, and development guides, visit our [Wiki](https://github.com/iad1tya/Dermavision/wiki).

---

*DermaVision - Advancing skin health analysis through artificial intelligence*
