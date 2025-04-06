import streamlit as st
from ai71 import AI71
from dotenv import load_dotenv
import os

class Diagnose:
    def __init__(self):
        # loading environment variables from .env file
        load_dotenv()
        self.AI71_API_KEY = os.getenv("AI71_API_KEY")
        self.client = AI71(self.AI71_API_KEY)

    def app(self):
        options = [
            "Fever", "Cough", "Headache", "Fatigue", "Nausea", "Vomiting",
            "Sore throat", "Runny nose", "Muscle pain", "Shortness of breath"
        ]

        # Load CSS styling
        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
            html, body, [class*="css"] {
                font-family: 'Poppins', sans-serif;
            }
            .title-box {
                background: linear-gradient(to right, #00c6ff, #0072ff);
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                color: white;
                box-shadow: 0px 5px 15px rgba(0,0,0,0.2);
                margin-bottom: 30px;
            }
            .title-box h1 {
                font-size: 60px;
                margin: 0;
            }
            .title-box h2 {
                font-size: 20px;
                font-weight: 300;
                margin-top: 10px;
            }
           
            .stButton>button {
                background: linear-gradient(135deg, #00c6ff, #0072ff);
                color: white;
                padding: 0.7em 2em;
                border: none;
                border-radius: 50px;
                font-size: 16px;
                transition: 0.3s ease-in-out;
            }
            .stButton>button:hover {
                background: linear-gradient(135deg, #0072ff, #00c6ff);
                transform: scale(1.05);
            }
            .diagnosis-result h1 {
                color: #0072ff;
                margin-top: 30px;
            }
            .diagnosis-result {
                background-color: #ffffffee;
                padding: 25px;
                border-radius: 15px;
                margin-top: 20px;
            }
            
        </style>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="title-box">
            <h1>Medicano</h1>
            <h2>A Medical Assistant</h2>
        </div>
        """, unsafe_allow_html=True)

        with st.form("diagnose_form"):
            st.markdown('<div class="glass-card ">', unsafe_allow_html=True)

            symptoms = st.multiselect("🩺 Select Your Symptoms", options)
            submit_diagnose = st.form_submit_button("🔍 Diagnose")

            st.markdown('</div>', unsafe_allow_html=True)

            if submit_diagnose:
                with st.spinner("Analyzing your symptoms... 💭"):
                    prompt = (
                      f"Based on the symptoms listed: {symptoms}, please perform a detailed diagnostic analysis. "
f"Your task is to provide a comprehensive overview of the potential disease, including the following sections:\n"
f"- **Disease Name**\n"
f"- **History**\n"
f"- **Introduction**\n"
f"- **Causes**\n"
f"- **Symptoms**\n"
f"- **Side Effects**\n"
f"- **Measures to Cure (Must include this section in detail)**\n"
f"Include blog/article links where applicable. Write in markdown format."

                    )

                    response = self.client.chat.completions.create(
                        model="tiiuae/falcon-180b-chat",
                        messages=[
                            {"role": "system", "content": "You are a medical assistant."},
                            {"role": "user", "content": prompt},
                        ],
                        stream=True,
                    )

                    response_content = ""
                    for chunk in response:
                        if chunk.choices[0].delta.content:
                            response_content += chunk.choices[0].delta.content

                st.markdown('<div class="diagnosis-result">', unsafe_allow_html=True)
                st.title("🧠 Disease Diagnosis")
                st.markdown(response_content, unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    app = Diagnose()
    app.app()
