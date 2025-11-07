"""
Example script demonstrating how to use the Custom Image Classifier programmatically.
This shows how to interact with the API without using the web interface.
"""

import requests
import json
import os
from pathlib import Path

# Configuration
BASE_URL = "http://localhost:5000"
API_URL = f"{BASE_URL}/api"

def create_project(name, description=""):
    """Create a new project"""
    url = f"{API_URL}/create_project"
    data = {
        "name": name,
        "description": description
    }
    response = requests.post(url, json=data)
    return response.json()

def upload_dataset(project_name, zip_file_path):
    """Upload a dataset zip file to a project"""
    url = f"{API_URL}/upload_dataset"
    
    with open(zip_file_path, 'rb') as f:
        files = {'file': f}
        data = {'project_name': project_name}
        response = requests.post(url, files=files, data=data)
    
    return response.json()

def train_model(project_name, epochs=10, batch_size=32, learning_rate=0.001):
    """Start training a model"""
    url = f"{API_URL}/train"
    data = {
        "project_name": project_name,
        "epochs": epochs,
        "batch_size": batch_size,
        "learning_rate": learning_rate
    }
    response = requests.post(url, json=data)
    return response.json()

def make_prediction(project_name, image_path):
    """Make a prediction on an image"""
    url = f"{API_URL}/predict"
    
    with open(image_path, 'rb') as f:
        files = {'image': f}
        data = {'project_name': project_name}
        response = requests.post(url, files=files, data=data)
    
    return response.json()

def list_projects():
    """Get all projects"""
    url = f"{API_URL}/projects"
    response = requests.get(url)
    return response.json()

def get_project(project_name):
    """Get details of a specific project"""
    url = f"{API_URL}/projects/{project_name}"
    response = requests.get(url)
    return response.json()

def delete_project(project_name):
    """Delete a project"""
    url = f"{API_URL}/delete_project/{project_name}"
    response = requests.delete(url)
    return response.json()

# Example usage
if __name__ == "__main__":
    print("🚀 Custom Image Classifier - API Example\n")
    
    # Example 1: Create a new project
    print("1. Creating a new project...")
    result = create_project(
        name="example_classifier",
        description="Example project for testing"
    )
    print(f"   Result: {json.dumps(result, indent=2)}\n")
    
    # Example 2: List all projects
    print("2. Listing all projects...")
    projects = list_projects()
    print(f"   Found {len(projects)} project(s)")
    for project in projects:
        print(f"   - {project['name']} ({project['num_classes']} classes)")
    print()
    
    # Example 3: Upload dataset (uncomment and provide path)
    # print("3. Uploading dataset...")
    # result = upload_dataset("example_classifier", "path/to/dataset.zip")
    # print(f"   Result: {json.dumps(result, indent=2)}\n")
    
    # Example 4: Train model (uncomment after uploading dataset)
    # print("4. Starting training...")
    # result = train_model("example_classifier", epochs=5)
    # print(f"   Result: {json.dumps(result, indent=2)}\n")
    
    # Example 5: Make prediction (uncomment after training)
    # print("5. Making prediction...")
    # result = make_prediction("example_classifier", "path/to/test_image.jpg")
    # print(f"   Prediction: {result['prediction']}")
    # print(f"   Confidence: {result['confidence']*100:.2f}%")
    # print(f"   All probabilities:")
    # for class_name, prob in result['all_probabilities'].items():
    #     print(f"      {class_name}: {prob*100:.2f}%")
    # print()
    
    # Example 6: Get project details
    # print("6. Getting project details...")
    # project = get_project("example_classifier")
    # print(f"   Result: {json.dumps(project, indent=2)}\n")
    
    # Example 7: Delete project (uncomment with caution!)
    # print("7. Deleting project...")
    # result = delete_project("example_classifier")
    # print(f"   Result: {json.dumps(result, indent=2)}\n")
    
    print("✅ Done! Uncomment the examples above to test each feature.")
