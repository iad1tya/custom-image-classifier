#!/usr/bin/env python3
"""
Command-line interface for Custom Image Classifier
Quick tool for managing projects without using the web interface
"""

import argparse
import json
import os
import sys
from pathlib import Path

def list_projects():
    """List all projects"""
    projects_dir = Path('projects')
    if not projects_dir.exists():
        print("No projects found. Create one first!")
        return
    
    projects = []
    for project_dir in projects_dir.iterdir():
        if project_dir.is_dir():
            config_file = project_dir / 'config.json'
            if config_file.exists():
                with open(config_file, 'r') as f:
                    config = json.load(f)
                    projects.append(config)
    
    if not projects:
        print("No projects found. Create one first!")
        return
    
    print(f"\n{'='*70}")
    print(f"{'PROJECT NAME':<25} {'CLASSES':<10} {'STATUS':<15} {'CREATED'}")
    print(f"{'='*70}")
    
    for project in projects:
        name = project['name']
        num_classes = project.get('num_classes', 0)
        status = '✓ Trained' if project.get('trained') else '⏳ Untrained'
        created = project.get('created_at', 'N/A')[:10]
        
        print(f"{name:<25} {num_classes:<10} {status:<15} {created}")
    
    print(f"{'='*70}\n")

def show_project_info(project_name):
    """Show detailed information about a project"""
    config_file = Path('projects') / project_name / 'config.json'
    
    if not config_file.exists():
        print(f"Error: Project '{project_name}' not found!")
        return
    
    with open(config_file, 'r') as f:
        config = json.load(f)
    
    print(f"\n{'='*70}")
    print(f"Project: {config['name']}")
    print(f"{'='*70}")
    print(f"Description: {config.get('description', 'N/A')}")
    print(f"Created: {config.get('created_at', 'N/A')}")
    print(f"Status: {'✓ Trained' if config.get('trained') else '⏳ Not trained'}")
    print(f"Number of classes: {config.get('num_classes', 0)}")
    
    if config.get('classes'):
        print(f"\nClasses:")
        for i, class_name in enumerate(config['classes'], 1):
            count = config.get('class_counts', {}).get(class_name, 0)
            print(f"  {i}. {class_name} ({count} images)")
    
    if config.get('training_history'):
        print(f"\nTraining History:")
        history = config['training_history']
        last_epoch = history[-1]
        print(f"  Epochs trained: {len(history)}")
        print(f"  Final loss: {last_epoch['loss']:.4f}")
        print(f"  Final accuracy: {last_epoch['accuracy']:.2f}%")
    
    print(f"{'='*70}\n")

def create_project(name, description=""):
    """Create a new project"""
    projects_dir = Path('projects')
    projects_dir.mkdir(exist_ok=True)
    
    project_dir = projects_dir / name
    
    if project_dir.exists():
        print(f"Error: Project '{name}' already exists!")
        return
    
    # Create project structure
    project_dir.mkdir()
    (project_dir / 'dataset').mkdir()
    (project_dir / 'models').mkdir()
    
    # Create config
    config = {
        "name": name,
        "description": description,
        "created_at": str(Path(__file__).stat().st_mtime),
        "num_classes": 0,
        "classes": [],
        "trained": False,
        "model_path": None,
        "training_history": []
    }
    
    config_file = project_dir / 'config.json'
    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✓ Project '{name}' created successfully!")
    print(f"  Location: {project_dir}")
    print(f"\nNext steps:")
    print(f"  1. Add your dataset to: {project_dir / 'dataset'}")
    print(f"  2. Organize images into class folders")
    print(f"  3. Run: python scripts/train_model.py --project {name}")

def train_project(project_name, epochs=10):
    """Train a project model"""
    config_file = Path('projects') / project_name / 'config.json'
    
    if not config_file.exists():
        print(f"Error: Project '{project_name}' not found!")
        return
    
    print(f"Starting training for project: {project_name}")
    print(f"Epochs: {epochs}")
    print(f"\nTraining output:\n")
    
    import subprocess
    cmd = [
        sys.executable,
        'scripts/train_model.py',
        '--project', project_name,
        '--epochs', str(epochs)
    ]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"\nError: Training failed with exit code {e.returncode}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Custom Image Classifier CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s list                              # List all projects
  %(prog)s info my_project                   # Show project details
  %(prog)s create animal_classifier          # Create new project
  %(prog)s train my_project --epochs 20      # Train model
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # List command
    subparsers.add_parser('list', help='List all projects')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show project information')
    info_parser.add_argument('project', help='Project name')
    
    # Create command
    create_parser = subparsers.add_parser('create', help='Create a new project')
    create_parser.add_argument('name', help='Project name')
    create_parser.add_argument('--description', '-d', default='', help='Project description')
    
    # Train command
    train_parser = subparsers.add_parser('train', help='Train a project model')
    train_parser.add_argument('project', help='Project name')
    train_parser.add_argument('--epochs', '-e', type=int, default=10, help='Number of epochs')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    if args.command == 'list':
        list_projects()
    elif args.command == 'info':
        show_project_info(args.project)
    elif args.command == 'create':
        create_project(args.name, args.description)
    elif args.command == 'train':
        train_project(args.project, args.epochs)

if __name__ == '__main__':
    main()
