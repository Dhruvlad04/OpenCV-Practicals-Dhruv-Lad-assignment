import cv2
import numpy as np
import os

# ✅ Load image safely

image_path = "BMWm5.jpeg"
if not os.path.exists(image_path):
    print(f"⚠️ File not found at {image_path}. Please place an image in the same folder.")
    exit()

img = cv2.imread(image_path)
if img is None:
    print("Error: Unable to read image. Check file format or path.")
    exit()

# 1. Display and save
cv2.imshow('Original Image', img)
cv2.imwrite('saved.jpg', img)
cv2.waitKey(0)

# 2. Resize
resized = cv2.resize(img, (300, 300))
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)

# 3. Flip
cv2.imshow('Flip Horizontal', cv2.flip(img, 1))
cv2.imshow('Flip Vertical', cv2.flip(img, 0))
cv2.imshow('Flip Both', cv2.flip(img, -1))
cv2.waitKey(0)

# 4. Draw shapes and text
drawn = img.copy()
cv2.line(drawn, (0,0), (200,200), (255,0,0), 5)
pts = np.array([[50,50],[150,50],[100,150]], np.int32)
cv2.polylines(drawn, [pts], True, (0,255,0), 3)
cv2.putText(drawn, 'OpenCV Demo', (50,250), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)
cv2.imshow('Shapes and Text', drawn)
cv2.waitKey(0)

# 5. Translation
rows, cols = img.shape[:2]
M = np.float32([[1,0,50],[0,1,100]])
translated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Translated Image', translated)
cv2.waitKey(0)

# 6. Rotation
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
rotated = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('Rotated Image', rotated)
cv2.waitKey(0)

# 7. Thresholding
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)

# 8. Blurring
cv2.imshow('Gaussian Blur', cv2.GaussianBlur(img, (5,5), 0))
cv2.imshow('Median Blur', cv2.medianBlur(img, 5))
cv2.waitKey(0)

# 9. Morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
cv2.imshow('Tophat', cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel))
cv2.imshow('Blackhat', cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel))
cv2.waitKey(0)

# 10. Edge detection
edges = cv2.Canny(img, 100, 200)
cv2.imshow('Canny Edges', edges)
cv2.waitKey(0)

# 11. Video read/write
cap = cv2.VideoCapture('video.mp4')  # Place a sample video in the folder
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Video Playback', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()

# 12. Live webcam capture
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
