import argparse
import os

from src.document_detector import detect_document
from src.perspective import four_point_transform
from src.enhancement import enhance_document
from src.quality import analyze_quality
from src.io_utils import load_image, save_image


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
        help="Folder where processed images will be saved"
    )

    args = parser.parse_args()

    image = load_image(args.input)

    if image is None:
        print("Error: Could not load the input image.")
        return

    print("Detecting document...")

    corners = detect_document(image)

    if corners is None:
        print("Error: Document boundary could not be detected.")
        return

    print("Document detected successfully.")

    warped = four_point_transform(image, corners)

    enhanced = enhance_document(warped)

    quality = analyze_quality(enhanced)

    os.makedirs(args.output, exist_ok=True)

    save_image(
        os.path.join(args.output, "scanned_document.jpg"),
        enhanced
    )

    print("\n--- Image Quality Report ---")
    print(f"Brightness : {quality['brightness']:.2f}")
    print(f"Contrast   : {quality['contrast']:.2f}")
    print(f"Sharpness  : {quality['sharpness']:.2f}")
    print(f"Edge Density: {quality['edge_density']:.4f}")
    print(f"Quality    : {quality['quality_label']}")

    print("\nProcessing completed successfully.")
    print(f"Output saved in: {args.output}")


if __name__ == "__main__":
    main()
