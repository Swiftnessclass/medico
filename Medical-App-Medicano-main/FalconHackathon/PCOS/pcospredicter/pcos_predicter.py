import sys
import os
import numpy as np
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.predict import predict_pcos

def app():
    # Set a title for the app
    st.title("🩺 PCOS Prediction")

    # Use session state to track the button click
    if 'start_clicked' not in st.session_state:
        st.session_state.start_clicked = False

    # Display instructions and Start Prediction button only if the button has not been clicked
    if not st.session_state.start_clicked:
        st.markdown("""
        ## Instructions

        This tool helps predict whether you might have Polycystic Ovary Syndrome (PCOS) based on certain health markers. 
        Enter the following values:

        - **I β-HCG (mIU/mL)**: A hormone produced during pregnancy or conditions related to PCOS.
        - **II β-HCG (mIU/mL)**: Another form of the HCG hormone, typically elevated in PCOS.
        - **AMH (ng/mL)**: Anti-Müllerian Hormone, which can be indicative of ovarian reserve.

        After entering the values, click **Start Prediction** to receive your result.
        """)

        # Add a button to start the prediction
        if st.button("🔍 Start Prediction"):
            st.session_state.start_clicked = True  # Mark that the button has been clicked
            st.experimental_rerun()  # Rerun the app to refresh the UI and hide the instructions and the button

    # Once the button is clicked, show the input fields for health details
    if st.session_state.start_clicked:
        st.subheader("Enter the following health details:")

        # Input fields for health details
        hcg_i = st.number_input("I β-HCG (mIU/mL)", min_value=0.0, format="%.2f", help="Enter the I β-HCG value")
        hcg_ii = st.number_input("II β-HCG (mIU/mL)", min_value=0.0, format="%.2f", help="Enter the II β-HCG value")
        amh = st.number_input("AMH (ng/mL)", min_value=0.0, format="%.2f", help="Enter the AMH value")

        # Prediction button
        if st.button("🔍 Predict"):
            if hcg_i == 0 or hcg_ii == 0 or amh == 0:
                st.warning("Please enter all values to proceed with the prediction.")
            else:
                # Prepare features for prediction
                features = np.array([[hcg_i, hcg_ii, amh]])
                result = predict_pcos(features)

                # Show results based on the prediction
                if result == 1:
                    st.error("⚠️ You might have PCOS. Please consult a gynecologist.")
                else:
                    st.success("✅ You are unlikely to have PCOS.")

    # Styling for the app (optional)
    st.markdown("""
    <style>
    .css-1v0mbdj { 
        background-color: #F3F4F6; 
        padding: 20px; 
        border-radius: 8px;
    }
    .css-1v0mbdj h1 { 
        font-size: 32px;
        font-weight: bold;
        color: #2C3E50;
    }
    .css-1v0mbdj p { 
        font-size: 16px;
        color: #34495E;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Footer (optional)
    st.markdown("""
    <footer style="text-align: center; padding: 20px;">
        <p style="font-size: 14px; color: #BDC3C7;">Made with ❤️ by the Medical Team | <a href="https://example.com" style="color: #2980B9;">Learn More</a></p>
    </footer>
    """, unsafe_allow_html=True)
