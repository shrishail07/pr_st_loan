import streamlit as st
from supabase_client import supabase


# 1. MUST BE FIRST STREAMLIT COMMAND: Set layout configuration
st.set_page_config(page_title="Education Loan Platform", layout="wide")

# =====================================================================
# PREMIUM THEMING AND VISIBILITY LAYOUT (CSS)
# =====================================================================
st.markdown("""
    <style>
        /* Modern App Background */
        .stApp {
            background-color: #0F172A !important; /* Premium Midnight Dark Blue */
        }
        
        /* Master Text and Headers Styling */
        h1, h2, h3, label, p, .stTabs [data-baseweb="tab"] {
            color: #F8FAFC !important; /* Ultra clean off-white text */
            font-weight: 600 !important;
        }
        
        /* Center Title Style Adjustment */
        .main h1 {
            text-align: center !important;
            margin-bottom: 20px !important;
            font-size: 2.2rem !important;
            letter-spacing: 0.5px !important;
        }

        /* Style Streamlit Tabs Bar */
        .stTabs [data-baseweb="tab-list"] {
            gap: 10px !important;
            background-color: transparent !important;
            justify-content: center !important;
        }

        .stTabs [data-baseweb="tab"] {
            background-color: #1E293B !important;
            border: 1px solid #334155 !important;
            padding: 10px 30px !important;
            border-radius: 8px 8px 0px 0px !important;
            font-size: 16px !important;
            transition: all 0.2s ease !important;
        }

        /* Active Tab Accent Styling */
        .stTabs [aria-selected="true"] {
            background-color: #38BDF8 !important; /* Clean Sky Blue Accent */
            color: #0F172A !important;
            border-color: #38BDF8 !important;
        }

        /* Content Panel/Card under the tabs */
        .stTabs [data-testid="stVerticalBlock"] > div {
            background-color: #1E293B !important; /* Polished Dashboard Dark Card */
            padding: 25px !important;
            border-radius: 12px !important;
            border: 1px solid #334155 !important;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4) !important;
        }

        /* UNIVERSAL INPUT BOX VISIBILITY FIX */
        div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important; /* Locked to clean white background */
            color: #0F172A !important; /* Rich charcoal text color (Zero blank visibility traps) */
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            height: 45px !important;
            font-size: 16px !important;
            font-weight: 500 !important;
        }

        /* AUTHENTICATION ACTION BUTTONS */
        div.stButton > button {
            background-color: #38BDF8 !important; /* Bright Sky Blue */
            color: #0F172A !important; /* Solid dark text label */
            font-weight: 700 !important;
            font-size: 16px !important;
            width: 100% !important;
            height: 45px !important;
            border-radius: 8px !important;
            border: none !important;
            margin-top: 15px !important;
            cursor: pointer !important;
            transition: all 0.2s ease-in-out !important;
        }

        /* Button Hover Feedback Actions */
        div.stButton > button:hover {
            background-color: #0EA5E9 !important; /* Darker vibrant blue on hover */
            box-shadow: 0 4px 12px rgba(14, 165, 233, 0.4) !important;
            transform: translateY(-1px) !important;
        }
        
        div.stButton > button:active {
            transform: translateY(1px) !important;
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Set the width exactly to 300 pixels
    st.image("pages/logo.png", width=1500)

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
