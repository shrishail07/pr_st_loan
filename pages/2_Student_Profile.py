import streamlit as st
from supabase_client import supabase

if not st.session_state.get('authenticated'):
    st.warning("Please log in from the main page.")
    st.stop()

st.set_page_config(layout="wide")
st.title("Student Profile & Education Loan Application")

# --- SECTION 1: COLLEGE & DEPARTMENT SELECTION ---
st.header("1. Target Education")

col1, col2, col3 = st.columns(3)
with col1:
    dream_univ = st.selectbox("Choose Dream University", ["Visvesvaraya Technological University (VTU)", "Manipal Academy", "PES University"])
with col2:
    target_college = st.selectbox("Choose College", ["RVCE", "BMSCE", "MSRIT", "PDA College of Engineering", "Appa Institute"])
with col3:
    target_dept = st.selectbox("Choose Department", ["Computer Science", "Artificial Intelligence", "Electronics", "Mechanical"])

st.divider()

# --- MOCK ADMIN DATA DISPLAY ---
# In a real app, this data would be fetched from Supabase based on the selections above.
st.subheader(f"Institution Details: {target_college}")

tab_info, tab_fees = st.tabs(["Institutional Profile", "Program Fees structure"])

with tab_info:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**1. About College:** A premier institute established to provide quality technical education.")
        st.markdown("**2. History:** Founded in 1946, it has a legacy of over 75 years.")
        st.markdown("**3. Accreditations:** NAAC A++, NBA Accredited.")
        st.markdown(f"**4. Department Name:** {target_dept}")
    with col_b:
        st.markdown(f"**5. Center of Excellence:** Advanced AI & Robotics Lab.")
        st.markdown(f"**6. Placements:** 95% placement rate, Highest package 45 LPA.")
        st.markdown(f"**7. MOUs Signed:** Microsoft, Google, Pragyan Smart AI Technology LLP.")

with tab_fees:
    st.markdown("**8. Program Fee**")
    fee_col1, fee_col2, fee_col3 = st.columns(3)
    
    with fee_col1:
        st.info("🏛️ Govt Quota (CET)")
        st.metric(label="Annual Fee", value="₹1,10,000")
        st.metric(label="Add-on Fee", value="₹25,000")
        
    with fee_col2:
        st.info("📝 ComedK Quota")
        st.metric(label="Annual Fee", value="₹2,60,000")
        st.metric(label="Add-on Fee", value="₹30,000")
        
    with fee_col3:
        st.info("💼 Management Quota")
        st.metric(label="Annual Fee", value="₹4,00,000")
        st.metric(label="Add-on Fee", value="₹50,000")

st.divider()

# --- SECTION 2: STUDENT AND PARENT PROFILE FOR LOAN ---
st.header("2. Loan Application Profile")

with st.form("student_loan_form"):
    st.subheader("Student Academic Details")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        board = st.selectbox("Board of Education", ["CBSE", "ICSE", "State Board"])
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
            "dream_university": dream_univ,
            "target_college": target_college,
            "target_department": target_dept,
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
