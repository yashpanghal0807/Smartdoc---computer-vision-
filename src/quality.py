import cv2
import numpy as np


def analyze_quality(image):
    """
    Analyze basic image quality metrics.

    Returns:
        Dictionary containing brightness, contrast,
        sharpness, edge density, and quality label.
    """

    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    brightness = float(np.mean(gray))

    contrast = float(np.std(gray))

    sharpness = float(
        cv2.Laplacian(gray, cv2.CV_64F).var()
    )

    edges = cv2.Canny(gray, 100, 200)

    edge_density = float(
        np.count_nonzero(edges) / edges.size
    )

    score = 0

    if 70 <= brightness <= 200:
        score += 1

    if contrast >= 35:
        score += 1

    if sharpness >= 100:
        score += 1

    if 0.02 <= edge_density <= 0.30:
        score += 1

    if score >= 3:
        quality_label = "Good"
    elif score == 2:
        quality_label = "Average"
    else:
        quality_label = "Needs Improvement"

    return {
        "brightness": brightness,
        "contrast": contrast,
        "sharpness": sharpness,
        "edge_density": edge_density,
        "quality_label": quality_label
    }
