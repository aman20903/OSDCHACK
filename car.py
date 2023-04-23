import cv2
import streamlit as st
import os

# Load the pre-trained car classifier file
car_cascade = cv2.CascadeClassifier('cars.xml')

# Add a title to the Streamlit webpage
st.title("Car Detection Using OpenCV")

# Create a file uploader widget
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi"])

# Check if a video file was uploaded
if video_file is not None:
    # Read the contents of the video file
    video_bytes = video_file.read()

    # Save the video to a temporary file
    with open("temp_video.mp4", "wb") as f:
        f.write(video_bytes)

    # Create a placeholder for the video
    video_placeholder = st.empty()

    # Open the video file using VideoCapture
    cap = cv2.VideoCapture("temp_video.mp4")

    # Loop through the frames of the video
    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Check if the frame was successfully captured
        if not ret:
            break

        # Convert the frame from BGR to RGB format
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect cars in the frame
        cars = car_cascade.detectMultiScale(rgb_frame, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the detected cars
        for (x, y, w, h) in cars:
            cv2.rectangle(rgb_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame in the Streamlit window
        video_placeholder.image(rgb_frame, channels="RGB")

    # Release the VideoCapture object and delete the temporary file
    cap.release()
    os.remove("temp_video.mp4")