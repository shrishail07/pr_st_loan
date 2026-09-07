import streamlit as st
from supabase_client import supabase
import pandas as pd

st.markdown(
    '<div style="background-color: #e8f4f8; padding: 10px; border-left: 5px solid #29b6f6; border-radius: 4px;">'
    '<span style="font-size: 20px; font-weight: bold; color: #005a80;">'
    'Requesting the Data from the Client ......'
    '</span>'
    '</div>', 
    unsafe_allow_html=True
)

if not st.session_state.get('authenticated'):
    st.warning("Please log in from the main page.")
    st.stop()

st.set_page_config(layout="wide")
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



# with st.form("Requesting the Data from the Client for loan application..."):
#         st.warning("please fill the following details to request the data from the client for the college profile and department details.")
#         # Create a columns for the input fields
#         university_name  = st.text_input("Enter the University Name...")
#         college_name     = st.text_input("Enter the College Name...")
#         about_college    = st.text_area("Enter the About College Details...")
#         history          = st.text_area("Enter the History of Your College...")
#         accreditations   = st.text_input("Enter the Accreditations of Your College...")

#         st.info("please fill the Principal Details.....")
#         principal_name   = st.text_input("Enter the Principal Name...")
#         principal_email  = st.text_input("Enter the Principal Email...")
#         principal_contact = st.text_input("Enter the Principal Contact Number...")

#         st.info("please fill the Department Details.....")
#         department_name = st.text_input("Enter the Department Name...")
#         intake_year     = st.number_input("Enter the Intake Year of the department...", min_value=2000, max_value=2100, step=1)
#         placement_rate  = st.number_input("Enter the Placement Rate of the department (%)...", min_value=0.0, max_value=100.0, step=0.1)
#         mou_signed      = st.text_input("Enter the MOUs Signed by the department...")

#         st.info("please fill the Head of the Department Details.....")
#         hod_name        = st.text_input("Enter the Head of the Department Name...")
#         hod_email       = st.text_input("Enter the Head of the Department Email...")
#         contact_number  = st.text_input("Enter the Head of the Department Contact Number...")

#         st.info("please fill the Center of Excellence and Highest Package Details.....")
#         center_of_excellence  = st.text_input("Enter the Center of Excellence details...")
#         highest_package       = st.number_input("Enter the Highest Package offered by the department (in LPA)...", min_value=0.0, step=0.1)

#         st.info("Government Program Fee Details(in INR).....")
#         program_fee_gov       = st.number_input("Enter the Government Program Fee (in INR)...", min_value=0.0, step=1000.0)
#         add_on_fee            = st.number_input("Enter the Add-on Fee (in INR)...", min_value=0.0, step=1000.0)
#         st.info("ComedK Program Fee Details(in INR).....")
#         program_fee_comedk    = st.number_input("Enter the ComedK Program Fee (in INR)...", min_value=0.0, step=1000.0)
#         add_on_fee_comedk     = st.number_input("Enter the ComedK Add-on Fee (in INR)...", min_value=0.0, step=1000.0)
#         st.info("Management Program Fee Details(in INR).....")
#         program_fee_mgmt      = st.number_input("Enter the Management Program Fee (in INR)...", min_value=0.0, step=1000.0)
#         add_on_fee_mgmt       = st.number_input("Enter the Management Add-on Fee (in INR)...", min_value=0.0, step=1000.0) 

#         # Submit button to send the data to Supabase
#         if st.form_submit_button("Submit College Profile Data"):
#             # Prepare the data to be sent to Supabase
#             college_profile_data = {
#                 "university_name": university_name,
#                 "college_name": college_name,
#                 "about_college": about_college,
#                 "history": history,
#                 "accreditations": accreditations,
#                 "department_name": department_name,
#                 "intake_year": intake_year,
#                 "placement_rate": placement_rate,
#                 "mou_signed": mou_signed,
#                 "center_of_excellence": center_of_excellence,
#                 "highest_package": highest_package,
#                 "program_fee_gov": program_fee_gov,
#                 "add_on_fee": add_on_fee,
#                 "program_fee_comedk": program_fee_comedk,
#                 "add_on_fee_comedk": add_on_fee_comedk,
#                 "program_fee_mgmt": program_fee_mgmt,
#                 "add_on_fee_mgmt": add_on_fee_mgmt,
#                 "hod_name": hod_name,
#                 "hod_email": hod_email,
#                 "contact_number": contact_number,
#                 "principal_name": principal_name,
#                 "principal_email": principal_email,
#                 "principal_contact": principal_contact
#             }


