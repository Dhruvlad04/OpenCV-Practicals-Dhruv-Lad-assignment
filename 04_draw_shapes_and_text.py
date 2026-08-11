import cv2
import numpy as np
from sample_image import get_sample_image_path

img = cv2.imread(get_sample_image_path())
canvas = img.copy()

# 1. Line
cv2.line(canvas, (20, 20), (300, 20), (0, 0, 255), 3)

# 2. Rectangle (outline)
cv2.rectangle(canvas, (20, 40), (200, 120), (0, 255, 0), 2)

# 3. Circle (filled)
cv2.circle(canvas, (400, 350), 50, (255, 0, 0), -1)

# 4. Polygon (e.g. a pentagon)
pts = np.array([[400, 50], [450, 90], [430, 150], [370, 150], [350, 90]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(canvas, [pts], isClosed=True, color=(255, 255, 0), thickness=3)

# 5. Text
cv2.putText(canvas, "Shapes & Text Demo", (20, 460),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("Original", img)
cv2.imshow("Shapes and Text", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("output_04_shapes_and_text.jpg", canvas)
print("Image with shapes and text saved.")
