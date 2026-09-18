import cv2


def enhance_document(image):
    """
    Enhance a perspective-corrected document image.

    Steps:
    1. Convert to grayscale
    2. Reduce noise
    3. Improve local contrast using CLAHE
    4. Apply adaptive thresholding
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    denoised = cv2.GaussianBlur(
        gray,
        (3, 3),
        0
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    enhanced = clahe.apply(denoised)

    thresholded = cv2.adaptiveThreshold(
        enhanced,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        21,
        10
    )

    return thresholded
