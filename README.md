# Planogram Compliance Detection

A computer vision system for detecting planogram compliance using vision transformer embeddings and cosine similarity. This project provides two implementations using different state-of-the-art models: DINOv2 and CLIP.

## Overview

This project uses vision transformer models to generate image embeddings and compare test images against a reference set to determine product compliance in planogram layouts. Three different approaches are provided:

1. **DINOv2-based**: Uses Facebook's DINOv2 model for self-supervised learning-based embeddings
2. **CLIP-based**: Uses OpenAI's CLIP model for contrastive learning-based embeddings
3. **Roboflow API-based**: Uses Roboflow's workflow API for object detection + CLIP embeddings with automatic product matching

## Features

- Image embedding generation using DINOv2-base or CLIP models
- Cosine similarity-based product matching
- Top-K similarity search for product identification
- Support for multiple vision transformer architectures
- **NEW**: Roboflow-powered object detection + CLIP matching pipeline
- Automatic crop filtering (minimum size threshold)
- Batch processing of card thumbnail databases
- Visual bounding box overlay with match confidence scores

## Setup

1. Install dependencies:
```bash
pip install "torch>=2.2" "transformers>=4.45" pillow faiss-cpu numpy
```

2. Run any of the notebooks:
   - `DINOv2_planogram_compliance.ipynb` - DINOv2-based implementation
   - `clip_planogram_compliance.ipynb` - CLIP-based implementation
   - `Avanti_press/roboflow_planogram_compliance.ipynb` - Roboflow API-based implementation

The first two notebooks will:
   - Generate embeddings for reference images
   - Test product matching on new images

For the Roboflow notebook, you'll need:
```bash
pip install inference-sdk pillow numpy matplotlib
```

## Usage

### DINOv2 Approach
The `DINOv2_planogram_compliance.ipynb` notebook contains:
- Model initialization with DINOv2-base
- Reference image embedding generation
- Test image similarity matching
- Saves embeddings to `dinov2_refs.npz`

### CLIP Approach
The `clip_planogram_compliance.ipynb` notebook contains:
- Model initialization with CLIP ViT-B/32
- Reference image embedding generation
- Test image similarity matching
- Saves embeddings to `clip_refs.npz`

### Roboflow API Approach
The `Avanti_press/roboflow_planogram_compliance.ipynb` notebook contains:
- **End-to-end planogram compliance pipeline**
- Object detection + CLIP embedding extraction via Roboflow workflow API
- Automatic product matching against card thumbnail database
- Minimum crop size filtering (20x20 pixels) to filter out noise
- Cosine similarity matching with confidence scores
- Visual overlay showing detected products with matched card names
- Includes commented Option B for local CLIP processing as fallback
- Processes images from `Avanti_press/test.png` and matches against `Avanti_press/card_thumbnails (1)/`

## Files

- `DINOv2_planogram_compliance.ipynb` - DINOv2-based implementation notebook
- `clip_planogram_compliance.ipynb` - CLIP-based implementation notebook
- `Avanti_press/roboflow_planogram_compliance.ipynb` - Roboflow API-based implementation notebook
- `dinov2_refs.npz` - Pre-computed DINOv2 reference embeddings
- `clip_refs.npz` - Pre-computed CLIP reference embeddings (generated when running CLIP notebook)
- `images/` - Reference and test product images
- `Avanti_press/` - Roboflow workflow demo with card thumbnails database and test shelf image

