# System Design and Diagrams

## 1. System Architecture

The Smartdoc system follows a modular Computer Vision pipeline.

```text
User
  |
  v
Input Document Image
  |
  v
Image Loading
  |
  v
Document Detection
  |
  v
Perspective Correction
  |
  v
Image Enhancement
  |
  v
Quality Analysis
  |
  v
Processed Document + Quality Report
