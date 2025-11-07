# Application Configuration

# Flask settings
DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

# File upload settings
MAX_UPLOAD_SIZE = 500 * 1024 * 1024  # 500MB
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'zip'}

# Directory settings
UPLOAD_FOLDER = 'datasets'
MODEL_FOLDER = 'models'
PROJECT_FOLDER = 'projects'

# Model training defaults
DEFAULT_EPOCHS = 10
DEFAULT_BATCH_SIZE = 32
DEFAULT_LEARNING_RATE = 0.001
IMAGE_SIZE = (128, 128)

# Model architecture settings
DROPOUT_RATE = 0.5
USE_BATCH_NORM = True

# Data augmentation settings
RANDOM_HORIZONTAL_FLIP = True
RANDOM_ROTATION = 10  # degrees
COLOR_JITTER = {
    'brightness': 0.2,
    'contrast': 0.2,
    'saturation': 0.2
}

# Database settings (optional - for tracking history)
USE_DATABASE = False
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = 'image_classifier'

# GPU settings
USE_CUDA = True  # Set to False to force CPU

# Advanced settings
EARLY_STOPPING = False
EARLY_STOPPING_PATIENCE = 5
SAVE_BEST_MODEL = True

# Logging
ENABLE_LOGGING = True
LOG_LEVEL = 'INFO'
