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


import streamlit as st
import pandas as pd

# Dummy Supabase client setup (Replace with your actual Supabase init)
# from supabase import create_client, Client
# supabase: Client = create_client("YOUR_SUPABASE_URL", "YOUR_SUPABASE_KEY")

def upload_to_supabase(uploaded_file, bucket_name, file_name):
    """
    Placeholder for Supabase storage upload logic.
    Uncomment the actual supabase lines when integrating.
    """
    if uploaded_file is not None:
        try:
            # bytes_data = uploaded_file.getvalue()
            # supabase.storage.from_(bucket_name).upload(file_name, bytes_data)
            # public_url = supabase.storage.from_(bucket_name).get_public_url(file_name)
            # return public_url
            
            # Returning a dummy URL for demonstration purposes
            return f"https://supabase.project.co/storage/v1/object/public/{bucket_name}/{file_name}"
        except Exception as e:
            st.error(f"Upload failed: {e}")
            return None
    return None

# 1. Initialize session state for all 5 tabs
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
if 'kyc_data' not in st.session_state:
    st.session_state.kyc_data = pd.DataFrame(columns=[
        "Student Aadhaar", "College ID", "Parent Aadhaar", "Parent PAN",
        "Total Loan/Year", "Fee Utilization", "Books/Laptop/Materials", "Skill Program", "Miscellaneous"
    ])
if 'bank_data' not in st.session_state:
    st.session_state.bank_data = pd.DataFrame(columns=[
        "Selected Banks"
    ])

# Create 5 Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Student Information", "Parents Information", "College Information", "KYC & Breakout", "Bank Selection"
])

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
            loan_amount_college = st.number_input("6. Loan Required per Year (₹)", min_value=0, step=1000)
        
        submit_college = st.form_submit_button("Submit College Info")
        
        if submit_college:
            new_data = pd.DataFrame([{
                "University Name": uni_name, "College Name": college_name, 
                "Department Name": dept_name, "Seat Type": seat_type, 
                "College Fees/Year": college_fees, "Loan Amount/Year": loan_amount_college
            }])
            st.session_state.college_data = pd.concat([st.session_state.college_data, new_data], ignore_index=True)
            st.success("College information submitted successfully!")
            
    st.subheader("Step 2 & 3: View and Modify Table")
    edited_college_df = st.data_editor(st.session_state.college_data, num_rows="dynamic", key="edit_college")
    if st.button("Save Modified College Data"):
        st.session_state.college_data = edited_college_df
        st.success("College table updated!")