#             try:
#                 # Assuming you have a 'loan_applications' table in Supabase
#              supabase.table("loan_applications").insert(college_profile_data).execute()
#              st.success("College profile data submitted successfully!")
#             except Exception as e:
#                 st.error(f"Failed to submit application: {e}")

# ==========================================
# 0. Initialize Session State DataFrames
# ==========================================
if 'college_data' not in st.session_state:
    st.session_state.college_data = pd.DataFrame(columns=[
        "University Name", "College Name", "About College", "History", "Accreditations"
    ])
if 'principal_data' not in st.session_state:
    st.session_state.principal_data = pd.DataFrame(columns=[
        "Principal Name", "Principal Email", "Principal Contact"
    ])
if 'dept_data' not in st.session_state:
    st.session_state.dept_data = pd.DataFrame(columns=[
        "Department Name", "Intake Year", "Placement Rate (%)", "MOUs Signed"
    ])
if 'hod_fees_data' not in st.session_state:
    st.session_state.hod_fees_data = pd.DataFrame(columns=[
        "HOD Name", "HOD Email", "HOD Contact", "Center of Excellence", "Highest Package (LPA)",
        "Govt Fee", "Govt Add-on", "ComedK Fee", "ComedK Add-on", "Mgmt Fee", "Mgmt Add-on"
    ])

# ==========================================
# Create the 4 Tabs
# ==========================================
tab1, tab2, tab3, tab4 = st.tabs([
    "College Details", "Principal Details", "Department Details", "HOD & Fees Details"
])

# ==========================================
# TAB 1: COLLEGE DETAILS
# ==========================================
with tab1:
    st.subheader("Step 1: Enter College Details")
    with st.form("college_form", clear_on_submit=True):
        st.warning("Please fill the following details for the college profile.")
        university_name  = st.text_input("Enter the University Name...")
        college_name     = st.text_input("Enter the College Name...")
        about_college    = st.text_area("Enter the About College Details...")
        history          = st.text_area("Enter the History of Your College...")
        accreditations   = st.text_input("Enter the Accreditations of Your College...")
        
        if st.form_submit_button("Submit College Details"):
            new_data = pd.DataFrame([{
                "University Name": university_name, "College Name": college_name,
                "About College": about_college, "History": history, "Accreditations": accreditations
            }])
            st.session_state.college_data = pd.concat([st.session_state.college_data, new_data], ignore_index=True)
            st.success("College details added to table!")

    st.subheader("Step 2 & 3: View, Modify, and Save Data")
    edited_college_df = st.data_editor(st.session_state.college_data, num_rows="dynamic", key="edit_college")
    
    if st.button("Save Modified College Data"):
        st.session_state.college_data = edited_college_df
        st.success("Table updated! (Add your Supabase insert logic here)")
        # Example Supabase integration:
        # supabase.table("college_details").insert(edited_college_df.to_dict('records')).execute()


# ==========================================
# TAB 2: PRINCIPAL DETAILS
# ==========================================
with tab2:
    st.subheader("Step 1: Enter Principal Details")
    with st.form("principal_form", clear_on_submit=True):
        st.info("Please fill the Principal Details.....")
        principal_name   = st.text_input("Enter the Principal Name...")
        principal_email  = st.text_input("Enter the Principal Email...")
        principal_contact = st.text_input("Enter the Principal Contact Number...")
        
        if st.form_submit_button("Submit Principal Details"):
            new_data = pd.DataFrame([{
                "Principal Name": principal_name, "Principal Email": principal_email, "Principal Contact": principal_contact
            }])
            st.session_state.principal_data = pd.concat([st.session_state.principal_data, new_data], ignore_index=True)
            st.success("Principal details added to table!")

    st.subheader("Step 2 & 3: View, Modify, and Save Data")
    edited_principal_df = st.data_editor(st.session_state.principal_data, num_rows="dynamic", key="edit_principal")
    
    if st.button("Save Modified Principal Data"):
        st.session_state.principal_data = edited_principal_df
        st.success("Table updated!")


