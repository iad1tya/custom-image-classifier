# 🚀 Getting Started Guide

Welcome to the Custom Image Classifier! This guide will walk you through setting up and using the framework.

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 4GB+ RAM (8GB+ recommended)
- Optional: CUDA-compatible GPU for faster training

## 🔧 Installation

### 1. Clone or Download the Repository

```bash
git clone https://github.com/iad1tya/custom-image-classifier.git
cd custom-image-classifier
```

### 2. Create a Virtual Environment (Recommended)

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- PyTorch (deep learning)
- OpenCV (image processing)
- And other necessary libraries

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## 📚 Usage Tutorial

### Step 1: Create a New Project

1. Open `http://localhost:5000` in your browser
2. Click "➕ New Project"
3. Enter a project name (e.g., `dog_breeds`, `plant_classifier`)
4. Add an optional description
5. Click "Create"

### Step 2: Prepare Your Dataset

Organize your images into folders by class:

```
my_dataset/
├── class1/
│   ├── image1.jpg
│   ├── image2.jpg
│   ├── image3.jpg
│   └── ...
├── class2/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
└── class3/
    ├── image1.jpg
    └── ...
```

**Tips:**
- Use clear, descriptive folder names (these become your class labels)
- Include at least 50-100 images per class for good results
- Images should be clear and representative of the class
- Supported formats: JPG, PNG, GIF, BMP

### Step 3: Upload Your Dataset

1. Click "📤 Upload Dataset"
2. Select your project from the dropdown
3. Either:
   - **Zip your dataset folder** and upload it, OR
   - **Upload individual images** and specify the class name
4. Wait for upload to complete
5. You'll see confirmation with detected classes

### Step 4: Train Your Model

1. Go back to the home page
2. Find your project card
3. Click "Train" button
4. Training will start in the background
5. Depending on your dataset size and hardware:
   - Small datasets (<1000 images): 2-10 minutes
   - Medium datasets (1000-5000 images): 10-30 minutes
   - Large datasets (5000+ images): 30+ minutes

**Training Progress:**
- Training happens in a separate process
- Check the terminal/console for real-time progress
- You'll see epoch updates and loss/accuracy metrics

### Step 5: Make Predictions

Once training is complete:

1. Click "🔮 Make Prediction"
2. Select your trained model
3. Choose to either:
   - **Upload an image** from your computer, OR
   - **Use your webcam** to capture an image
4. Click "Predict"
5. View results with confidence scores for all classes

## 💡 Example Use Cases

### 1. Animal Classifier

```
animals/
├── dog/
├── cat/
├── bird/
└── fish/
```

### 2. Plant Disease Detector

```
plant_diseases/
├── healthy/
├── rust/
├── powdery_mildew/
└── blight/
```

### 3. Product Categorizer

```
products/
├── electronics/
├── clothing/
├── food/
└── toys/
```

### 4. Document Classifier

```
documents/
├── invoice/
├── receipt/
├── contract/
└── letter/
```

## 🎯 Best Practices

### Dataset Quality
- ✅ Use high-quality, clear images
- ✅ Include variety within each class
- ✅ Balance the number of images across classes
- ❌ Avoid blurry or corrupted images
- ❌ Don't include irrelevant images

### Training Tips
- Start with default settings (10 epochs)
- If accuracy is low, try:
  - Adding more training images
  - Increasing epochs to 20-30
  - Ensuring better class balance
- If training is too slow:
  - Reduce image count
  - Use a GPU if available
  - Reduce batch size

### Model Performance
- Test your model with new images (not from training set)
- If predictions are poor:
  - Add more diverse training images
  - Retrain with more epochs
  - Check if classes are too similar
  - Ensure training data represents real-world scenarios

## 🔄 Managing Projects

### Retrain a Model
- Click "Retrain" on any project card
- Useful after adding more training data
- Previous model will be overwritten

### Delete a Project
- Click "Delete" on the project card
- This removes all data and models (cannot be undone!)
- Use with caution

## 🐛 Troubleshooting

### "Import Error" when starting
```bash
# Make sure you're in the virtual environment
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### "CUDA out of memory"
```bash
# Reduce batch size in training
# Edit scripts/train_model.py, reduce DEFAULT_BATCH_SIZE
```

### "Model not found" error
- Ensure training completed successfully
- Check terminal for training errors
- Retrain the project

### Slow training
- GPU not detected: Check PyTorch CUDA installation
- Use smaller images: Images are resized to 128x128 automatically
- Reduce epochs: Start with 5-10 epochs for testing

## 📊 Understanding Results

### Confidence Score
- **80-100%**: Very confident prediction
- **60-80%**: Confident prediction
- **40-60%**: Uncertain prediction
- **<40%**: Low confidence (model unsure)

### Training Metrics
- **Loss**: Lower is better (measures error)
- **Accuracy**: Higher is better (percentage correct)
- Expect improvement over epochs

## 🚀 Advanced Usage

### Custom Training Parameters
Edit `scripts/train_model.py` to adjust:
- Number of epochs
- Learning rate
- Batch size
- Image size
- Data augmentation settings

### API Integration
Use the REST API to integrate with other applications:

```python
import requests

# Make prediction
files = {'image': open('test.jpg', 'rb')}
data = {'project_name': 'my_project'}
response = requests.post('http://localhost:5000/api/predict', files=files, data=data)
print(response.json())
```

## 📧 Need Help?

- Check the main README.md for more details
- Open an issue on GitHub
- Review the code comments for technical details

---

**Ready to classify? Start with your first project now!** 🎉
