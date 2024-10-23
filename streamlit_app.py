# Import packages
import streamlit as st
from PIL import Image

# CSS for dark blue background and tab styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #00008B;  /* Dark Blue color for background */
        color: white;  /* Change text color to white for better contrast */
    }

    /* Tabs container styling - centering tabs */
    div[data-testid="stTabs"] {
        display: flex;
        justify-content: center;  /* Center the tabs */
    }

    /* Tabs button styling */
    div[data-testid="stTabs"] button {
        color: white;  /* Tab text color */
        background-color: #1E90FF;  /* Light blue background for tabs */
        border: 1px solid #FFFFFF;  /* White border around tabs */
        padding: 10px 20px;  /* Uniform padding to make tabs equal size */
        flex-grow: 1;  /* Ensures tabs have equal width */
        max-width: 150px;  /* Set a max width for each tab */
        text-align: center;  /* Center the text inside the tab */
    }

    /* Active tab styling */
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #FFFFFF;  /* White background for active tab */
        color: #00008B;  /* Dark blue text color for active tab */
    }

    /* Hover effect on tabs */
    div[data-testid="stTabs"] button:hover {
        background-color: #FFFFFF;  /* White background on hover */
        color: #00008B;  /* Dark blue text color on hover */
    }

    /* Custom style for the Create an Account text */
    .account-header {
        color: white;  /* Change the color of the Create an Account text to white */
        font-size: 20px;  /* Adjust font size as necessary */
        font-weight: bold;  /* Make the text bold for emphasis */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create multiple tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Resume", "Job Search", "Saved", "Help"])

with tab1:
    # Center-align the image with Streamlit layout
    image = Image.open('role_ready_logo.png') 
    st.image(image, width=800, use_column_width='always')  # Use column width to keep it centered

    # Create an Account section
    st.markdown('<p class="account-header">Create an Account</p>', unsafe_allow_html=True)

    # Input fields for username and password
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", placeholder="Enter your password", type="password")

    # Optional: Button to submit the form
    if st.button("Create Account"):
        st.success(f"Account created for {username}!")
