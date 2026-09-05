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
