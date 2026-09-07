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
        /* =================================================================
           1. FORM CONTAINER & MASTER STYLING
           ================================================================= */
        div[data-testid="stForm"] {
            background-color: #1E293B !important; /* Deep Premium Slate/Midnight Blue */
            padding: 30px !important;
            border-radius: 16px !important;
            border: 1px solid #334155 !important; /* Elegant subtle edge definition */
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 8px 10px -6px rgba(0, 0, 0, 0.3) !important;
        }
        
        /* Force master form text labels to look crisp and clean */
        div[data-testid="stForm"] label,
        div[data-testid="stForm"] p, 
        div[data-testid="stForm"] h3 {
            color: #F8FAFC !important; /* Bright off-white text for ultimate readability */
            font-weight: 600 !important;
            letter-spacing: 0.5px !important;
            margin-bottom: 6px !important;
        }

        /* =================================================================
           2. UNIVERSAL INPUT BOX REWRITE (TEXT, NUMBERS, SELECT BOXES)
           ================================================================= */
        /* This comprehensively targets input fields, select tags, and dropdown hooks */
        div[data-testid="stForm"] input,
        div[data-testid="stForm"] div[data-baseweb="select"],
        div[data-testid="stForm"] div[data-baseweb="select"] > div,
        div[data-testid="stForm"] div[data-baseweb="input"] {
            background-color: #FFFFFF !important; /* Pure solid white backgrounds for zero contrast failure */
            border-radius: 8px !important;
            border: 1px solid #CBD5E1 !important;
            height: 42px !important;
        }

        /* HARD OVERRIDE: Absolutely forces all input text, chosen text, and values to solid black */
        div[data-testid="stForm"] input,
        div[data-testid="stForm"] div[data-baseweb="select"] *,
        div[data-testid="stForm"] div[data-baseweb="select"] span,
        div[data-testid="stForm"] div[data-baseweb="select"] div {
            color: #0F172A !important; /* Dark charcoal/black for text visibility */
            font-weight: 500 !important;
        }

        /* Fixes target stepper icons (+ and - buttons) inside number inputs */
        div[data-testid="stForm"] button[step] {
            background-color: #E2E8F0 !important;
            color: #0F172A !important;
        }

        /* =================================================================
           3. FLOATING DROPDOWN LIST FIX (BOARD OF EDUCATION DROPDOWN LIST)
           ================================================================= */
        /* Streamlit creates selection popups outside the form root. This targets them directly. */
        div[data-testid="stSelectboxVirtualDropdown"] {
            background-color: #FFFFFF !important;
            border-radius: 8px !important;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2) !important;
        }
        
        div[data-testid="stSelectboxVirtualDropdown"] li,
        div[data-testid="stSelectboxVirtualDropdown"] li * {
            color: #0F172A !important; /* Force items in the active dropdown list to black */
            font-weight: 500 !important;
            background-color: #FFFFFF !important;
        }

        /* Hover selection effect inside the choice menu */
        div[data-testid="stSelectboxVirtualDropdown"] li:hover,
        div[data-testid="stSelectboxVirtualDropdown"] li[aria-selected="true"] {
            background-color: #F1F5F9 !important; /* Elegant light slate selection tint */
        }

        /* =================================================================
           4. PREMIUM COMPLEMENTARY SUBMIT BUTTON
           ================================================================= */
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"] {
            background-color: #F59E0B !important; /* High-end Amber Gold background */
            border: none !important;
            width: 100% !important;
            padding: 12px 0px !important;
            height: auto !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            box-shadow: 0 4px 6px -1px rgba(245, 158, 11, 0.2) !important;
            margin-top: 15px !important;
            transition: all 0.2s ease-in-out !important;
        }

        /* Forces button text elements to be stark black, bold, and clear */
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"] *,
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"] span {
            color: #0F172A !important; 
            font-weight: 700 !important;
            font-size: 16px !important;
        }

        /* Smooth Interactive Hover State */
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"]:hover {
            background-color: #D97706 !important; /* Deep luxury honey-gold tone on hover */
            box-shadow: 0 10px 15px -3px rgba(217, 119, 6, 0.3) !important;
            transform: translateY(-1px) !important;
        }
        
        div[data-testid="stForm"] button[data-testid="stFormSubmitButton"]:hover * {
            color: #0F172A !important;
        }
    </style>