# ==========================================
# TAB 3: DEPARTMENT DETAILS
# ==========================================
with tab3:
    st.subheader("Step 1: Enter Department Details")
    with st.form("department_form", clear_on_submit=True):
        st.info("Please fill the Department Details.....")
        department_name = st.text_input("Enter the Department Name...")
        intake_year     = st.number_input("Enter the Intake Year of the department...", min_value=2000, max_value=2100, step=1)
        placement_rate  = st.number_input("Enter the Placement Rate of the department (%)...", min_value=0.0, max_value=100.0, step=0.1)
        mou_signed      = st.text_input("Enter the MOUs Signed by the department...")
        
        if st.form_submit_button("Submit Department Details"):
            new_data = pd.DataFrame([{
                "Department Name": department_name, "Intake Year": intake_year, 
                "Placement Rate (%)": placement_rate, "MOUs Signed": mou_signed
            }])
            st.session_state.dept_data = pd.concat([st.session_state.dept_data, new_data], ignore_index=True)
            st.success("Department details added to table!")

    st.subheader("Step 2 & 3: View, Modify, and Save Data")
    edited_dept_df = st.data_editor(st.session_state.dept_data, num_rows="dynamic", key="edit_dept")
    
    if st.button("Save Modified Department Data"):
        st.session_state.dept_data = edited_dept_df
        st.success("Table updated!")


# ==========================================
# TAB 4: HOD & FEES DETAILS
# ==========================================
with tab4:
    st.subheader("Step 1: Enter HOD, COE & Fee Details")
    with st.form("hod_fees_form", clear_on_submit=True):
        st.info("Please fill the Head of the Department Details.....")
        hod_name        = st.text_input("Enter the Head of the Department Name...")
        hod_email       = st.text_input("Enter the Head of the Department Email...")
        contact_number  = st.text_input("Enter the Head of the Department Contact Number...")

        st.info("Please fill the Center of Excellence and Highest Package Details.....")
        center_of_excellence  = st.text_input("Enter the Center of Excellence details...")
        highest_package       = st.number_input("Enter the Highest Package offered (in LPA)...", min_value=0.0, step=0.1)

        # Using columns to layout the fees neatly side-by-side
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("Government Fees")
            program_fee_gov       = st.number_input("Govt Program Fee (INR)", min_value=0.0, step=1000.0)
            add_on_fee            = st.number_input("Govt Add-on Fee (INR)", min_value=0.0, step=1000.0)
        with col2:
            st.info("ComedK Fees")
            program_fee_comedk    = st.number_input("ComedK Program Fee (INR)", min_value=0.0, step=1000.0)
            add_on_fee_comedk     = st.number_input("ComedK Add-on Fee (INR)", min_value=0.0, step=1000.0)
        with col3:
            st.info("Management Fees")
            program_fee_mgmt      = st.number_input("Mgmt Program Fee (INR)", min_value=0.0, step=1000.0)
            add_on_fee_mgmt       = st.number_input("Mgmt Add-on Fee (INR)", min_value=0.0, step=1000.0)

        if st.form_submit_button("Submit HOD & Fees Details"):
            new_data = pd.DataFrame([{
                "HOD Name": hod_name, "HOD Email": hod_email, "HOD Contact": contact_number,
                "Center of Excellence": center_of_excellence, "Highest Package (LPA)": highest_package,
                "Govt Fee": program_fee_gov, "Govt Add-on": add_on_fee,
                "ComedK Fee": program_fee_comedk, "ComedK Add-on": add_on_fee_comedk,
                "Mgmt Fee": program_fee_mgmt, "Mgmt Add-on": add_on_fee_mgmt
            }])
            st.session_state.hod_fees_data = pd.concat([st.session_state.hod_fees_data, new_data], ignore_index=True)
            st.success("HOD and Fees details added to table!")

    st.subheader("Step 2 & 3: View, Modify, and Save Data")
    edited_hod_fees_df = st.data_editor(st.session_state.hod_fees_data, num_rows="dynamic", key="edit_hod_fees")
    
    if st.button("Save Modified HOD & Fees Data"):
        st.session_state.hod_fees_data = edited_hod_fees_df
        st.success("Table updated! (Ready for final Supabase upload)")





