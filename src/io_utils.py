import cv2
import os


def load_image(path):
    """
    Load an image from the given file path.

    Returns:
        Image as a NumPy array, or None if loading fails.
    """

    if not os.path.exists(path):
        return None

    image = cv2.imread(path)

    return image


def save_image(path, image):
    """
    Save the processed image to the given path.
    """

    folder = os.path.dirname(path)

    if folder:
        os.makedirs(folder, exist_ok=True)

    success = cv2.imwrite(path, image)

    return success
