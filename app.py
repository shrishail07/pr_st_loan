import streamlit as st
from supabase_client import supabase


# 1. MUST BE FIRST STREAMLIT COMMAND: Set layout configuration
st.set_page_config(page_title="Education Loan Platform", layout="wide")
st.markdown("""
    <style>
        /* =================================================================
           1. CORE APPLICATION BACKGROUND
           ================================================================= */
        .stApp {
            background-color: #0F172A !important; /* Premium Dark Navy */
        }
        
        /* =================================================================
           2. SIDEBAR ISOLATION (No bleed into the main screen)
           ================================================================= */
        section[data-testid="stSidebar"] {
            background-color: #FFF0F5 !important; /* Locks light pink sidebar background */
        }
        
        section[data-testid="stSidebar"] * {
            color: #1E293B !important; /* Crisp dark charcoal for sidebar links */
            font-weight: 600 !important;
        }

        /* =================================================================
           3. MAIN PANEL OVERRIDES (Titles, Forms, Labels)
           ================================================================= */
        /* Targets the grand title directly */
        div[data-testid="stHeaderBlock"] h1, 
        .main h1, 
        .main h2 {
            color: #FFFFFF !important;
            text-align: center !important;
            font-weight: 700 !important;
            letter-spacing: 0.5px !important;
        }
        
        /* Subheaders and Input Labels inside the main container */
        .main h3, 
        .main label, 
        .main p {
            color: #F1F5F9 !important; /* Clear off-white for full visibility */
            font-weight: 600 !important;
        }

        /* =================================================================
           4. STUNNING CARD NAVIGATION TABS
           ================================================================= */
        .stTabs [data-baseweb="tab-list"] {
            gap: 12px !important;
            background-color: transparent !important;
            justify-content: center !important;
            margin-bottom: -4px !important; /* Pulls container snugly up to card */
        }

        /* Dormant Tab Button Style */
        .stTabs [data-baseweb="tab"] {
            background-color: #1E293B !important;
            border: 1px solid #334155 !important;
            padding: 12px 35px !important;
            border-radius: 8px 8px 0px 0px !important;
            transition: all 0.2s ease-in-out !important;
        }

        /* Force inner text of dormant tabs to stay white */
        .stTabs [data-baseweb="tab"] * {
            color: #94A3B8 !important; /* Clean muted grey/white text */
            font-weight: 600 !important;
            font-size: 15px !important;
        }

        /* Active Tab Accent Styling */
        .stTabs [aria-selected="true"] {
            background-color: #38BDF8 !important; /* Electric Sky Blue */
            border-color: #38BDF8 !important;
        }
        
        /* Force inner text of the active tab to turn dark */
        .stTabs [aria-selected="true"] * {
            color: #0F172A !important; /* Stark contrast black text */
            font-weight: 700 !important;
        }

        /* Main Content Panel Box under the tabs */
        .stTabs [data-testid="stVerticalBlock"] > div {
            background-color: #1E293B !important; /* Polished Sleek Dashboard Card */
            padding: 30px !important;
            border-radius: 12px !important;
            border: 1px solid #334155 !important;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.4) !important;
        }

        /* =================================================================
           5. SECURE & HIGH-VISIBILITY INPUT BOXES
           ================================================================= */
        div[data-testid="stTextInput"] input {
            background-color: #FFFFFF !important; /* Crisp solid white fields */
            color: #0F172A !important; /* Deep slate font color */
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            height: 46px !important;
            font-size: 16px !important;
            font-weight: 500 !important;
        }
        
        /* Highlight input border when focused/clicked */
        div[data-testid="stTextInput"] input:focus {
            border: 2px solid #38BDF8 !important;
        }

        /* =================================================================
           6. ACTION BUTTONS (Login & Sign Up)
           ================================================================= */
        div.stButton > button {
            background-color: #38BDF8 !important; /* Vibrant Action Sky Blue */
            border: none !important;
            width: 100% !important;
            height: 46px !important;
            border-radius: 8px !important;
            margin-top: 20px !important;
            cursor: pointer !important;
            box-shadow: 0 4px 6px -1px rgba(56, 189, 248, 0.2) !important;
            transition: all 0.2s ease-in-out !important;
        }
        
        /* Button text formatting */
        div.stButton > button * {
            color: #0F172A !important; /* High contrast bold black text */
            font-weight: 700 !important;
            font-size: 16px !important;
        }

        /* Button Hover Feedback */
        div.stButton > button:hover {
            background-color: #0EA5E9 !important; /* Richer accent blue on hover */
            box-shadow: 0 10px 15px -3px rgba(14, 165, 233, 0.3) !important;
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
