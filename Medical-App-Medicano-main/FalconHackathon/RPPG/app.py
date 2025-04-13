import streamlit as st
from .video_processing import process_video

def app():
    # Title for the RPPG feature
    st.title("🩺 RPPG - Remote Heart Rate Detection")

    # Button to start the video capture
    if st.button("Start RPPG"):
        with st.spinner('Processing video...'):
            # Start the video capture and analysis
            heart_rate, respiration_rate, spO2, stress_level, hrv, blood_pressure, emotion = process_video()

        # Display the detected parameters
        st.success(f"Heart Rate: {heart_rate} BPM")
        st.success(f"Respiration Rate: {respiration_rate} breaths per minute")
        st.success(f"Blood Oxygen Saturation (SpO2): {spO2}%")
        st.success(f"Stress Level: {stress_level}")
        st.success(f"Heart Rate Variability (HRV): {hrv} ms")
        st.success(f"Blood Pressure Estimate: {blood_pressure} mmHg")
        st.success(f"Emotion Detected: {emotion}")

    # Instructions for the user
    st.markdown("""
    This feature uses your webcam to remotely detect your health metrics based on 
    subtle changes in your skin tone and facial expressions. Please ensure you are well-lit and positioned 
    in front of the camera for optimal results.
    
    Features:
    - **Heart Rate**: Detected remotely via your webcam.
    - **Respiration Rate**: Measures your breathing rate based on subtle skin tone changes.
    - **Blood Oxygen Saturation (SpO2)**: Estimates your blood oxygen levels.
    - **Stress Level**: Identifies signs of stress or anxiety.
    - **Heart Rate Variability (HRV)**: Assesses the variation in your heartbeat intervals.
    - **Blood Pressure Estimate**: Provides an estimate of your blood pressure.
    - **Emotion Recognition**: Detects your emotional state based on facial expressions.
    """)

