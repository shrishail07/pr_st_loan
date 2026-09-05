import streamlit as st
from supabase_client import supabase
st.markdown(
    '<div style="background-color: #e8f4f8; padding: 10px; border-left: 5px solid #29b6f6; border-radius: 4px;">'
    '<span style="font-size: 20px; font-weight: bold; color: #C71585;">'
    'Please fill Your Details For Loan Approval.....'
    '</span>'
    '</div>', 
    unsafe_allow_html=True
)
if not st.session_state.get('authenticated'):
    st.warning("Please log in from the main page.")
    st.stop()

st.set_page_config(layout="wide")
st.info("Student Profile & Parent details")

# --- INJECT CUSTOM PURPLE & WHITE FORM STYLE ---
st.markdown("""
    <style>
        /* 1. Target the specific form container background */
        div[data-testid="stForm"] {
            background-color: #4B0082 !important; /* Deep Indigo/Purple */
            padding: 25px !important;
            border-radius: 12px !important;
            border: 2px solid #00F0FF !important; /* Premium Cyan Border */
        }
        
        /* 2. Target text headers and labels to stand out */
        div[data-testid="stForm"] p, 
        div[data-testid="stForm"] h3, 
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] span {
            color: #FFFFFF !important; /* Crystal White Text */
            font-weight: bold !important;
        }

        /* 3. Style standard text/number inputs to match the clean design */
        div[data-testid="stForm"] input {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border-radius: 6px !important;
        }

        /* COMPLETE FIX FOR THE SELECT/DROPDOWN BOX */
        div[data-testid="stForm"] div[data-baseweb="select"] > div {
            background-color: #FFFFFF !important; /* Fixed background container to white */
            border: 1px solid #00F0FF !important; /* Matches theme accents */
            border-radius: 6px !important;
        }
        
        /* Force text inside the dropdown selection element to black */
        div[data-testid="stForm"] div[data-baseweb="select"] * {
            color: #000000 !important;
        }
        
        /* 4. Brand New Styled Submit Button */
        div[data-testid="stForm"] button {
            background-color: #00F0FF !important; /* Electric Cyan background */
            border: none !important; 
            width: 100% !important; 
            color: #000000 !important; /* High contrast black text */
            border-radius: 8px !important;
            padding: 10px 0px !important;
            transition: all 0.3s ease !important;
        }

        /* FORCE ALL INNER BUTTON TEXT ELEMENTS TO BLACK */
        div[data-testid="stForm"] button * {
            color: #000000 !important; 
            font-weight: bold !important;
            font-size: 16px !important;
        }
        
        /* Button hover effect - darkens smoothly on cursor hover */
        div[data-testid="stForm"] button:hover {
            background-color: #00C2CC !important; /* Deeper turquoise feedback */
            box-shadow: 0 0 10px #00F0FF !important; /* Futuristic outer glow */
        }
        div[data-testid="stForm"] button:hover * {
            color: #000000 !important;
        }
    </style>
""", unsafe_allow_html=True)




st.divider()

# --- SECTION 2: STUDENT AND PARENT PROFILE FOR LOAN ---
st.warning("Loan Application Profile")

with st.form("student_loan_form"):
    st.subheader("Student Academic Details")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        board    = st.selectbox("Board of Education", ["CBSE", "ICSE", "State Board"])
        marks_10 = st.number_input("10th Class Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
    with s_col2:
        marks_12 = st.number_input("12th Class Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
        cet_rank = st.number_input("CET / ComedK Ranking", min_value=1, step=1)

    st.subheader("Parent/Guardian Financial Details")
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        parent_name = st.text_input("Name of Parent/Guardian")
        salary = st.number_input("Monthly Salary (₹)", min_value=0, step=5000)
    with p_col2:
        business_income = st.number_input("Business Annual Income (₹)", min_value=0, step=10000)
        agriculture_income = st.number_input("Agriculture Annual Income (₹)", min_value=0, step=10000)

    submit_application = st.form_submit_button("Submit Loan Application Profile")
    
    if submit_application:
        payload = {
            "user_id": st.session_state['user_id'],
            # "dream_university": dream_univ,
            # "target_college": target_college,
            # "target_department": target_dept,
            "board": board,
            "marks_10th": marks_10,
            "marks_12th": marks_12,
            "cet_rank": cet_rank,
            "parent_name": parent_name,
            "parent_monthly_salary": salary,
            "parent_annual_business": business_income,
            "parent_annual_agriculture": agriculture_income
        }
        try:
            # Assuming you have a 'loan_applications' table in Supabase
            supabase.table("loan_applications").insert(payload).execute()
            st.success("Loan profile submitted successfully to the admin dashboard!")
        except Exception as e:
            st.error(f"Failed to submit application: {e}")
