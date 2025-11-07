import torch
import torch.nn as nn
import torch.nn.functional as F

# Define CNN model architecture for image classification
class ImageClassifier(nn.Module):
    """
    Flexible CNN architecture for custom image classification.
    Works with any number of classes.
    """
    def __init__(self, num_classes=2):
        super(ImageClassifier, self).__init__()

        # Convolutional layers
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.conv2 = nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.conv3 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1)

        # Pooling layer
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

        # Batch normalization layers
        self.bn1 = nn.BatchNorm2d(32)
        self.bn2 = nn.BatchNorm2d(64)
        self.bn3 = nn.BatchNorm2d(128)

        # Fully connected layers (dynamically adjusted)
        self.fc1 = nn.Linear(128 * 16 * 16, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, num_classes)
        
        # Dropout for regularization
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        # Convolutional layers with batch norm and pooling
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = self.pool(F.relu(self.bn2(self.conv2(x))))
        x = self.pool(F.relu(self.bn3(self.conv3(x))))

        # Flatten before passing to FC layers
        x = x.view(x.size(0), -1)
        
        # Fully connected layers with dropout
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)

        return x

def load_model(model_path, num_classes):
    """
    Load a trained model from disk.
    
    Args:
        model_path: Path to the saved model weights
        num_classes: Number of output classes
    
    Returns:
        Loaded model in evaluation mode
    """
    model = ImageClassifier(num_classes=num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

def create_model(num_classes):
    """
    Create a new untrained model.
    
    Args:
        num_classes: Number of output classes
    
    Returns:
        New model instance
    """
    return ImageClassifier(num_classes=num_classes)
