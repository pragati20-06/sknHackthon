import streamlit as st

# Import your data functions
try:
    from data_file import data_fetcher, find_correlation, indiavix_data_fetcher, show_predictions
except ImportError:
    st.error("Please make sure data_file.py is in the correct path")
    data_fetcher = None
    find_correlation = None
    indiavix_data_fetcher = None
    show_predictions = None

def app():
    # Security check - redirect if not logged in
    if not st.session_state.get("logged_in", False):
        st.warning("⚠️ Please login to access this page.")
        st.session_state.current_page = "login"
        st.rerun()
        return
    
    # Display welcome message
    st.title(f"📈 Stock Market Dashboard")
    st.subheader(f"Welcome, {st.session_state.get('email', 'User')}!")

    # Sidebar navigation
    with st.sidebar:
        st.subheader("🌐 Navigation")
        
        if st.button("🏠 Home", use_container_width=True):
            st.session_state.active_page = "home"
        
        if st.button("📊 Stock Analysis", use_container_width=True):
            st.session_state.active_page = "stock_analysis"
        
        if st.button("🔗 Find Correlation", use_container_width=True):
            st.session_state.active_page = "find_correlation"
        
        if st.button("🔮 Show Predictions", use_container_width=True):
            st.session_state.active_page = "show_predictions"
        
        st.divider()
        st.write(f"📧 Logged in as: {st.session_state.get('email', 'Unknown')}")
        
        if st.button("🚪 Logout", use_container_width=True):
            # Clear session state
            st.session_state.logged_in = False
            st.session_state.current_page = "login"
            st.session_state.email = ""
            st.rerun()
    
    # Initialize active page if not set
    if "active_page" not in st.session_state:
        st.session_state.active_page = "home"
    
    # Page content based on selection
    try:
        if st.session_state.active_page == "home":
            st.subheader("📊 Current India VIX Data")
            if indiavix_data_fetcher and hasattr(indiavix_data_fetcher, 'display_vix_data'):
                indiavix_data_fetcher.display_vix_data()
            else:
                st.info("VIX data display function not available")
        
        elif st.session_state.active_page == "stock_analysis":
            st.subheader("📈 Stock Analysis")
            if data_fetcher and hasattr(data_fetcher, 'app'):
                data_fetcher.app()
            else:
                st.info("Stock analysis function not available")
        
        elif st.session_state.active_page == "find_correlation":
            st.subheader("🔗 Find Correlation")
            if find_correlation and hasattr(find_correlation, 'app'):
                find_correlation.app()
            else:
                st.info("Correlation function not available")
        
        elif st.session_state.active_page == "show_predictions":
            st.subheader("🔮 Show Predictions")
            if show_predictions and hasattr(show_predictions, 'app'):
                show_predictions.app()
            else:
                st.info("Predictions function not available")
    except Exception as e:
        st.error(f"Error loading page: {e}")
    
    # Display logo if you have pages.py with logo
    try:
        from apps.pages import display_logo
        display_logo()
    except:
        pass
