import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh_value = 127
max_value = 255
ret, binary = cv2.threshold(gray, thresh_value, max_value, cv2.THRESH_BINARY)
ret_inv, binary_inv = cv2.threshold(gray, thresh_value, max_value, cv2.THRESH_BINARY_INV)

print(f"Threshold value used: {thresh_value}")

cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Binary Threshold", binary)
cv2.imshow("Binary Threshold Inverted", binary_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_07_binary_threshold.jpg", binary)
cv2.imwrite("output_07_binary_threshold_inv.jpg", binary_inv)
print("Thresholded images saved.")
