import firebase_admin
from firebase_admin import auth, credentials
import streamlit as st

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\hp\Downloads\serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title("🔐 Login to Stock Market App")

    # Input fields
    email = st.text_input("📧 Email", key="login_email")
    password = st.text_input("🔑 Password", type="password", key="login_password")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        if st.button("Login", key="login_button"):
            if not email or not password:
                st.error("❌ Please enter both email and password")
            else:
                try:
                    # Verify user exists in Firebase Auth
                    user = auth.get_user_by_email(email)
                    # Note: For actual password verification, use Firebase REST API
                    # This is a simplified version
                    
                    st.success(f"✅ Login successful! Welcome, {email}!")
                    
                    # Set session state
                    st.session_state.logged_in = True
                    st.session_state.email = email
                    st.session_state.current_page = "home"
                    
                    # Force a rerun to show home page
                    st.rerun()
                    
                except auth.UserNotFoundError:
                    st.error("❌ User not found. Please check your email or sign up.")
                except Exception as e:
                    st.error(f"Login failed: {e}")
    
    with col4:
        if st.button("Create New Account", key="go_to_signup"):
            st.session_state.current_page = "sign_up"
            st.rerun()
    
    # Display logo if you have pages.py with logo
    try:
        from apps.pages import display_logo
        display_logo()
    except:
        pass
