import streamlit as st
import time
from PCOS.pcospredicter.pcos_predicter import app as PCOSApp
from modules.medical import Medical  # Adjust path as needed
from RPPG.app import app as rppg_app  # Importing the RPPG app

class Homes:
    @staticmethod
    def app():
        if "back_button_clicked" not in st.session_state:
            st.session_state.back_button_clicked = False

        # CSS Styling
        st.markdown("""
        <style>
        .header-container {
            background: linear-gradient(135deg, #003366, #006699);
            border-radius: 10px;
            padding: 30px 20px;
            text-align: center;
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        .header-container h1 {
            color: white;
            font-size: 60px;
            margin-bottom: 10px;
            animation: fadeInDown 1s ease-in-out;
        }

        .header-container h2 {
            color: #e0e0e0;
            font-size: 22px;
            animation: fadeInUp 1s ease-in-out;
        }

        .stButton button {
            width: 100%;
            height: 80px;
            font-size: 24px;
            background-color: #006699;
            color: white;
            border-radius: 10px;
            border: none;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        .stButton button:hover {
            background-color: #004466;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        }

        .back-button {
            background-color: black;
            color: white;
            font-size: 16px;
            padding: 8px 16px;
            border-radius: 6px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
            cursor: pointer;
            z-index: 9999;
            margin-top: 20px;
            border: none;
            width: 40px;
            height: 0px;
        }

        .back-button:hover {
            background-color: #222;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        }
        </style>
        """, unsafe_allow_html=True)

        # Header section
        st.markdown("""
        <div class="header-container">
            <h1>Medicano</h1>
            <h2>A Smart Medical Assistant</h2>
        </div>
        """, unsafe_allow_html=True)

        # If a feature is selected
        if 'selected_feature' in st.session_state:
            if st.session_state.selected_feature == "PCOS":
                with st.spinner('Loading PCOS Prediction...'):
                    time.sleep(2)
                    PCOSApp()  # Load the PCOS Prediction App

                # Back button
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("🔙 Back", key="back_button"):
                        del st.session_state.selected_feature
                        st.experimental_rerun()

            elif st.session_state.selected_feature == "RPPG":
                with st.spinner('Loading RPPG...'):
                    time.sleep(2)
                    rppg_app()  # Load the RPPG App

                # Back button
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("🔙 Back", key="back_button"):
                        del st.session_state.selected_feature
                        st.experimental_rerun()

        else:
            # Feature buttons
            col1, col2 = st.columns(2)

            with col1:
                if st.button("🩺 RPPG", key="rppg_btn"):
                    st.session_state.selected_feature = "RPPG"  # Set selected feature as RPPG
                    st.experimental_rerun()

            with col2:
                if st.button("💊 PCOS Prediction", key="pcos_btn"):
                    st.session_state.selected_feature = "PCOS"  # Set selected feature as PCOS
                    st.experimental_rerun()
