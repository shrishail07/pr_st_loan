import os
from dotenv import load_dotenv
from supabase import create_client, Client
import streamlit as st

# Load environment variables
load_dotenv()

@st.cache_resource
def init_connection() -> Client:
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    if not url or not key:
        st.error("Supabase URL or Key is missing. Please check your .env file.")
        st.stop()
    return create_client(url, key)

supabase = init_connection()
