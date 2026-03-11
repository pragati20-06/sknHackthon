import streamlit as st
from apps import sign_up, login, home

st.set_page_config(
    page_title="Stock Market App",
    page_icon="📈",
)

def main():
    # Initialize session state variables
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"  # Default to login page
    if "email" not in st.session_state:
        st.session_state.email = ""
    
    # Navigation logic
    if st.session_state.logged_in:
        home.app()  # Show home page if logged in
    else:
        if st.session_state.current_page == "login":
            login.app()
        elif st.session_state.current_page == "sign_up":
            sign_up.app()

if __name__ == "__main__":
    main()
