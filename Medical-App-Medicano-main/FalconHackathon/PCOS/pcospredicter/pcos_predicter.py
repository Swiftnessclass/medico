import sys
import os
import numpy as np
import streamlit as st
import joblib

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Load the trained model and scaler
model_path = os.path.join(os.path.dirname(__file__), '..', 'pcos_model', 'pcos_model.pkl')
scaler_path = os.path.join(os.path.dirname(__file__), '..', 'pcos_model', 'scaler.pkl')

model = joblib.load(os.path.abspath(model_path))
scaler = joblib.load(os.path.abspath(scaler_path))

def predict_pcos(features):
    """
    Predict whether the patient has PCOS based on input features.
    Scales the features and uses the trained model for prediction.
    """
    # Scale the features using the saved scaler
    features_scaled = scaler.transform(features)
    
    # Predict using the model
    prediction = model.predict(features_scaled)
    
    # Return prediction result: 1 if positive for PCOS, 0 otherwise
    return prediction[0]

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

        - Age: Age of the person.
        - BMI: Body Mass Index.
        - Menstrual Irregularity: Whether there is any menstrual irregularity (1 = Yes, 0 = No).
        - **Testosterone Level**: The level of testosterone in ng/dL.
        - **Antral Follicle Count**: The number of antral follicles in the ovaries.

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
        age = st.number_input("Age", min_value=0, max_value=100, help="Enter your age")
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, help="Enter your BMI")
        menstrual_irregularity = st.selectbox("Menstrual Irregularity", [0, 1], help="1 = Yes, 0 = No")
        testosterone_level = st.number_input("Testosterone Level (ng/dL)", min_value=0.0, max_value=200.0, help="Enter testosterone level")
        antral_follicle_count = st.number_input("Antral Follicle Count", min_value=0, max_value=50, help="Enter the number of antral follicles")

        # Prediction button
        if st.button("🔍 Predict"):
            # Check if any value is invalid (less than or equal to 0)
            if age <= 0 or bmi <= 0 or testosterone_level <= 0 or antral_follicle_count <= 0:
                st.warning("Please enter valid values for all fields to proceed with the prediction.")
            else:
                # Prepare features for prediction
                features = np.array([[age, bmi, menstrual_irregularity, testosterone_level, antral_follicle_count]])
                result = predict_pcos(features)

                # Show results based on the prediction
                if result == 1:
                    st.error("⚠️ You might have PCOS. Please consult a gynecologist.")
                else:
                    st.success("✅ You are unlikely to have PCOS.")

    # Styling for the app (optional)
    st.markdown("""
    <style>
    .custom-container {
        background-color: #F3F4F6;
        padding: 20px;
        border-radius: 8px;
        box-shadow: none; /* Remove any visual "depth" */
    }

    h1 {
        font-size: 32px;
        font-weight: bold;
        color: #2C3E50;
    }

    p, label, .stMarkdown, .stNumberInput, .stSelectbox {
        font-size: 16px !important;
        color: #34495E !important;
   
        filter: none !important;
    }

    /* Removes any blur from focused input fields */
    input:focus, select:focus, textarea:focus {
        backdrop-filter: none !important;
        filter: none !important;
        outline: 2px solid #2980B9;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Footer (optional)
    st.markdown("""
    <footer style="text-align: center; padding: 20px;">
        <p style="font-size: 14px; color: #BDC3C7;">Made with ❤️ by the Medical Team | <a href="https://example.com" style="color: #2980B9;">Learn More</a></p>
    </footer>
    """, unsafe_allow_html=True)