# ==========================================
# TAB 4: KYC & LOAN BREAKOUT
# ==========================================
with tab4:
    st.subheader("Step 1: KYC Documents & Loan Breakout")
    with st.form("kyc_form", clear_on_submit=True):
        st.info("Upload KYC Documents (Images will be saved to Supabase)")
        
        # File Uploaders
        s_aadhaar = st.file_uploader("1. Student Aadhaar Card Image", type=['png', 'jpg', 'jpeg'])
        c_id = st.file_uploader("2. College ID Card Image", type=['png', 'jpg', 'jpeg'])
        p_aadhaar = st.file_uploader("3. Parent Aadhaar Card Image", type=['png', 'jpg', 'jpeg'])
        p_pan = st.file_uploader("4. Parent PAN Card Image", type=['png', 'jpg', 'jpeg'])
        
        st.info("Loan Details & Breakout")
        loan_amt_kyc = st.number_input("5. How much loan amount you want per year?", min_value=0, step=1000)
        
        st.write("6. Loan Breakout (Should sum up to total loan amount)")
        col1, col2 = st.columns(2)
        with col1:
            fee_utilize = st.number_input("College fee utilization (₹)", min_value=0, step=1000)
            materials = st.number_input("Books, laptop, other materials (₹)", min_value=0, step=1000)
        with col2:
            skill_prog = st.number_input("Skill program cost (₹)", min_value=0, step=1000)
            misc = st.number_input("Miscellaneous (₹)", min_value=0, step=1000)

        submit_kyc = st.form_submit_button("Submit KYC & Breakout")
        
        if submit_kyc:
            # Upload logic for Supabase (Placeholder outputs used here)
            bucket = "kyc_documents"
            s_aadhaar_url = upload_to_supabase(s_aadhaar, bucket, f"student_aadhaar_{s_aadhaar.name}") if s_aadhaar else "Not Uploaded"
            c_id_url = upload_to_supabase(c_id, bucket, f"college_id_{c_id.name}") if c_id else "Not Uploaded"
            p_aadhaar_url = upload_to_supabase(p_aadhaar, bucket, f"parent_aadhaar_{p_aadhaar.name}") if p_aadhaar else "Not Uploaded"
            p_pan_url = upload_to_supabase(p_pan, bucket, f"parent_pan_{p_pan.name}") if p_pan else "Not Uploaded"
            
            new_kyc = pd.DataFrame([{
                "Student Aadhaar": s_aadhaar_url, "College ID": c_id_url,
                "Parent Aadhaar": p_aadhaar_url, "Parent PAN": p_pan_url,
                "Total Loan/Year": loan_amt_kyc, "Fee Utilization": fee_utilize,
                "Books/Laptop/Materials": materials, "Skill Program": skill_prog,
                "Miscellaneous": misc
            }])
            
            st.session_state.kyc_data = pd.concat([st.session_state.kyc_data, new_kyc], ignore_index=True)
            st.success("KYC documents uploaded to Supabase and Breakout saved!")

    st.subheader("Step 2 & 3: View and Modify KYC Table")
    edited_kyc_df = st.data_editor(st.session_state.kyc_data, num_rows="dynamic", key="edit_kyc")
    if st.button("Save Modified KYC Data"):
        st.session_state.kyc_data = edited_kyc_df
        st.success("KYC & Breakout table updated!")

# ==========================================
# TAB 5: BANK SELECTION
# ==========================================
with tab5:
    st.subheader("Step 1: Select Banks for Loan")
    with st.form("bank_form", clear_on_submit=True):
        st.info("You can select multiple banks.")
        bank_options = ["PSU banks", "Private banks", "NBFC banks", "Peer loan"]
        selected_banks = st.multiselect("Select Bank Type(s)", bank_options)
        
        submit_banks = st.form_submit_button("Submit Bank Selection")
        
        if submit_banks:
            # Join multiple selections into a single string for table display
            banks_str = ", ".join(selected_banks)
            new_banks = pd.DataFrame([{"Selected Banks": banks_str}])
            
            st.session_state.bank_data = pd.concat([st.session_state.bank_data, new_banks], ignore_index=True)
            st.success("Bank selection saved!")

    st.subheader("Step 2 & 3: View and Modify Bank Table")
    edited_bank_df = st.data_editor(st.session_state.bank_data, num_rows="dynamic", key="edit_bank")
    if st.button("Save Modified Bank Data"):
        st.session_state.bank_data = edited_bank_df
        st.success("Bank selection table updated!")
# ==========================================
# TAB 6: ADMIN DASHBOARD (Approvals)
# ==========================================
with tab6:
    st.header("Admin Panel: Loan Approvals")
    st.write("Review incoming applications and update their approval status below.")
    
    # Configure the 'Application Status' column to act as a Dropdown
    edited_admin_df = st.data_editor(
        st.session_state.admin_data,
        column_config={
            "Application Status": st.column_config.SelectboxColumn(
                "Approval Status",
                help="Select the current status of the loan application",
                options=["Pending", "Approved", "Rejected"],
                required=True
            ),
            "Total Loan Requested": st.column_config.NumberColumn(
                "Total Loan Requested (₹)",
                format="₹ %d"
            )
        },
        hide_index=True,
        num_rows="dynamic",
        key="admin_editor"
    )
    
    if st.button("Save Admin Status Changes"):
        # Save the updated statuses back to session state (or push to Supabase)
        st.session_state.admin_data = edited_admin_df
        
        # Example Supabase update logic:
        # for index, row in edited_admin_df.iterrows():
        #     supabase.table("loan_applications").update({"status": row["Application Status"]}).eq("student_name", row["Student Name"]).execute()
            
        st.success("Application statuses updated successfully!")
