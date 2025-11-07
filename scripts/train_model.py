import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader
import os
import json
import argparse
from pathlib import Path
import sys

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from models.model import ImageClassifier

def train_model(project_name, epochs=10, batch_size=32, learning_rate=0.001):
    """Train a custom image classification model"""
    
    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    
    # Project paths
    project_dir = os.path.join('projects', project_name)
    dataset_dir = os.path.join(project_dir, 'dataset')
    model_dir = os.path.join(project_dir, 'models')
    config_path = os.path.join(project_dir, 'config.json')
    
    # Load project config
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    print(f"\n{'='*60}")
    print(f"Training Project: {project_name}")
    print(f"{'='*60}\n")
    
    # Define image transformations
    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
    ])
    
    # Load dataset
    print(f"Loading dataset from: {dataset_dir}")
    try:
        train_data = datasets.ImageFolder(root=dataset_dir, transform=transform)
        train_loader = DataLoader(dataset=train_data, batch_size=batch_size, shuffle=True)
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return False
    
    # Get class names
    class_labels = train_data.classes
    num_classes = len(class_labels)
    print(f"\nClasses found: {class_labels}")
    print(f"Number of classes: {num_classes}")
    print(f"Total training images: {len(train_data)}\n")
    
    # Update config with class info
    config['classes'] = class_labels
    config['num_classes'] = num_classes
    
    # Initialize model
    model = ImageClassifier(num_classes=num_classes).to(device)
    
    # Define loss function & optimizer
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    
    # Training loop
    print(f"Starting training for {epochs} epochs...\n")
    training_history = []
    
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        
        for i, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)
            
            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)
            
            # Backward pass
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            # Statistics
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            
            # Print progress every 10 batches
            if (i + 1) % 10 == 0:
                print(f"Epoch [{epoch+1}/{epochs}], Batch [{i+1}/{len(train_loader)}], "
                      f"Loss: {loss.item():.4f}")
        
        # Epoch statistics
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        
        print(f"\n{'='*60}")
        print(f"Epoch [{epoch+1}/{epochs}] Summary:")
        print(f"Average Loss: {epoch_loss:.4f}")
        print(f"Training Accuracy: {epoch_acc:.2f}%")
        print(f"{'='*60}\n")
        
        # Save epoch stats
        training_history.append({
            'epoch': epoch + 1,
            'loss': epoch_loss,
            'accuracy': epoch_acc
        })
    
    # Save model
    model_path = os.path.join(model_dir, 'model.pth')
    torch.save(model.state_dict(), model_path)
    print(f"\n✅ Model saved to: {model_path}")
    
    # Save class labels
    labels_path = os.path.join(model_dir, 'class_labels.json')
    with open(labels_path, 'w') as f:
        json.dump(class_labels, f, indent=2)
    print(f"✅ Class labels saved to: {labels_path}")
    
    # Update config
    config['trained'] = True
    config['model_path'] = model_path
    config['training_history'] = training_history
    config['training_params'] = {
        'epochs': epochs,
        'batch_size': batch_size,
        'learning_rate': learning_rate
    }
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"\n{'='*60}")
    print(f"✅ Training Complete!")
    print(f"{'='*60}\n")
    
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Train a custom image classifier')
    parser.add_argument('--project', type=str, required=True, help='Project name')
    parser.add_argument('--epochs', type=int, default=10, help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=32, help='Batch size')
    parser.add_argument('--learning_rate', type=float, default=0.001, help='Learning rate')
    
    args = parser.parse_args()
    
    success = train_model(
        project_name=args.project,
        epochs=args.epochs,
        batch_size=args.batch_size,
        learning_rate=args.learning_rate
    )
    
    sys.exit(0 if success else 1)
