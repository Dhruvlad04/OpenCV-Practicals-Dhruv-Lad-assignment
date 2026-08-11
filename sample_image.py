import os
import cv2
import numpy as np

IMAGE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sample.jpg")


def get_sample_image_path():
    """Return the path to sample.jpg, creating a synthetic one if it
    doesn't already exist."""
    if not os.path.exists(IMAGE_PATH):
        img = np.full((480, 640, 3), (245, 222, 179), dtype=np.uint8)  # light background

        cv2.rectangle(img, (50, 50), (250, 200), (255, 0, 0), -1)      # blue rectangle
        cv2.circle(img, (450, 120), 80, (0, 165, 255), -1)             # orange circle
        cv2.line(img, (50, 300), (600, 300), (0, 0, 0), 4)             # black line
        cv2.putText(img, "OpenCV Sample Image", (60, 400),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 0, 128), 2, cv2.LINE_AA)

        cv2.imwrite(IMAGE_PATH, img)
        print(f"[sample_image] Generated synthetic sample image at: {IMAGE_PATH}")

    return IMAGE_PATH


if __name__ == "__main__":
    path = get_sample_image_path()
    print(f"Sample image ready at: {path}")
