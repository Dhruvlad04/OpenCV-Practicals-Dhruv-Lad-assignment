import cv2

cap = cv2.VideoCapture(0)  # 0 = default webcam

if not cap.isOpened():
    raise IOError("Cannot open webcam. Make sure a camera is connected "
                   "and not being used by another application.")

print("Webcam opened. Press 's' to save a snapshot, 'q' to quit.")
snapshot_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break

    cv2.imshow("Live Webcam Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        snapshot_count += 1
        filename = f"output_12_webcam_snapshot_{snapshot_count}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Snapshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()
print("Webcam released. Program ended.")
