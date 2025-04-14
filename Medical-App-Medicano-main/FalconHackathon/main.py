import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
import time  # Import the time module for adding delay

# Set page config FIRST — before any Streamlit UI components
st.set_page_config(
    page_title="Medicano",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import your internal modules
import Blogs, Home, Alternatives, DiagnoseDisease, MedicineInformation, NearbyPharmacies, Ambulance, About_Contact
from PillRemainder import app as PillReminderApp
from auth import register_user, login_user

# ---------------- Session Setup ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "popup_shown" not in st.session_state:
    st.session_state.popup_shown = False
if "popup_message" not in st.session_state:
    st.session_state.popup_message = ""

# ---------------- Header ----------------
st.markdown("<h1 style='text-align: center;'>💊 Welcome to <span style='color:#4a4aff;'>Medicano</span></h1>", unsafe_allow_html=True)

# ---------------- Login / Register Section ----------------
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Register"])

    with tab1:
        st.markdown("### 👤 Login to your account")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            username = st.text_input("👨‍⚕️ Username", placeholder="Enter your username")
            password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")

            if st.button("🚪 Login"):
                success, user = login_user(username, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.username = user["username"]
                    st.success("🎉 Login successful!")
                    rain(emoji="💊", font_size=30, falling_speed=5, animation_length="medium")
                    st.rerun()
                else:
                    st.error("❌ Invalid credentials. Please try again.")

    with tab2:
        st.markdown("### 🆕 Create a new account")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            new_username = st.text_input("👤 Username", key="reg_username", placeholder="Choose a username")
            new_email = st.text_input("📧 Email", key="reg_email", placeholder="Enter your email")
            new_password = st.text_input("🔐 Password", type="password", key="reg_password", placeholder="Create a password")
            confirm_password = st.text_input("🔐 Confirm Password", type="password", key="reg_confirm", placeholder="Re-enter your password")

            if st.button("✅ Register"):
                if new_password != confirm_password:
                    st.warning("⚠️ Passwords do not match!")
                elif len(new_password) < 6:
                    st.warning("⚠️ Password should be at least 6 characters.")
                else:
                    success, msg = register_user(new_username, new_email, new_password)
                    if success:
                        st.session_state.popup_message = "✅ Registration successful!"
                        st.session_state.popup_shown = True
                        st.session_state.username = new_username  # Set the username for the session
                    else:
                        st.error("❌ " + msg)

# ---------------- Show Registration Success Pop-up ----------------
if st.session_state.popup_shown:
    # Display the pop-up
    st.markdown(f"""
        <style>
            .popup {{
                background-color: #4CAF50; /* Correct background color */
                color: white;
                border-radius: 10px;
                padding: 20px;
                font-size: 16px;
                display: flex;
                flex-direction: column;
                align-items: center;
                position: fixed;
                top: 40%;
                left: 50%;
                transform: translate(-50%, -40%);
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            }}
            .popup button {{
                background-color: #fff;
                color: #4CAF50;
                border: none;
                padding: 10px 20px;
                margin-top: 10px;
                cursor: pointer;
                font-size: 14px;
                border-radius: 5px;
            }}
            .popup button:hover {{
                background-color: #e0e0e0;
            }}
        </style>
        <div class="popup">
            <h3>{st.session_state.popup_message}</h3>
            <p>Please click below to log in.</p>
            <button onclick="window.location.href='?popup_shown=False';">Login Now</button>
        </div>
    """, unsafe_allow_html=True)

    # Wait for 2-3 seconds before hiding the pop-up and proceeding
    time.sleep(3)  # Add a delay of 3 seconds
    st.session_state.popup_shown = False  # Hide the pop-up after the delay
    st.experimental_rerun()  # Trigger a rerun to show the login page

# ---------------- Load App if Logged In ----------------
if st.session_state.logged_in:

    class MultiApp:
        def __init__(self):
            self.apps = []

        def add_apps(self, title, function):
            self.apps.append({"title": title, "function": function})

        def run(self):
            titles = [app['title'] for app in self.apps]

            with st.sidebar:
                st.markdown(f"👋 Logged in as **{st.session_state.username}**")

                if st.button("🚪 Logout"):
                    st.session_state.logged_in = False
                    st.session_state.username = ""
                    st.rerun()

                app_title = option_menu(
                    menu_title='Medicano',
                    options=titles,
                    icons=['house-fill', 'heart-pulse', 'capsule', 'info-circle', 'journal-text',
                           'geo-alt', 'exclamation-triangle-fill', 'bell', 'activity'],
                    menu_icon='chat-text-fill',
                    default_index=0,
                    styles={
                        "container": {"padding": "5!important", "background-color": 'white'},
                        "icon": {"color": "black", "font-size": "23px"},
                        "nav-link": {
                            "color": "black", "font-size": "20px", "text-align": "left", "margin": "0px",
                            "--hover-color": "#000066"
                        },
                        "nav-link-selected": {"background-color": "white"}
                    }
                )

            selected_app = next((app for app in self.apps if app['title'] == app_title), None)
            if selected_app:
                selected_app['function']()

    # Initialize and Add Apps
    Medical = MultiApp()
    Medical.add_apps("Home", Home.Homes.app)
    Medical.add_apps("Diagnose Disease", lambda: DiagnoseDisease.Diagnose().app())
    Medical.add_apps("Medicine Alternatives", lambda: Alternatives.Alternatives().app())
    Medical.add_apps("Medicine Information", lambda: MedicineInformation.Information().app())
    Medical.add_apps("Nearby Pharmacies", lambda: NearbyPharmacies.Pharmacies().app())
    Medical.add_apps("Blogs", lambda: Blogs.Blogs().app())
    Medical.add_apps("Emergency Ambulance", lambda: Ambulance.AmbulanceFinder().app())
    Medical.add_apps("Pill Reminder", PillReminderApp)  # No .app() needed here
    Medical.add_apps("About&Contact", lambda: About_Contact.app())  # Make sure About_Contact has app()

    # Run Selected App
    Medical.run()  
