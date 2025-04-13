import sys
import os
import numpy as np
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predict import predict_pcos

def app():
    st.title("🩺 PCOS Prediction")

    st.markdown("Enter the following health details:")

 
    hcg_i = st.number_input("I β-HCG (mIU/mL)", min_value=0.0)
    hcg_ii = st.number_input("II β-HCG (mIU/mL)", min_value=0.0)
    amh = st.number_input("AMH (ng/mL)", min_value=0.0)

    if st.button("🔍 Predict"):
        features = np.array([[ hcg_i, hcg_ii, amh]])
        result = predict_pcos(features)

        if result == 1:
            st.error("⚠️ You might have PCOS. Please consult a gynecologist.")
        else:
            st.success("✅ You are unlikely to have PCOS.")
