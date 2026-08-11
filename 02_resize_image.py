
import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
print(f"Original size (W x H): {img.shape[1]} x {img.shape[0]}")

# 1. Resize to fixed dimensions
resized_fixed = cv2.resize(img, (300, 200))  # (width, height)
print(f"Resized (fixed) size: {resized_fixed.shape[1]} x {resized_fixed.shape[0]}")

# 2. Resize using scale factors (50% of original)
resized_scaled = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
print(f"Resized (scaled 0.5x) size: {resized_scaled.shape[1]} x {resized_scaled.shape[0]}")

# 3. Enlarge (150%)
resized_large = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
print(f"Resized (scaled 1.5x) size: {resized_large.shape[1]} x {resized_large.shape[0]}")

# Display
cv2.imshow("Original", img)
cv2.imshow("Resized - Fixed 300x200", resized_fixed)
cv2.imshow("Resized - 0.5x", resized_scaled)
cv2.imshow("Resized - 1.5x", resized_large)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save outputs
cv2.imwrite("output_02_resized_fixed.jpg", resized_fixed)
cv2.imwrite("output_02_resized_scaled.jpg", resized_scaled)
print("Resized images saved.")
