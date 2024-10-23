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

    /* Custom style for Work Experience header */
    .work-experience-header {
        color: white;  /* Change the color of Work Experience section */
        font-size: 18px;  /* Adjust font size */
        font-weight: bold;  /* Make the text bold */
    }

    /* Custom style for Work Experience subheaders */
    .work-experience-subheader {
        color: white;  /* Change the color of Work Experience subheaders to white */
        font-size: 16px;  /* Adjust font size */
        font-weight: bold;  /* Make the text bold */
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

with tab2:
    # Work Experience Section
    st.markdown('<p class="work-experience-header">Work Experience</p>', unsafe_allow_html=True)

    # Initialize session state for work experiences if it doesn't exist
    if 'work_experiences' not in st.session_state:
        st.session_state.work_experiences = []  # List to hold work experience data

    # Function to display work experience fields and remove button
    def display_work_experience(index):
        # Use the custom class for the subheader
        st.markdown(f'<p class="work-experience-subheader">Work Experience {index}</p>', unsafe_allow_html=True)
        role_title = st.text_input(f"Role Title {index}", placeholder="Enter your role title", key=f"role_title_{index}")
        location = st.text_input(f"Location {index}", placeholder="Enter your location", key=f"location_{index}")
        time_period = st.text_input(f"Time Period {index}", placeholder="e.g., Jan 2020 - Dec 2020", key=f"time_period_{index}")
        job_description = st.text_area(f"Job Description {index}", placeholder="Describe your job responsibilities", key=f"job_description_{index}")

        # Button to remove the specific work experience
        if st.button(f"Remove Work Experience {index}", key=f"remove_{index}"):
            st.session_state.work_experiences.pop(index - 1)  # Remove entry from the list
            st.experimental_rerun()  # Rerun the app to refresh the display

        return (role_title, location, time_period, job_description)

    # Display all work experiences from session state
    for i in range(len(st.session_state.work_experiences)):
        display_work_experience(i + 1)  # Display existing work experiences

    # Button to add more work experience
    if st.button("Add Work Experience"):
        # Collect the data from the latest experience before adding a new one
        new_index = len(st.session_state.work_experiences) + 1
        new_experience = display_work_experience(new_index)  # Display new entry
        st.session_state.work_experiences.append(new_experience)  # Append new experience
