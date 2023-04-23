import cv2
import streamlit as st

def detect_faces(video_stream):
    # Create a face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Loop over frames in the video stream
    while True:
        # Read a frame from the video stream
        ret, frame = video_stream.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw bounding boxes around the detected faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Return the output frame as an image
        return frame

def main():
    # Create a video capture object
    video_stream = cv2.VideoCapture(0)

    # Create a Streamlit window
    st.title('Face Detection App')

    # Loop over frames in the video stream and display the output
    while True:
        # Get the output image
        output_frame = detect_faces(video_stream)

        # Display the output image in the Streamlit window
        st.image(output_frame, channels='BGR')

if __name__ == '__main__':
    main()
