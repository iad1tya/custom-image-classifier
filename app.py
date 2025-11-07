from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import json
import cv2
import numpy as np
import base64
from werkzeug.utils import secure_filename
import zipfile
from datetime import datetime
from pathlib import Path
import shutil

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max upload
app.config['UPLOAD_FOLDER'] = 'datasets'
app.config['MODEL_FOLDER'] = 'models'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'zip'}

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['MODEL_FOLDER'], exist_ok=True)
os.makedirs('projects', exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_projects():
    """Get list of all projects"""
    projects = []
    if os.path.exists('projects'):
        for project_dir in os.listdir('projects'):
            project_path = os.path.join('projects', project_dir)
            if os.path.isdir(project_path):
                config_file = os.path.join(project_path, 'config.json')
                if os.path.exists(config_file):
                    with open(config_file, 'r') as f:
                        projects.append(json.load(f))
    return projects

@app.route('/')
def home():
    """Main landing page"""
    projects = get_projects()
    return render_template('index.html', projects=projects)

@app.route('/upload')
def upload_page():
    """Dataset upload page"""
    return render_template('upload.html')

@app.route('/predict')
def predict_page():
    """Prediction interface"""
    projects = get_projects()
    return render_template('predict.html', projects=projects)

@app.route('/api/projects', methods=['GET'])
def list_projects():
    """API: List all projects"""
    return jsonify(get_projects())

@app.route('/api/projects/<project_name>', methods=['GET'])
def get_project(project_name):
    """API: Get project details"""
    project_path = os.path.join('projects', project_name, 'config.json')
    if os.path.exists(project_path):
        with open(project_path, 'r') as f:
            return jsonify(json.load(f))
    return jsonify({"error": "Project not found"}), 404

@app.route('/api/create_project', methods=['POST'])
def create_project():
    """API: Create a new project"""
    data = request.json
    project_name = secure_filename(data.get('name', '').strip())
    
    if not project_name:
        return jsonify({"error": "Project name is required"}), 400
    
    project_dir = os.path.join('projects', project_name)
    if os.path.exists(project_dir):
        return jsonify({"error": "Project already exists"}), 400
    
    # Create project structure
    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'dataset'), exist_ok=True)
    os.makedirs(os.path.join(project_dir, 'models'), exist_ok=True)
    
    # Create project config
    config = {
        "name": project_name,
        "description": data.get('description', ''),
        "created_at": datetime.now().isoformat(),
        "num_classes": 0,
        "classes": [],
        "trained": False,
        "model_path": None,
        "training_history": []
    }
    
    with open(os.path.join(project_dir, 'config.json'), 'w') as f:
        json.dump(config, f, indent=2)
    
    return jsonify({"success": True, "project": config})

@app.route('/api/upload_dataset', methods=['POST'])
def upload_dataset():
    """API: Upload dataset for a project"""
    project_name = request.form.get('project_name')
    if not project_name:
        return jsonify({"error": "Project name is required"}), 400
    
    project_dir = os.path.join('projects', project_name)
    if not os.path.exists(project_dir):
        return jsonify({"error": "Project not found"}), 404
    
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400
    
    dataset_dir = os.path.join(project_dir, 'dataset')
    
    # Handle zip file upload
    if file.filename.endswith('.zip'):
        zip_path = os.path.join(project_dir, 'temp.zip')
        file.save(zip_path)
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(dataset_dir)
            os.remove(zip_path)
        except Exception as e:
            return jsonify({"error": f"Failed to extract zip: {str(e)}"}), 400
    else:
        # Handle individual image upload
        class_name = request.form.get('class_name', 'default')
        class_dir = os.path.join(dataset_dir, class_name)
        os.makedirs(class_dir, exist_ok=True)
        
        filename = secure_filename(file.filename)
        file.save(os.path.join(class_dir, filename))
    
    # Update project config with classes
    classes = [d for d in os.listdir(dataset_dir) 
               if os.path.isdir(os.path.join(dataset_dir, d)) and not d.startswith('.')]
    
    config_path = os.path.join(project_dir, 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    config['classes'] = sorted(classes)
    config['num_classes'] = len(classes)
    
    # Count images per class
    class_counts = {}
    for class_name in classes:
        class_path = os.path.join(dataset_dir, class_name)
        count = len([f for f in os.listdir(class_path) 
                    if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))])
        class_counts[class_name] = count
    
    config['class_counts'] = class_counts
    
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    return jsonify({"success": True, "classes": classes, "class_counts": class_counts})

@app.route('/api/train', methods=['POST'])
def train_model():
    """API: Train a model for a project"""
    data = request.json
    project_name = data.get('project_name')
    
    if not project_name:
        return jsonify({"error": "Project name is required"}), 400
    
    project_dir = os.path.join('projects', project_name)
    if not os.path.exists(project_dir):
        return jsonify({"error": "Project not found"}), 404
    
    # Get training parameters
    epochs = int(data.get('epochs', 10))
    batch_size = int(data.get('batch_size', 32))
    learning_rate = float(data.get('learning_rate', 0.001))
    
    # Import training script
    import subprocess
    import sys
    
    # Run training in subprocess
    cmd = [
        sys.executable,
        'scripts/train_model.py',
        '--project', project_name,
        '--epochs', str(epochs),
        '--batch_size', str(batch_size),
        '--learning_rate', str(learning_rate)
    ]
    
    try:
        # Start training in background
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return jsonify({
            "success": True,
            "message": "Training started",
            "process_id": process.pid
        })
    except Exception as e:
        return jsonify({"error": f"Failed to start training: {str(e)}"}), 500

@app.route('/api/predict', methods=['POST'])
def predict():
    """API: Make prediction using trained model"""
    project_name = request.form.get('project_name')
    
    if not project_name:
        return jsonify({"error": "Project name is required"}), 400
    
    project_dir = os.path.join('projects', project_name)
    config_path = os.path.join(project_dir, 'config.json')
    
    if not os.path.exists(config_path):
        return jsonify({"error": "Project not found"}), 404
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    if not config.get('trained'):
        return jsonify({"error": "Model not trained yet"}), 400
    
    # Get image from request
    if 'image' in request.files:
        file = request.files['image']
        image_bytes = file.read()
        np_arr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    elif 'image_data' in request.form:
        # Base64 encoded image
        image_data = request.form['image_data']
        image_decoded = base64.b64decode(image_data.split(',')[1])
        np_arr = np.frombuffer(image_decoded, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    else:
        return jsonify({"error": "No image provided"}), 400
    
    # Load model and make prediction
    from utils.predictor import predict_image
    
    model_path = os.path.join(project_dir, 'models', 'model.pth')
    class_labels = config['classes']
    
    try:
        prediction, confidence = predict_image(img, model_path, class_labels)
        
        return jsonify({
            "prediction": prediction,
            "confidence": float(confidence),
            "all_probabilities": {class_name: float(prob) 
                                 for class_name, prob in zip(class_labels, confidence)}
        })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500

@app.route('/api/delete_project/<project_name>', methods=['DELETE'])
def delete_project(project_name):
    """API: Delete a project"""
    project_dir = os.path.join('projects', project_name)
    
    if not os.path.exists(project_dir):
        return jsonify({"error": "Project not found"}), 404
    
    try:
        shutil.rmtree(project_dir)
        return jsonify({"success": True, "message": "Project deleted"})
    except Exception as e:
        return jsonify({"error": f"Failed to delete project: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)