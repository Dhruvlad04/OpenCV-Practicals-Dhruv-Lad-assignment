import cv2
import numpy as np
import os

VIDEO_PATH = "output_11_sample_video.mp4"


def create_sample_video(path, num_frames=60, fps=20, size=(640, 480)):
    """Generate a simple synthetic video: a circle moving across frames."""
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(path, fourcc, fps, size)

    for i in range(num_frames):
        frame = np.full((size[1], size[0], 3), (245, 222, 179), dtype=np.uint8)
        x = int((i / num_frames) * (size[0] - 60)) + 30
        cv2.circle(frame, (x, size[1] // 2), 30, (0, 0, 255), -1)
        cv2.putText(frame, f"Frame {i+1}/{num_frames}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)
        writer.write(frame)

    writer.release()
    print(f"Sample video written to: {path} ({num_frames} frames @ {fps}fps)")


def play_video(path):
    """Read the video back frame-by-frame and display it."""
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError(f"Could not open video: {path}")

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # end of video
        frame_count += 1
        cv2.imshow("Video Playback", frame)
        # Press 'q' to quit early, otherwise ~20fps playback
        if cv2.waitKey(50) & 0xFF == ord("q"):
            break

    print(f"Total frames read: {frame_count}")
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if not os.path.exists(VIDEO_PATH):
        create_sample_video(VIDEO_PATH)
    play_video(VIDEO_PATH)
