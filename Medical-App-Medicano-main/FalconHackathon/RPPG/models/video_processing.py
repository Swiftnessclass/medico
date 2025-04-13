import streamlit as st
import cv2
import numpy as np
import time
from models.utils import extract_face_region, extract_rppg_signal, predict_stress, predict_emotion
from models.signal_extraction import compute_heart_rate, compute_respiration_rate, compute_hrv

def process_video():
    stframe = st.empty()
    cap = cv2.VideoCapture(0)
    signals, timestamps = [], []
    start_time = time.time()

    while time.time() - start_time < 20:
        ret, frame = cap.read()
        if not ret:
            break

        face = extract_face_region(frame)
        signal = extract_rppg_signal(face)

        signals.append(signal)
        timestamps.append(time.time() - start_time)
        stframe.image(frame, channels='BGR')

    cap.release()

    signals = np.array(signals)
    timestamps = np.array(timestamps)

    if len(signals) < 10:
        st.error("Insufficient signal. Ensure good lighting and sit still,camera not found")
        return None

    hr = compute_heart_rate(signals, timestamps)
    rr = compute_respiration_rate(signals, timestamps)
    hrv = compute_hrv(signals, timestamps)

    bp_sys = int(0.5 * hr + 80)
    bp_dia = int(0.33 * hr + 50)

    stress = predict_stress(hrv)
    emotion = predict_emotion(frame)

    return (
        int(hr), int(rr), 98,  # SpO2 = dummy placeholder
        stress, round(hrv, 2),
        f"{bp_sys}/{bp_dia}", emotion
    )
