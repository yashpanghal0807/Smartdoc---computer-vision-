import cv2
import numpy as np


def detect_document(image):
    """
    Detect the largest four-sided document-like contour.

    Returns:
        numpy array containing four corner points,
        or None if no suitable document is found.
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, 50, 150)

    kernel = np.ones((5, 5), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    image_area = image.shape[0] * image.shape[1]

    for contour in contours[:20]:

        area = cv2.contourArea(contour)

        if area < image_area * 0.20:
            continue

        perimeter = cv2.arcLength(contour, True)

        approximation = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True
        )

        if len(approximation) == 4:
            return approximation.reshape(4, 2).astype(np.float32)

    return None
