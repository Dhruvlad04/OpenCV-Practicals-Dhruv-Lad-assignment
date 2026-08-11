import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
(h, w) = img.shape[:2]
center = (w // 2, h // 2)

def rotate(image, angle, scale=1.0):
    M = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, M, (w, h))

rotated_45 = rotate(img, 45)
rotated_90 = rotate(img, 90)
rotated_180 = rotate(img, 180)

cv2.imshow("Original", img)
cv2.imshow("Rotated 45 deg", rotated_45)
cv2.imshow("Rotated 90 deg", rotated_90)
cv2.imshow("Rotated 180 deg", rotated_180)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_06_rotated_45.jpg", rotated_45)
cv2.imwrite("output_06_rotated_90.jpg", rotated_90)
cv2.imwrite("output_06_rotated_180.jpg", rotated_180)
print("Rotated images saved.")
