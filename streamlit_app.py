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

    /* Custom style for Work Experience header */
    .work-experience-header {
        color: white;  /* Change the color of Work Experience section */
        font-size: 18px;  /* Adjust font size */
        font-weight: bold;  /* Make the text bold */
    }

    /* Custom style for Education header */
    .education-header {
        color: white;  /* Change the color of Education section */
        font-size: 18px;  /* Adjust font size */
        font-weight: bold;  /* Make the text bold */
    }

    /* Custom style for Work Experience and Education subheaders */
    .subheader {
        color: white;  /* Change the color of subheaders to white */
        font-size: 16px;  /* Adjust font size */
        font-weight: bold;  /* Make the text bold */
    }
    </style>
    """,
    unsafe_allow_html=True
)

def styled_header(title, css_class="header"):
    st.markdown(f'<p class="{css_class}">{title}</p>', unsafe_allow_html=True)

# Initialize session state for work experiences if not already initialized
if 'work_experiences' not in st.session_state:
    st.session_state.work_experiences = []


# Create multiple tabs
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Home", "Resume", "Job Search", "Saved", "Help", "Resume develop"])

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
    st.header("Work Experience")
    
    # Create a collapsible section for Work Experience
    with st.expander("Add Work Experience", expanded=True):
        for index, experience in enumerate(st.session_state.work_experiences):
            st.subheader(f"Work Experience {index + 1}")
            col1, col2 = st.columns(2)
            with col1:
                experience['job_title'] = st.text_input("Job Title", experience['job_title'], key=f"job_title_{index}")
                experience['company'] = st.text_input("Company", experience['company'], key=f"company_{index}")
                experience['period'] = st.text_input("Period", experience['period'], key=f"period_{index}")
                experience['location'] = st.text_input("Location", experience['location'], key=f"location_{index}")
            with col2:
                experience['description'] = st.text_area("Job Description", experience['description'], key=f"description_{index}")

            if st.button(f"Remove Work Experience {index + 1}", key=f"remove_{index}"):
                st.session_state.work_experiences.pop(index)
                st.experimental_rerun()  # Refresh the app to reflect the removal

        # Button to add new work experience
        if st.button("Add Work Experience"):
            st.session_state.work_experiences.append({
                "job_title": "",
                "company": "",
                "period": "",
                "location": "",
                "description": ""
            })
            st.experimental_rerun()  # Refresh the app to reflect the addition

