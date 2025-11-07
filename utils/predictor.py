import torch
import torchvision.transforms as transforms
import cv2
import numpy as np
from PIL import Image
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from models.model import ImageClassifier

def predict_image(image, model_path, class_labels):
    """
    Make a prediction on an image using a trained model.
    
    Args:
        image: OpenCV image (BGR format)
        model_path: Path to the trained model
        class_labels: List of class names
    
    Returns:
        tuple: (predicted_class, confidence_scores)
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    
    # Load model
    num_classes = len(class_labels)
    model = ImageClassifier(num_classes=num_classes).to(device)
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.eval()
    
    # Define image transformations
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_pil = Image.fromarray(image_rgb)
    
    # Transform and add batch dimension
    image_tensor = transform(image_pil).unsqueeze(0).to(device)
    
    # Make prediction
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)
        
        predicted_class = class_labels[predicted.item()]
        all_confidences = probabilities[0].cpu().numpy()
    
    return predicted_class, all_confidences
