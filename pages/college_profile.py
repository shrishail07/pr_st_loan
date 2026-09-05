import streamlit as st
from supabase_client import supabase

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



with st.form("Requesting the Data from the Client for loan application..."):
        st.warning("please fill the following details to request the data from the client for the college profile and department details.")
        # Create a columns for the input fields
        university_name  = st.text_input("Enter the University Name...")
        college_name     = st.text_input("Enter the College Name...")
        about_college    = st.text_area("Enter the About College Details...")
        history          = st.text_area("Enter the History of Your College...")
        accreditations   = st.text_input("Enter the Accreditations of Your College...")

        st.info("please fill the Principal Details.....")
        principal_name   = st.text_input("Enter the Principal Name...")
        principal_email  = st.text_input("Enter the Principal Email...")
        principal_contact = st.text_input("Enter the Principal Contact Number...")

        st.info("please fill the Department Details.....")
        department_name = st.text_input("Enter the Department Name...")
        intake_year     = st.number_input("Enter the Intake Year of the department...", min_value=2000, max_value=2100, step=1)
        placement_rate  = st.number_input("Enter the Placement Rate of the department (%)...", min_value=0.0, max_value=100.0, step=0.1)
        mou_signed      = st.text_input("Enter the MOUs Signed by the department...")

        st.info("please fill the Head of the Department Details.....")
        hod_name        = st.text_input("Enter the Head of the Department Name...")
        hod_email       = st.text_input("Enter the Head of the Department Email...")
        contact_number  = st.text_input("Enter the Head of the Department Contact Number...")

        st.info("please fill the Center of Excellence and Highest Package Details.....")
        center_of_excellence  = st.text_input("Enter the Center of Excellence details...")
        highest_package       = st.number_input("Enter the Highest Package offered by the department (in LPA)...", min_value=0.0, step=0.1)

        st.info("Government Program Fee Details(in INR).....")
        program_fee_gov       = st.number_input("Enter the Government Program Fee (in INR)...", min_value=0.0, step=1000.0)
        add_on_fee            = st.number_input("Enter the Add-on Fee (in INR)...", min_value=0.0, step=1000.0)
        st.info("ComedK Program Fee Details(in INR).....")
        program_fee_comedk    = st.number_input("Enter the ComedK Program Fee (in INR)...", min_value=0.0, step=1000.0)
        add_on_fee_comedk     = st.number_input("Enter the ComedK Add-on Fee (in INR)...", min_value=0.0, step=1000.0)
        st.info("Management Program Fee Details(in INR).....")
        program_fee_mgmt      = st.number_input("Enter the Management Program Fee (in INR)...", min_value=0.0, step=1000.0)
        add_on_fee_mgmt       = st.number_input("Enter the Management Add-on Fee (in INR)...", min_value=0.0, step=1000.0) 

        # Submit button to send the data to Supabase
        if st.form_submit_button("Submit College Profile Data"):
            # Prepare the data to be sent to Supabase
            college_profile_data = {
                "university_name": university_name,
                "college_name": college_name,
                "about_college": about_college,
                "history": history,
                "accreditations": accreditations,
                "department_name": department_name,
                "intake_year": intake_year,
                "placement_rate": placement_rate,
                "mou_signed": mou_signed,
                "center_of_excellence": center_of_excellence,
                "highest_package": highest_package,
                "program_fee_gov": program_fee_gov,
                "add_on_fee": add_on_fee,
                "program_fee_comedk": program_fee_comedk,
                "add_on_fee_comedk": add_on_fee_comedk,
                "program_fee_mgmt": program_fee_mgmt,
                "add_on_fee_mgmt": add_on_fee_mgmt,
                "hod_name": hod_name,
                "hod_email": hod_email,
                "contact_number": contact_number,
                "principal_name": principal_name,
                "principal_email": principal_email,
                "principal_contact": principal_contact
            }


            try:
                # Assuming you have a 'loan_applications' table in Supabase
             supabase.table("loan_applications").insert(college_profile_data).execute()
             st.success("College profile data submitted successfully!")
            except Exception as e:
                st.error(f"Failed to submit application: {e}")







