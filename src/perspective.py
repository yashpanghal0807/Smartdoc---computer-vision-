import cv2
import numpy as np


def order_points(points):
    """
    Arrange four points in the order:
    top-left, top-right, bottom-right, bottom-left.
    """

    points = np.array(points, dtype=np.float32)

    ordered = np.zeros((4, 2), dtype=np.float32)

    total = points.sum(axis=1)
    difference = np.diff(points, axis=1).reshape(4)

    ordered[0] = points[np.argmin(total)]
    ordered[2] = points[np.argmax(total)]
    ordered[1] = points[np.argmin(difference)]
    ordered[3] = points[np.argmax(difference)]

    return ordered


def four_point_transform(image, points):
    """
    Apply perspective transformation using four document corners.
    """

    rect = order_points(points)

    top_left, top_right, bottom_right, bottom_left = rect

    width_top = np.linalg.norm(top_right - top_left)
    width_bottom = np.linalg.norm(bottom_right - bottom_left)

    max_width = int(max(width_top, width_bottom))

    height_right = np.linalg.norm(
        bottom_right - top_right
    )

    height_left = np.linalg.norm(
        bottom_left - top_left
    )

    max_height = int(max(height_right, height_left))

    destination = np.array([
        [0, 0],
        [max_width - 1, 0],
        [max_width - 1, max_height - 1],
        [0, max_height - 1]
    ], dtype=np.float32)

    matrix = cv2.getPerspectiveTransform(
        rect,
        destination
    )

    warped = cv2.warpPerspective(
        image,
        matrix,
        (max_width, max_height)
    )

    return warped
