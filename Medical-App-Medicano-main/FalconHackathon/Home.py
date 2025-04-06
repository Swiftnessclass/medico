import streamlit as st

class Homes:
    @staticmethod
    def app():
        # Custom CSS for aesthetic enhancements
        st.markdown("""
        <style>
        body {
            background-color: #f0f2f6;
        }
        .header-container {
            background: linear-gradient(135deg, #003366, #006699);
            border-radius: 10px;
            padding: 30px 20px;
            text-align: center;
            margin-bottom: 20px;
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
        @keyframes fadeInDown {
            0% { opacity: 0; transform: translateY(-20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .section {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .section h2 {
            color: #003366;
            font-size: 28px;
            margin-bottom: 10px;
        }
        .section p, .section li {
            font-size: 16px;
            line-height: 1.6;
            color: #333333;
        }
        </style>
        """, unsafe_allow_html=True)

        # Header
        st.markdown("""
        <div class="header-container">
            <h1>Medicano</h1>
            <h2>A Smart Medical Assistant</h2>
        </div>
        """, unsafe_allow_html=True)

        # Welcome title
        st.title("👋 Welcome to Medicano")

        # About Section
        st.markdown("""
        <div class="section">
            <h2>About Medicano</h2>
            <p>
                Medicano is a comprehensive mobile application designed to help users make informed decisions about their health. From understanding your medicines to checking availability and discovering better alternatives — we’ve got it covered.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Features Section
        st.markdown("""
        <div class="section">
            <h2>Key Features</h2>
            <ul>
                <li><strong>🧾 Detailed Medicine Info:</strong> Know what you consume — uses, ingredients, and side effects.</li>
                <li><strong>🔄 Alternative Options:</strong> Find safer or more affordable alternatives based on your needs.</li>
                <li><strong>📍 Local Availability:</strong> Instantly check which nearby pharmacies have your meds in stock.</li>
                <li><strong>📰 Health News:</strong> Get fresh updates and trending health articles.</li>
                <li><strong>🎯 Personalized Suggestions:</strong> Tailored medicine suggestions based on your health profile.</li>
                <li><strong>🎙 Voice Search:</strong> Search with ease using your voice.</li>
                <li><strong>💡 Symptom Checker:</strong> Describe your symptoms and get instant treatment insights.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Team Section
        st.markdown("""
        <div class="section">
            <h2>Meet Our Team</h2>
            <ul>
                <li><strong>Ahmad Raza</strong> – CEO & Lead Developer</li>
                <li><strong>Flap</strong> – Co-founder & UI/UX Designer</li>
                <li><strong>Mobarak</strong> – Co-founder & Backend Developer</li>
                <li><strong>Arslan</strong> – Co-founder & Idea Specialist</li>
                <li><strong>Kolmax</strong> – Co-founder & Presenter</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Contact Section
        st.markdown("""
        <div class="section">
            <h2>Contact Us</h2>
            <p>
                For inquiries or feedback, feel free to reach out to us at 
                <a href="mailto:sktfscm21557034@gmail.com">sktfscm21557034@gmail.com</a>.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Footer
        st.markdown("""
        <div style="text-align:center; color: #888; font-size: 14px; margin-top: 30px;">
            © 2024 Medicano. All rights reserved.
        </div>
        """, unsafe_allow_html=True)
