import cv2
import numpy as np
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))

tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original (Gray)", gray)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_09_tophat.jpg", tophat)
cv2.imwrite("output_09_blackhat.jpg", blackhat)
print("Morphological operation outputs saved.")
