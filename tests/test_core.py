import cv2
import numpy as np

from src.enhancement import enhance_document
from src.quality import analyze_quality
from src.perspective import four_point_transform


def create_test_image():
    """Create a simple synthetic document image for testing."""

    image = np.ones((400, 300, 3), dtype=np.uint8) * 255

    cv2.rectangle(
        image,
        (50, 50),
        (250, 350),
        (0, 0, 0),
        3
    )

    return image


def test_perspective_transform():
    image = create_test_image()

    points = np.array([
        [50, 50],
        [250, 50],
        [250, 350],
        [50, 350]
    ], dtype=np.float32)

    result = four_point_transform(image, points)

    assert result is not None
    assert result.shape[0] > 0
    assert result.shape[1] > 0


def test_enhancement():
    image = create_test_image()

    result = enhance_document(image)

    assert result is not None
    assert len(result.shape) == 2


def test_quality_analysis():
    image = create_test_image()

    result = analyze_quality(image)

    assert "brightness" in result
    assert "contrast" in result
    assert "sharpness" in result
    assert "edge_density" in result
    assert "quality_label" in result
