# Example Dataset Structures

This document provides examples of how to organize your dataset for different use cases.

## Basic Structure

All datasets should follow this folder structure:

```
dataset_name/
├── class1/
│   ├── image1.jpg
│   ├── image2.jpg
│   └── ...
├── class2/
│   ├── image1.jpg
│   └── ...
└── class3/
    └── ...
```

## Example 1: Animal Classification

```
animals/
├── dog/
│   ├── dog_001.jpg
│   ├── dog_002.jpg
│   ├── dog_003.jpg
│   └── ... (50-100+ images)
├── cat/
│   ├── cat_001.jpg
│   ├── cat_002.jpg
│   └── ...
├── bird/
│   └── ...
└── fish/
    └── ...
```

## Example 2: Flower Species

```
flowers/
├── rose/
│   └── ...
├── tulip/
│   └── ...
├── sunflower/
│   └── ...
└── daisy/
    └── ...
```

## Example 3: Quality Control (Binary Classification)

```
product_inspection/
├── defective/
│   ├── defect_001.jpg
│   ├── defect_002.jpg
│   └── ...
└── good/
    ├── good_001.jpg
    ├── good_002.jpg
    └── ...
```

## Example 4: Document Classification

```
documents/
├── invoice/
│   └── ...
├── receipt/
│   └── ...
├── contract/
│   └── ...
└── letter/
    └── ...
```

## Example 5: Plant Disease Detection

```
plant_health/
├── healthy/
│   └── ...
├── bacterial_spot/
│   └── ...
├── early_blight/
│   └── ...
├── late_blight/
│   └── ...
└── leaf_mold/
    └── ...
```

## Best Practices

### Naming Conventions
- Use lowercase for folder names
- Avoid spaces (use underscores instead)
- Be descriptive but concise
- Examples: `golden_retriever`, `red_rose`, `invoice_2023`

### Image Organization
- **Minimum**: 20-30 images per class (for testing)
- **Recommended**: 50-100 images per class
- **Optimal**: 200+ images per class
- Balance: Try to have similar numbers across classes

### Image Quality
- Resolution: Any size (automatically resized to 128x128)
- Format: JPG, PNG, GIF, or BMP
- Quality: Clear, well-lit photos
- Variety: Different angles, lighting, backgrounds

### Example Good Dataset
```
dog_breeds/
├── golden_retriever/          # 150 images
│   ├── golden_001.jpg
│   ├── golden_002.jpg
│   └── ...
├── labrador/                   # 145 images
│   └── ...
├── german_shepherd/            # 160 images
│   └── ...
└── poodle/                     # 140 images
    └── ...
```

### Example Poor Dataset (Avoid)
```
dogs/
├── big_dogs/                   # Too vague
│   ├── mix1.jpg              # Mixed breeds unclear
│   └── ...
├── small/                      # Inconsistent naming
│   └── ...                     # Only 10 images - too few
└── medium-sized-dogs/          # Spaces and hyphens
    └── ...
```

## Creating a Zip File

### On macOS/Linux:
```bash
cd path/to/your/dataset
zip -r my_dataset.zip dataset_name/
```

### On Windows:
1. Right-click the dataset folder
2. Select "Send to" → "Compressed (zipped) folder"

### Using Python:
```python
import shutil

shutil.make_archive('my_dataset', 'zip', 'path/to/dataset_name')
```

## Quick Start Templates

Download these example dataset structures:

### Template 1: Binary Classification
```
my_project/
├── positive/
│   └── (your images here)
└── negative/
    └── (your images here)
```

### Template 2: Multi-class (5 classes)
```
my_project/
├── class_a/
├── class_b/
├── class_c/
├── class_d/
└── class_e/
```

### Template 3: Fine-grained Classification
```
my_project/
├── category1_type1/
├── category1_type2/
├── category2_type1/
├── category2_type2/
└── ...
```

## Tips for Gathering Images

### Web Scraping (Legal & Ethical)
- Use Google Images (respect copyright)
- Check Creative Commons images
- Use royalty-free image sites (Unsplash, Pexels)

### Taking Your Own Photos
- Use consistent lighting
- Multiple angles per subject
- Vary backgrounds
- Include different sizes/distances

### Data Augmentation
- The framework automatically applies:
  - Random flips
  - Random rotations
  - Color adjustments
- This effectively multiplies your dataset

## Common Mistakes to Avoid

❌ **Don't:**
- Mix multiple subjects in one image
- Use extremely low-quality images
- Have highly imbalanced classes (e.g., 1000 vs 10)
- Include corrupted files
- Use ambiguous class names

✅ **Do:**
- One clear subject per image
- Good resolution and lighting
- Balance classes reasonably
- Test images are separate from training
- Use descriptive, unique class names

## Need More Help?

Check the main README.md or GETTING_STARTED.md for more information!
