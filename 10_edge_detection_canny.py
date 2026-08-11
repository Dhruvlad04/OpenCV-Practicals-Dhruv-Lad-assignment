import cv2
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

cv2.imshow("Original", img)
cv2.imshow("Grayscale + Blurred", blurred)
cv2.imshow("Canny Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_10_canny_edges.jpg", edges)
print("Edge-detected image saved.")
