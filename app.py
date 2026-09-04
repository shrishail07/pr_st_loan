import streamlit as st
from supabase_client import supabase

st.set_page_config(page_title="Education Loan Platform", layout="wide")

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'user_id' not in st.session_state:
    st.session_state['user_id'] = None

def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        st.session_state['authenticated'] = True
        st.session_state['user_id'] = response.user.id
        st.success("Login successful!")
        st.rerun()
    except Exception as e:
        st.error(f"Login failed: {e}")

def signup_user(email, password):
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        st.success("Signup successful! You can now log in.")
    except Exception as e:
        st.error(f"Signup failed: {e}")

# --- PAGE 0: LOGIN / SIGNUP ---
if not st.session_state['authenticated']:
    st.title("Welcome to the Education Loan Platform")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.subheader("Login to your account")
        login_email = st.text_input("Email", key="login_email")
        login_pass = st.text_input("Password", type="password", key="login_pass")
        if st.button("Login"):
            login_user(login_email, login_pass)
            
    with tab2:
        st.subheader("Create a new account")
        signup_email = st.text_input("Email", key="signup_email")
        signup_pass = st.text_input("Password", type="password", key="signup_pass")
        if st.button("Sign Up"):
            signup_user(signup_email, signup_pass)
else:
    st.sidebar.success("You are logged in.")
    if st.sidebar.button("Logout"):
        supabase.auth.sign_out()
        st.session_state['authenticated'] = False
        st.session_state['user_id'] = None
        st.rerun()
        
    st.title("Dashboard")
    st.write("Please select a page from the sidebar to continue:")
    st.write("👉 **Alumni Investor**")
    st.write("👉 **Student Profile**")
