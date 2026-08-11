import cv2
from sample_image import get_sample_image_path

# 1. Read the image
image_path = get_sample_image_path()
img = cv2.imread(image_path)

if img is None:
    raise FileNotFoundError(f"Could not read image at {image_path}")

print(f"Image loaded successfully. Shape (H, W, Channels): {img.shape}")

# 2. Display the image
cv2.imshow("Original Image", img)
print("Press any key on the image window to continue...")
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Save a copy of the image
output_path = "output_01_saved_copy.jpg"
cv2.imwrite(output_path, img)
print(f"Image saved to: {output_path}")
