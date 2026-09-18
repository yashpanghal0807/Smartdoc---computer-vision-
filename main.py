import argparse
import os

from src.document_detector import detect_document
from src.perspective import four_point_transform
from src.enhancement import enhance_document
from src.quality import analyze_quality
from src.io_utils import load_image, save_image


def process_document(input_path, output_dir="output"):
    """
    Complete Smartdoc document processing pipeline.
    """

    image = load_image(input_path)

    if image is None:
        raise FileNotFoundError(
            f"Could not load image: {input_path}"
        )

    print("[1/5] Detecting document...")

    corners = detect_document(image)

    if corners is None:
        print("No document boundary detected.")
        return False

    print("[2/5] Correcting perspective...")

    corrected = four_point_transform(
        image,
        corners
    )

    print("[3/5] Enhancing document...")

    enhanced = enhance_document(corrected)

    print("[4/5] Analyzing image quality...")

    quality = analyze_quality(corrected)

    os.makedirs(output_dir, exist_ok=True)

    corrected_path = os.path.join(
        output_dir,
        "corrected_document.jpg"
    )

    enhanced_path = os.path.join(
        output_dir,
        "enhanced_document.jpg"
    )

    save_image(corrected_path, corrected)
    save_image(enhanced_path, enhanced)

    print("[5/5] Processing complete.")

    print("\nQuality Report")
    print("-------------------------")
    print(
        f"Brightness: {quality['brightness']:.2f}"
    )
    print(
        f"Contrast: {quality['contrast']:.2f}"
    )
    print(
        f"Sharpness: {quality['sharpness']:.2f}"
    )
    print(
        f"Edge Density: {quality['edge_density']:.4f}"
    )
    print(
        f"Quality: {quality['quality_label']}"
    )

    print("\nResults saved in:", output_dir)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Smartdoc - Computer Vision Document Scanner"
    )

    parser.add_argument(
        "input",
        help="Path to the input document image"
    )

    parser.add_argument(
        "--output",
        default="output",
        help="Directory for processed images"
    )

    args = parser.parse_args()

    try:
        process_document(
            args.input,
            args.output
        )

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
