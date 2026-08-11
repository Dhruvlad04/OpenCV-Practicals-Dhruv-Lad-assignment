import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())

gaussian_blurred = cv2.GaussianBlur(img, (9, 9), sigmaX=0)
median_blurred = cv2.medianBlur(img, 9)  # kernel size must be odd

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian_blurred)
cv2.imshow("Median Blur", median_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_08_gaussian_blur.jpg", gaussian_blurred)
cv2.imwrite("output_08_median_blur.jpg", median_blurred)
print("Blurred images saved.")
