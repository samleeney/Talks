import cv2


def blur_image(input_image_path, output_image_path, blur_strength=5):
    # Read the input image
    image = cv2.imread(input_image_path)

    # Check if image was successfully opened
    if image is None:
        print(f"Error: Could not open or find the image '{input_image_path}'.")
        return

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)

    # Save the blurred image
    cv2.imwrite(output_image_path, blurred_image)
    print(f"Blurred image saved as '{output_image_path}'.")


if __name__ == "__main__":
    # Example usage
    input_image_path = "input_image.jpg"  # Path to the input image
    output_image_path = "blurred_image.jpg"  # Path to save the output blurred image
    blur_strength = 15  # Strength of the blur, should be an odd number

    blur_image(input_image_path, output_image_path, blur_strength)
