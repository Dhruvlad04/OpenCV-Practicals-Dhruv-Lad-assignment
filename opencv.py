import cv2
import numpy as np
import os


# ============================================================
# OpenCV Practicals - Main Program
# ============================================================

INPUT_IMAGE = "input/sample.jpg"
INPUT_VIDEO = "input/sample.mp4"

OUTPUT_FOLDER = "output"


# Create output folder automatically
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)


# ============================================================
# Check Image
# ============================================================

def load_image():

    image = cv2.imread(INPUT_IMAGE)

    if image is None:
        print("\nERROR: sample.jpg not found!")
        print("Place your image inside the input folder.")
        return None

    return image


# ============================================================
# 1. Read, Display and Save Image
# ============================================================

def read_display_save():

    image = load_image()

    if image is None:
        return

    cv2.imshow("Original Image", image)

    cv2.imwrite(
        "output/saved_image.jpg",
        image
    )

    print("\nImage read successfully.")
    print("Image saved as output/saved_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 2. Resize Image
# ============================================================

def resize_image():

    image = load_image()

    if image is None:
        return

    resized = cv2.resize(
        image,
        (600, 400)
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)

    cv2.imwrite(
        "output/resized.jpg",
        resized
    )

    print("\nImage resized successfully.")
    print("Saved as output/resized.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 3. Flip Image
# ============================================================

def flip_image():

    image = load_image()

    if image is None:
        return

    horizontal = cv2.flip(image, 1)
    vertical = cv2.flip(image, 0)
    both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("Horizontal Flip", horizontal)
    cv2.imshow("Vertical Flip", vertical)
    cv2.imshow("Both Flip", both)

    cv2.imwrite(
        "output/horizontal_flip.jpg",
        horizontal
    )

    cv2.imwrite(
        "output/vertical_flip.jpg",
        vertical
    )

    cv2.imwrite(
        "output/both_flip.jpg",
        both
    )

    print("\nFlip operations completed.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 4. Draw Shapes and Add Text
# ============================================================

def draw_shapes_text():

    image = load_image()

    if image is None:
        return

    # Line
    cv2.line(
        image,
        (50, 50),
        (400, 50),
        (255, 0, 0),
        3
    )

    # Rectangle
    cv2.rectangle(
        image,
        (50, 100),
        (300, 250),
        (0, 255, 0),
        3
    )

    # Circle
    cv2.circle(
        image,
        (450, 180),
        80,
        (0, 0, 255),
        3
    )

    # Polygon
    points = np.array([
        [350, 300],
        [450, 250],
        [550, 300],
        [500, 400],
        [400, 400]
    ], np.int32)

    cv2.polylines(
        image,
        [points],
        True,
        (255, 255, 0),
        3
    )

    # Text
    cv2.putText(
        image,
        "OpenCV Practical",
        (50, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow(
        "Shapes and Text",
        image
    )

    cv2.imwrite(
        "output/shapes_text.jpg",
        image
    )

    print("\nShapes and text added successfully.")
    print("Saved as output/shapes_text.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 5. Image Translation using warpAffine
# ============================================================

def translation():

    image = load_image()

    if image is None:
        return

    rows, cols = image.shape[:2]

    x = 100
    y = 50

    matrix = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])

    translated = cv2.warpAffine(
        image,
        matrix,
        (cols, rows)
    )

    cv2.imshow("Original", image)
    cv2.imshow("Translated", translated)

    cv2.imwrite(
        "output/translated.jpg",
        translated
    )

    print("\nImage translated successfully.")
    print("Saved as output/translated.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 6. Image Rotation
# ============================================================

def rotation():

    image = load_image()

    if image is None:
        return

    height, width = image.shape[:2]

    center = (
        width // 2,
        height // 2
    )

    matrix = cv2.getRotationMatrix2D(
        center,
        45,
        1.0
    )

    rotated = cv2.warpAffine(
        image,
        matrix,
        (width, height)
    )

    cv2.imshow("Original", image)
    cv2.imshow("Rotated 45 Degrees", rotated)

    cv2.imwrite(
        "output/rotated.jpg",
        rotated
    )

    print("\nImage rotated successfully.")
    print("Saved as output/rotated.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 7. Binary Thresholding
# ============================================================

def thresholding():

    image = load_image()

    if image is None:
        return

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    _, threshold = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    cv2.imshow("Original Gray", gray)
    cv2.imshow("Binary Threshold", threshold)

    cv2.imwrite(
        "output/threshold.jpg",
        threshold
    )

    print("\nBinary threshold applied successfully.")
    print("Saved as output/threshold.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 8. Gaussian Blur and Median Blur
# ============================================================

def blurring():

    image = load_image()

    if image is None:
        return

    gaussian = cv2.GaussianBlur(
        image,
        (5, 5),
        0
    )

    median = cv2.medianBlur(
        image,
        5
    )

    cv2.imshow("Original", image)
    cv2.imshow("Gaussian Blur", gaussian)
    cv2.imshow("Median Blur", median)

    cv2.imwrite(
        "output/gaussian_blur.jpg",
        gaussian
    )

    cv2.imwrite(
        "output/median_blur.jpg",
        median
    )

    print("\nBlurring completed.")
    print("Gaussian Blur saved.")
    print("Median Blur saved.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 9. Tophat and Blackhat
# ============================================================

def morphological_operations():

    image = load_image()

    if image is None:
        return

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (9, 9)
    )

    tophat = cv2.morphologyEx(
        gray,
        cv2.MORPH_TOPHAT,
        kernel
    )

    blackhat = cv2.morphologyEx(
        gray,
        cv2.MORPH_BLACKHAT,
        kernel
    )

    cv2.imshow("Original", gray)
    cv2.imshow("Tophat", tophat)
    cv2.imshow("Blackhat", blackhat)

    cv2.imwrite(
        "output/tophat.jpg",
        tophat
    )

    cv2.imwrite(
        "output/blackhat.jpg",
        blackhat
    )

    print("\nMorphological operations completed.")
    print("Tophat saved.")
    print("Blackhat saved.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 10. Canny Edge Detection
# ============================================================

def edge_detection():

    image = load_image()

    if image is None:
        return

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    cv2.imshow("Original", image)
    cv2.imshow("Canny Edge Detection", edges)

    cv2.imwrite(
        "output/canny_edges.jpg",
        edges
    )

    print("\nCanny edge detection completed.")
    print("Saved as output/canny_edges.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# ============================================================
# 11. Read and Write Video
# ============================================================

def video_read_write():

    cap = cv2.VideoCapture(
        INPUT_VIDEO
    )

    if not cap.isOpened():

        print("\nERROR: sample.mp4 not found!")
        print("Place your video inside the input folder.")

        return

    width = int(
        cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    )

    height = int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )

    fps = cap.get(
        cv2.CAP_PROP_FPS
    )

    if fps <= 0:
        fps = 30

    fourcc = cv2.VideoWriter_fourcc(
        *"mp4v"
    )

    out = cv2.VideoWriter(
        "output/output_video.mp4",
        fourcc,
        fps,
        (width, height)
    )

    print("\nVideo processing started.")
    print("Press Q to stop.")

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow(
            "Input Video",
            frame
        )

        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()

    print("Video processing completed.")
    print("Saved as output/output_video.mp4")


# ============================================================
# 12. Live Webcam
# ============================================================

def webcam_capture():

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():

        print("\nERROR: Webcam could not be opened.")

        return

    print("\nWebcam started.")
    print("Press Q to exit.")

    while True:

        ret, frame = cap.read()

        if not ret:

            print("Unable to read webcam frame.")
            break

        cv2.imshow(
            "Live Webcam",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()

    cv2.destroyAllWindows()

    print("Webcam stopped.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("=" * 60)
        print("             OPENCV PRACTICALS")
        print("=" * 60)

        print("1.  Read, Display and Save Image")
        print("2.  Resize Image")
        print("3.  Flip Image")
        print("4.  Draw Shapes and Add Text")
        print("5.  Image Translation")
        print("6.  Image Rotation")
        print("7.  Binary Thresholding")
        print("8.  Gaussian and Median Blur")
        print("9.  Tophat and Blackhat")
        print("10. Canny Edge Detection")
        print("11. Read and Write Video")
        print("12. Capture Live Webcam")
        print("0.  Exit")

        print("=" * 60)

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":
            read_display_save()

        elif choice == "2":
            resize_image()

        elif choice == "3":
            flip_image()

        elif choice == "4":
            draw_shapes_text()

        elif choice == "5":
            translation()

        elif choice == "6":
            rotation()

        elif choice == "7":
            thresholding()

        elif choice == "8":
            blurring()

        elif choice == "9":
            morphological_operations()

        elif choice == "10":
            edge_detection()

        elif choice == "11":
            video_read_write()

        elif choice == "12":
            webcam_capture()

        elif choice == "0":

            print("\nThank you!")
            print("OpenCV Practicals Completed.")

            break

        else:

            print("\nInvalid choice!")
            print("Please enter a number from 0 to 12.")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()
