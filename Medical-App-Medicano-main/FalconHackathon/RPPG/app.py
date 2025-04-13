import streamlit as st
from .video_processing import process_video

def app():
    # Title for the RPPG feature
    st.title("🩺 RPPG - Remote Heart Rate Detection")

    # Button to start the video capture
    if st.button("Start RPPG"):
        with st.spinner('Processing video...'):
            # Start the video capture and analysis
            heart_rate = process_video()

        # Display the detected heart rate
        st.success(f"Heart Rate: {heart_rate} BPM")

    # Instructions for the user
    st.markdown("""
    This feature uses your webcam to remotely detect your heart rate based on 
    subtle changes in your skin tone. Please ensure you are well-lit and positioned 
    in front of the camera.
    """)
