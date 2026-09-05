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
with st.form("Requesting the Data from the Client for loan application..."):
        st.info("please fill the following details to request the data from the client for the college profile and department details.")
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







