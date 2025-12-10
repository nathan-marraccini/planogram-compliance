# Planogram Compliance Detection

A computer vision system for detecting planogram compliance using vision transformer embeddings and cosine similarity. This project provides two implementations using different state-of-the-art models: DINOv2 and CLIP.

## Overview

This project uses vision transformer models to generate image embeddings and compare test images against a reference set to determine product compliance in planogram layouts. Two different approaches are provided:

1. **DINOv2-based**: Uses Facebook's DINOv2 model for self-supervised learning-based embeddings
2. **CLIP-based**: Uses OpenAI's CLIP model for contrastive learning-based embeddings

## Features

- Image embedding generation using DINOv2-base or CLIP models
- Cosine similarity-based product matching
- Top-K similarity search for product identification
- Support for multiple vision transformer architectures

## Setup

1. Install dependencies:
```bash
pip install "torch>=2.2" "transformers>=4.45" pillow faiss-cpu numpy
```

2. Run either notebook:
   - `DINOv2_planogram_compliance.ipynb` - DINOv2-based implementation
   - `CLIP_planogram_compliance.ipynb` - CLIP-based implementation

Both notebooks will:
   - Generate embeddings for reference images
   - Test product matching on new images

## Usage

### DINOv2 Approach
The `DINOv2_planogram_compliance.ipynb` notebook contains:
- Model initialization with DINOv2-base
- Reference image embedding generation
- Test image similarity matching
- Saves embeddings to `dinov2_refs.npz`

### CLIP Approach
The `CLIP_planogram_compliance.ipynb` notebook contains:
- Model initialization with CLIP ViT-B/32
- Reference image embedding generation
- Test image similarity matching
- Saves embeddings to `clip_refs.npz`

## Files

- `DINOv2_planogram_compliance.ipynb` - DINOv2-based implementation notebook
- `CLIP_planogram_compliance.ipynb` - CLIP-based implementation notebook
- `dinov2_refs.npz` - Pre-computed DINOv2 reference embeddings
- `clip_refs.npz` - Pre-computed CLIP reference embeddings (generated when running CLIP notebook)
- `images/` - Reference and test product images

