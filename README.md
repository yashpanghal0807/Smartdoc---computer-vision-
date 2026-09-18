# Smartdoc - Computer Vision

## Computer Vision Based Document Scanner & Image Quality Analyzer

Smartdoc - Computer Vision is a Computer Vision project that automatically detects a document from an input photograph, corrects its perspective, enhances the image, and analyzes its visual quality.

The project uses classical Computer Vision techniques such as grayscale conversion, Gaussian Blur, Canny Edge Detection, contour detection, polygon approximation, perspective transformation, CLAHE enhancement, and adaptive thresholding.

---

## Problem Statement

Photographs of documents are often captured at an angle. This causes perspective distortion and can make the document difficult to read. Uneven lighting, blur, noise, and low contrast can further reduce image quality.

Smartdoc - Computer Vision provides an automated solution that detects the document boundary, corrects the perspective, enhances the document image, and generates quality measurements.

---

## Objectives

- Detect a document from an input image.
- Identify the four corners of the document.
- Correct perspective distortion.
- Improve document readability.
- Apply adaptive thresholding.
- Calculate image quality metrics.
- Save processed images automatically.
- Provide a simple command-line interface.

---

## Features

### 1. Document Detection

The system uses:

- Grayscale conversion
- Gaussian Blur
- Canny Edge Detection
- Morphological operations
- Contour detection
- Polygon approximation

to identify a rectangular document.

### 2. Perspective Correction

The detected four corners are ordered and used to perform a perspective transformation.

### 3. Image Enhancement

The corrected document is processed using:

- Grayscale conversion
- Denoising
- CLAHE contrast enhancement
- Adaptive thresholding

### 4. Image Quality Analysis

The system calculates:

- Mean brightness
- Contrast
- Blur score
- Edge density
- Overall quality label

### 5. Automated Testing

Unit tests are included for important Computer Vision operations.

---

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- unittest

---

## Project Structure

```text
Smartdoc - Computer Vision/
│
├── README.md
├── statement.md
├── requirements.txt
├── main.py
├── generate_sample.py
│
├── src/
│   ├── __init__.py
│   ├── document_detector.py
│   ├── perspective.py
│   ├── enhancement.py
│   ├── quality.py
│   └── io_utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_core.py
│
└── docs/
    └── diagrams.md