""", unsafe_allow_html=True)





# st.divider()

# # --- SECTION 2: STUDENT AND PARENT PROFILE FOR LOAN ---
# st.warning("Loan Application Profile")

# with st.form("student_loan_form"):
#     st.subheader("Student Academic Details")
#     s_col1, s_col2 = st.columns(2)
#     with s_col1:
#         board    = st.selectbox("Board of Education", ["CBSE", "ICSE", "State Board"])
#         marks_10 = st.number_input("10th Class Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
#     with s_col2:
#         marks_12 = st.number_input("12th Class Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
#         cet_rank = st.number_input("CET / ComedK Ranking", min_value=1, step=1)

#     st.subheader("Parent/Guardian Financial Details")
#     p_col1, p_col2 = st.columns(2)
#     with p_col1:
#         parent_name = st.text_input("Name of Parent/Guardian")
#         salary = st.number_input("Monthly Salary (₹)", min_value=0, step=5000)
#     with p_col2:
#         business_income = st.number_input("Business Annual Income (₹)", min_value=0, step=10000)
#         agriculture_income = st.number_input("Agriculture Annual Income (₹)", min_value=0, step=10000)

#     submit_application = st.form_submit_button("Submit Loan Application Profile")
    
#     if submit_application:
#         payload = {
#             "user_id": st.session_state['user_id'],
#             # "dream_university": dream_univ,
#             # "target_college": target_college,
#             # "target_department": target_dept,
#             "board": board,
#             "marks_10th": marks_10,
#             "marks_12th": marks_12,
#             "cet_rank": cet_rank,
#             "parent_name": parent_name,
#             "parent_monthly_salary": salary,
#             "parent_annual_business": business_income,
#             "parent_annual_agriculture": agriculture_income
#         }
#         try:
#             # Assuming you have a 'loan_applications' table in Supabase
#             supabase.table("loan_applications").insert(payload).execute()
#             st.success("Loan profile submitted successfully to the admin dashboard!")
#         except Exception as e:
#             st.error(f"Failed to submit application: {e}")


import pandas as pd

# 1. Initialize session state to store data across tab switches
if 'student_data' not in st.session_state:
    st.session_state.student_data = pd.DataFrame(columns=[
        "Student Name", "Father Name", "Email ID", "Phone Number", 
        "10th Board", "PUC Board", "PUC Marks (%)", "Ranking"
    ])
if 'parent_data' not in st.session_state:
    st.session_state.parent_data = pd.DataFrame(columns=[
        "Parent Name", "Monthly Salary", "Business Income", "Agriculture Income"
    ])
if 'college_data' not in st.session_state:
    st.session_state.college_data = pd.DataFrame(columns=[
        "University Name", "College Name", "Department Name", 
        "Seat Type", "College Fees/Year", "Loan Amount/Year"
    ])

# Create the 3 Tabs
tab1, tab2, tab3 = st.tabs(["Student Information", "Parents Information", "College Information"])

# ==========================================
# TAB 1: STUDENT INFORMATION
# ==========================================
with tab1:
    st.subheader("Step 1: Enter Student Details")
    with st.form("student_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            s_name = st.text_input("1. Student Name")
            email = st.text_input("3. Email ID")
            board_10 = st.text_input("5. 10th Class Board (e.g., State, CBSE)")
            puc_marks = st.number_input("7. PUC 2nd Year Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
        with col2:
            f_name = st.text_input("2. Father Name")
            phone = st.text_input("4. Phone Number")
            puc_board = st.text_input("6. PUC 2 Year Board")
            ranking = st.number_input("8. CET or COMEDK Ranking", min_value=0, step=1)
        
        submit_student = st.form_submit_button("Submit Student Info")
        
        if submit_student:
            new_data = pd.DataFrame([{
                "Student Name": s_name, "Father Name": f_name, "Email ID": email, 
                "Phone Number": phone, "10th Board": board_10, "PUC Board": puc_board, 
                "PUC Marks (%)": puc_marks, "Ranking": ranking
            }])
            st.session_state.student_data = pd.concat([st.session_state.student_data, new_data], ignore_index=True)
            st.success("Student information submitted successfully!")
    
    st.subheader("Step 2 & 3: View and Modify Table")
    # st.data_editor allows inline modification of the dataframe
    edited_student_df = st.data_editor(st.session_state.student_data, num_rows="dynamic", key="edit_student")
    if st.button("Save Modified Student Data"):
        st.session_state.student_data = edited_student_df
        st.success("Student table updated!")

# ==========================================
# TAB 2: PARENTS INFORMATION
# ==========================================
with tab2:
    st.subheader("Step 1: Enter Parents Details")
    with st.form("parent_form", clear_on_submit=True):
        p_name = st.text_input("1. Name of Parent")
        m_salary = st.number_input("2. Monthly Salary (₹)", min_value=0, step=1000)
        b_income = st.number_input("3. Business Annual Income (₹)", min_value=0, step=1000)
        a_income = st.number_input("4. Agriculture Annual Income (₹)", min_value=0, step=1000)
        
        submit_parent = st.form_submit_button("Submit Parent Info")
        
        if submit_parent:
            new_data = pd.DataFrame([{
                "Parent Name": p_name, "Monthly Salary": m_salary, 
                "Business Income": b_income, "Agriculture Income": a_income
            }])
            st.session_state.parent_data = pd.concat([st.session_state.parent_data, new_data], ignore_index=True)
            st.success("Parent information submitted successfully!")
            
    st.subheader("Step 2 & 3: View and Modify Table")
    edited_parent_df = st.data_editor(st.session_state.parent_data, num_rows="dynamic", key="edit_parent")
    if st.button("Save Modified Parent Data"):
        st.session_state.parent_data = edited_parent_df
        st.success("Parent table updated!")

# ==========================================
# TAB 3: COLLEGE INFORMATION (LOAN DETAILS)
# ==========================================
with tab3:
    st.subheader("Step 1: Enter College & Loan Details")
    with st.form("college_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            uni_name = st.text_input("1. University Name")
            dept_name = st.text_input("3. Department Name")
            college_fees = st.number_input("5. College Fees per Year (₹)", min_value=0, step=1000)
        with col2:
            college_name = st.text_input("2. College Name")
            seat_type = st.selectbox("4. Seat Type", ["Government", "Private", "Management Quota"])
            loan_amount = st.number_input("6. Loan Required per Year (₹)", min_value=0, step=1000)
        
        submit_college = st.form_submit_button("Submit College Info")
        
        if submit_college:
            new_data = pd.DataFrame([{
                "University Name": uni_name, "College Name": college_name, 
                "Department Name": dept_name, "Seat Type": seat_type, 
                "College Fees/Year": college_fees, "Loan Amount/Year": loan_amount
            }])
            st.session_state.college_data = pd.concat([st.session_state.college_data, new_data], ignore_index=True)
            st.success("College information submitted successfully!")
            
    st.subheader("Step 2 & 3: View and Modify Table")
    edited_college_df = st.data_editor(st.session_state.college_data, num_rows="dynamic", key="edit_college")
    if st.button("Save Modified College Data"):
        st.session_state.college_data = edited_college_df
        st.success("College table updated!")
