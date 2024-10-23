import streamlit as st
from PIL import Image

# CSS for dark blue background
st.markdown(
    """
    <style>
    .stApp {
        background-color: #00008B;  /* Dark Blue color */
        color: white;  /* Change text color to white for better contrast */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create multiple tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home","Resume", "Job Search", "Saved", "Help"])

with tab1: 

    # Custom CSS to change the title font color to white without affecting the background
    st.markdown("""
    <style>
    h1 {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

    # Open and display an image from your local directory
    image = Image.open('role_ready_logo.png') 
    st.image(image, caption='This is a local image.', use_column_width=True)




