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

# Initialize session state for work experiences if not already initialized
if 'work_experiences' not in st.session_state:
    st.session_state.work_experiences = []

# Initialize session state for education if not already initialized
if 'education_entries' not in st.session_state:
    st.session_state.education_entries = []



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
    st.markdown('<h2 style="color: white;">Work Experience</h2>', unsafe_allow_html=True)
    
    # Create a collapsible section for Work Experience
    with st.expander("Add Work Experience", expanded=True):
        for index, experience in enumerate(st.session_state.work_experiences):
            st.markdown(f'<h4 style="color: white;">Work Experience {index + 1}</h4>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                # Display labels in white and input fields below
                st.markdown('<span style="color: white;">Job Title</span>', unsafe_allow_html=True)
                experience['job_title'] = st.text_input("", experience['job_title'], key=f"job_title_{index}")
                
                st.markdown('<span style="color: white;">Company</span>', unsafe_allow_html=True)
                experience['company'] = st.text_input("", experience['company'], key=f"company_{index}")
                
                st.markdown('<span style="color: white;">Period</span>', unsafe_allow_html=True)
                experience['period'] = st.text_input("", experience['period'], key=f"period_{index}")
                
                st.markdown('<span style="color: white;">Location</span>', unsafe_allow_html=True)
                experience['location'] = st.text_input("", experience['location'], key=f"location_{index}")
                
            with col2:
                st.markdown('<span style="color: white;">Job Description</span>', unsafe_allow_html=True)
                experience['description'] = st.text_area("", experience['description'], key=f"description_{index}")

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
    
    st.markdown('<h2 style="color: white;">Education</h2>', unsafe_allow_html=True)

    # Create a collapsible section for Education
    with st.expander("Add Education", expanded=True):
        for index, education in enumerate(st.session_state.education_entries):
            # Correct the heading to reflect "Education" rather than "Work Experience"
            st.markdown(f'<h4 style="color: white;">Education {index + 1}</h4>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)

            with col1:
                # Display labels in white and input fields below
                st.markdown('<span style="color: white;">University</span>', unsafe_allow_html=True)
                education['university'] = st.text_input("", education.get('university', ''), key=f"university_{index}")

                st.markdown('<span style="color: white;">Degree</span>', unsafe_allow_html=True)
                education['degree'] = st.text_input("", education.get('degree', ''), key=f"degree_{index}")

            with col2:
                st.markdown('<span style="color: white;">Graduation Year</span>', unsafe_allow_html=True)
                education['graduation year'] = st.text_input("", education.get('graduation year', ''), key=f"graduation_year_{index}")

                st.markdown('<span style="color: white;">Grade</span>', unsafe_allow_html=True)
                education['grade'] = st.text_input("", education.get('grade', ''), key=f"grade_{index}")

            # Add the Remove Education button
            if st.button(f"Remove Education {index + 1}", key=f"remove_education_{index}"):
                st.session_state.education_entries.pop(index)
                st.experimental_rerun()  # Refresh the page to reflect the removal

        # Button to add new education entry
        if st.button("Add Education"):
            st.session_state.education_entries.append({
                "university": "",
                "degree": "",
                "graduation year": "",
                "grade": ""
            })
            st.experimental_rerun()  # Refresh the page to reflect the addition