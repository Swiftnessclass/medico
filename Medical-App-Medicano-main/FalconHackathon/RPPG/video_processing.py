import cv2
import numpy as np
import time

def process_video():
    # Start capturing video from webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise Exception("Could not open video device")
    
    # Set the resolution of the video
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # List to store frames for analysis
    frames = []

    # Time duration for video processing (seconds)
    duration = 10  # Capture 10 seconds of video

    start_time = time.time()
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Collect frames for the specified duration
        frames.append(frame)

        # Display video frame
        cv2.imshow("Video Capture - Press 'q' to exit", frame)

        # Break the loop after 'duration' seconds
        if time.time() - start_time > duration:
            break

        # Wait for the 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

    # Process frames and return the result (Placeholder for now)
    heart_rate = analyze_heart_rate(frames)
    return heart_rate

def analyze_heart_rate(frames):
    # Placeholder for heart rate analysis (RPPG Algorithm)
    # You would replace this with your heart rate calculation method
    # Here, it's just a dummy value
    return 72  # Dummy heart rate value in beats per minute
