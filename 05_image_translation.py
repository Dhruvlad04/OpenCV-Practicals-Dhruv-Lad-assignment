import cv2
import numpy as np
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
(h, w) = img.shape[:2]

tx, ty = 100, 60  # shift 100px right, 60px down
M = np.float32([[1, 0, tx],
                 [0, 1, ty]])

translated = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Original", img)
cv2.imshow(f"Translated (tx={tx}, ty={ty})", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_05_translated.jpg", translated)
print("Translated image saved.")
