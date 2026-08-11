import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())

flip_horizontal = cv2.flip(img, 1)
flip_vertical = cv2.flip(img, 0)
flip_both = cv2.flip(img, -1)

cv2.imshow("Original", img)
cv2.imshow("Flipped Horizontal", flip_horizontal)
cv2.imshow("Flipped Vertical", flip_vertical)
cv2.imshow("Flipped Both", flip_both)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_03_flip_horizontal.jpg", flip_horizontal)
cv2.imwrite("output_03_flip_vertical.jpg", flip_vertical)
cv2.imwrite("output_03_flip_both.jpg", flip_both)
print("All flipped images saved.")
