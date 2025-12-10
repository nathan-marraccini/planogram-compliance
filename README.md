# Planogram Compliance Detection

A computer vision system for detecting planogram compliance using DINOv2 embeddings and cosine similarity.

## Overview

This project uses Facebook's DINOv2 model to generate image embeddings and compare test images against a reference set to determine product compliance in planogram layouts.

## Features

- Image embedding generation using DINOv2-base model
- Cosine similarity-based product matching
- Top-K similarity search for product identification

## Setup

1. Install dependencies:
```bash
pip install "torch>=2.2" "transformers>=4.45" pillow faiss-cpu numpy
```

2. Run the notebook `planogram_compliance.ipynb` to:
   - Generate embeddings for reference images
   - Test product matching on new images

## Usage

The notebook contains:
- Model initialization with DINOv2-base
- Reference image embedding generation
- Test image similarity matching

## Files

- `planogram_compliance.ipynb` - Main notebook with implementation
- `dinov2_refs.npz` - Pre-computed reference embeddings
- `images/` - Reference and test product images

