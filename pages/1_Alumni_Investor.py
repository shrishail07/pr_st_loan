import streamlit as st
from supabase_client import supabase

st.markdown(
    '<div style="background-color: #e8f4f8; padding: 10px; border-left: 5px solid #29b6f6; border-radius: 4px;">'
    '<span style="font-size: 20px; font-weight: bold; color: #C71585;">'
    'Alumni Investor Profile.....'
    '</span>'
    '</div>', 
    unsafe_allow_html=True
)

if not st.session_state.get('authenticated'):
    st.warning("Please log in from the main page.")
    st.stop()

st.info("Help fund the next generation of students from your alma mater.")

# --- INJECT CUSTOM PURPLE & WHITE FORM STYLE ---
st.markdown("""
    <style>
        /* 1. Target the specific form container background */
        div[data-testid="stForm"] {
            background-color: #4B0082 !important; /* Deep Indigo/Purple */
            padding: 20px !important;
            border-radius: 10px !important;
            border: none !important;
        }
        
        /* 2. Target text color inside the form to be White/dark for readability */
        div[data-testid="stForm"] p, 
        div[data-testid="stForm"] h3, 
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] span {
            color: #FFFFFF !important; /* White Text */
            font-weight: bold !important;
        }

        /* 3. Style the inputs so they stand out against purple background */
        div[data-testid="stForm"] input, 
        div[data-testid="stForm"] div[data-baseweb="select"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
        }
        
        /* 4. Target the form submit button to be white with black text */
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"] {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
            font-weight: bold !important;
            width: 100% !important; /* Optional: Makes button span full width */
        }
        
        /* Button hover effect */
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"]:hover {
            background-color: #F0F2F6 !important;
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)

with st.form("alumni_form"):
    st.subheader("Professional Details")
    
    col1, col2 = st.columns(2)
    with col1:
        college = st.text_input("College Name")
        dept = st.text_input("Department Name")
        pass_year = st.number_input("Pass Out Year", min_value=1950, max_value=2030, step=1)
        
    with col2:
        company = st.text_input("Current Company")
        salary_range = st.selectbox(
            "Salary Range (LPA)", 
            ["0-5 LPA", "5-10 LPA", "10-20 LPA", "20-30 LPA", "30+ LPA"]
        )
        
    submitted = st.form_submit_button("Save Investor Profile")
    
    if submitted:
        data = {
            "user_id": st.session_state['user_id'],
            "college_name": college,
            "department": dept,
            "passout_year": pass_year,
            "current_company": company,
            "salary_range": salary_range
        }
        try:
            # Assuming you have an 'alumni_investors' table in Supabase
            supabase.table("alumni_investors").insert(data).execute()
            st.success("Profile saved successfully!")
        except Exception as e:
            st.error(f"Error saving data: {e}")
