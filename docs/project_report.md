# Smartdoc - Computer Vision Document Scanner

## 1. Introduction

Smartdoc is a Computer Vision based document scanning and image quality analysis system. It takes a document image as input, detects the document boundary, corrects perspective, enhances the document and analyzes its image quality.

## 2. Problem Statement

Photos of documents may contain tilted pages, perspective distortion, noise, poor lighting and blur. These problems make documents difficult to read and process.

Smartdoc solves this problem using Computer Vision techniques to automatically detect and process document images.

## 3. Objectives

- Detect document boundaries automatically.
- Correct perspective distortion.
- Improve document readability.
- Analyze image quality.
- Provide processed output images.

## 4. Functional Modules

### Module 1: Document Detection

Uses grayscale conversion, Gaussian blur, Canny edge detection, morphological operations and contour detection to identify a four-sided document.

### Module 2: Perspective Correction

The four detected corners are ordered and a perspective transformation is applied using a homography matrix.

### Module 3: Document Enhancement

The corrected document is converted to grayscale, denoised, enhanced using CLAHE and processed using adaptive thresholding.

### Module 4: Quality Analysis

The system calculates brightness, contrast, sharpness and edge density and produces a quality label.

### Module 5: Input and Output Handling

The system loads input images, processes them and saves corrected and enhanced images.

## 5. Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- GitHub

## 6. Computer Vision Techniques

The project uses:

- Grayscale conversion
- Gaussian filtering
- Canny edge detection
- Morphological processing
- Contour detection
- Polygon approximation
- Perspective transformation
- CLAHE
- Adaptive thresholding
- Laplacian variance for sharpness

## 7. System Workflow

Input Image  
↓  
Image Loading  
↓  
Document Detection  
↓  
Corner Detection  
↓  
Perspective Correction  
↓  
Document Enhancement  
↓  
Quality Analysis  
↓  
Processed Output

## 8. Architecture

The project follows a modular architecture.

`main.py` acts as the main controller and connects the different modules.

The `src` folder contains separate modules for document detection, perspective correction, enhancement, quality analysis and image input/output.

The `tests` folder contains automated tests for important functions.

## 9. Non-Functional Requirements

- Performance: The system should process normal document images efficiently.
- Usability: The command-line interface should be simple to use.
- Reliability: Invalid image paths should be handled safely.
- Maintainability: Computer Vision operations are separated into independent modules.
- Scalability: Additional image-processing techniques can be added as separate modules.
- Error Handling: The program reports errors when an image cannot be loaded.

## 10. Testing

The project includes tests for:

- Perspective transformation
- Document enhancement
- Image quality analysis

Synthetic images are used to verify the core functions.

## 11. Expected Output

The system produces:

- A perspective-corrected document image.
- An enhanced document image.
- A quality report containing brightness, contrast, sharpness, edge density and quality label.

## 12. Challenges

Some challenges include detecting documents under poor lighting, handling noisy edges and correctly identifying the four document corners.

## 13. Learnings

Through this project, we learned how Computer Vision techniques can be combined into a complete image-processing pipeline. We also learned modular Python development, OpenCV processing and automated testing.

## 14. Future Enhancements

- Mobile application interface.
- OCR-based text extraction.
- Automatic document rotation.
- Better detection for complex backgrounds.
- PDF generation.
- Machine-learning based document quality prediction.

## 15. Conclusion

Smartdoc demonstrates a practical Computer Vision solution for document scanning and quality analysis. The modular design makes the system easier to test, maintain and extend.

## 16. References

- OpenCV Documentation
- NumPy Documentation
- Python Documentation
