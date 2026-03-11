import firebase_admin
from firebase_admin import credentials, auth
import streamlit as st

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(r"C:\Users\hp\Downloads\serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

def app():
    st.title("📝 Create New Account")

    # Input fields
    email = st.text_input("📧 Email", key="signup_email")
    password = st.text_input("🔑 Password", type="password", key="signup_password")
    confirm_password = st.text_input("🔒 Confirm Password", type="password", key="signup_confirm")

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

    with col1:
        if st.button("Create Account", key="signup_button"):
            # Validation
            if not email or not password:
                st.error("❌ Please fill all fields")
            elif password != confirm_password:
                st.error("❌ Passwords do not match.")
            elif len(password) < 6:
                st.error("❌ Password must be at least 6 characters")
            else:
                try:
                    # Create user in Firebase
                    user = auth.create_user(
                        email=email, 
                        password=password
                    )
                    st.success(f"✅ Account created successfully! Please login.")
                    
                    # Redirect to login page
                    st.session_state.current_page = "login"
                    st.rerun()
                        
                except auth.EmailAlreadyExistsError:
                    st.error("❌ Email already exists. Please login instead.")
                except Exception as e:
                    st.error(f"Error creating account: {e}")

    with col4:
        if st.button("← Back to Login", key="back_to_login"):
            st.session_state.current_page = "login"
            st.rerun()
    
    # Display logo if you have pages.py with logo
    try:
        from apps.pages import display_logo
        display_logo()
    except:
        pass
