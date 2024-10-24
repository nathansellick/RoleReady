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
    # Create two columns, one for Work Experience and the other for Education
    col1, col2, col3, col4, col5 = st.columns(5)

    # Work Experience Section (in first column)
    with col1:
        st.markdown('<p class="work-experience-header">Work Experience</p>', unsafe_allow_html=True)

        # Initialize session state for work experiences if it doesn't exist
        if 'work_experiences' not in st.session_state:
            st.session_state.work_experiences = []  # List to hold work experience data

        # Function to display work experience fields and remove button
        def display_work_experience(index):
            st.markdown(f'<p class="subheader">Work Experience {index}</p>', unsafe_allow_html=True)
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
            new_index = len(st.session_state.work_experiences) + 1
            new_experience = display_work_experience(new_index)  # Display new entry
            st.session_state.work_experiences.append(new_experience)  # Append new experience

    # Education Section (in second column)
    with col2:
        st.markdown('<p class="education-header">Education</p>', unsafe_allow_html=True)

        # Initialize session state for education if it doesn't exist
        if 'education_entries' not in st.session_state:
            st.session_state.education_entries = []  # List to hold education entries

        # Function to display education fields and remove button
        def display_education(index):
            st.markdown(f'<p class="subheader">Education {index}</p>', unsafe_allow_html=True)
            degree = st.text_input(f"Degree {index}", placeholder="Enter your degree", key=f"degree_{index}")
            institution = st.text_input(f"Institution {index}", placeholder="Enter your institution", key=f"institution_{index}")
            graduation_year = st.text_input(f"Graduation Year {index}", placeholder="Enter your graduation year", key=f"graduation_year_{index}")

            # Button to remove the specific education entry
            if st.button(f"Remove Education {index}", key=f"remove_education_{index}"):
                st.session_state.education_entries.pop(index - 1)  # Remove entry from the list
                st.experimental_rerun()  # Rerun the app to refresh the display

            return (degree, institution, graduation_year)

        # Display all education entries from session state
        for i in range(len(st.session_state.education_entries)):
            display_education(i + 1)  # Display existing education entries

        # Button to add more education entries
        if st.button("Add Education"):
            new_index = len(st.session_state.education_entries) + 1
            new_education = display_education(new_index)  # Display new entry
            st.session_state.education_entries.append(new_education)  # Append new education

   # Skills Section (in the third column)
    with col3:
        st.markdown('<p class="skills-header">Skills</p>', unsafe_allow_html=True)

        # Initialize session state for skills if it doesn't exist
        if 'skills' not in st.session_state:
            st.session_state.skills = []  # List to hold skills

        # Function to display skill fields and remove button
        def display_skill(index):
            st.markdown(f'<p class="subheader">Skill {index}</p>', unsafe_allow_html=True)
            skill_name = st.text_input(f"Skill {index}", placeholder="Enter your skill", key=f"skill_{index}")

            # Button to remove the specific skill
            if st.button(f"Remove Skill {index}", key=f"remove_skill_{index}"):
                st.session_state.skills.pop(index - 1)  # Remove entry from the list
                st.experimental_rerun()  # Rerun the app to refresh the display

            return skill_name

        # Display all skills from session state
        for i in range(len(st.session_state.skills)):
            display_skill(i + 1)  # Display existing skills

        # Button to add more skills
        if st.button("Add Skill"):
            new_index = len(st.session_state.skills) + 1
            new_skill = display_skill(new_index)  # Display new entry
            st.session_state.skills.append(new_skill)  # Append new skill

    # Projects Section (in the fourth column)
    with col4:
        st.markdown('<p class="projects-header">Projects</p>', unsafe_allow_html=True)

        # Initialize session state for projects if it doesn't exist
        if 'projects' not in st.session_state:
            st.session_state.projects = []  # List to hold project entries

        # Function to display project fields and remove button
        def display_project(index):
            st.markdown(f'<p class="subheader">Project {index}</p>', unsafe_allow_html=True)
            project_title = st.text_input(f"Project Title {index}", placeholder="Enter your project title", key=f"project_title_{index}")
            project_description = st.text_area(f"Project Description {index}", placeholder="Describe your project", key=f"project_description_{index}")

            # Button to remove the specific project entry
            if st.button(f"Remove Project {index}", key=f"remove_project_{index}"):
                st.session_state.projects.pop(index - 1)  # Remove entry from the list
                st.experimental_rerun()  # Rerun the app to refresh the display

            return (project_title, project_description)

        # Display all projects from session state
        for i in range(len(st.session_state.projects)):
            display_project(i + 1)  # Display existing project entries

        # Button to add more projects
        if st.button("Add Project"):
            new_index = len(st.session_state.projects) + 1
            new_project = display_project(new_index)  # Display new entry
            st.session_state.projects.append(new_project)  # Append new project

    # Certificates Section (in the fifth column)
    with col5:
        st.markdown('<p class="certificates-header">Certificates</p>', unsafe_allow_html=True)

        # Initialize session state for certificates if it doesn't exist
        if 'certificates' not in st.session_state:
            st.session_state.certificates = []  # List to hold certificate entries

        # Function to display certificate fields and remove button
        def display_certificate(index):
            st.markdown(f'<p class="subheader">Certificate {index}</p>', unsafe_allow_html=True)
            certificate_title = st.text_input(f"Certificate Title {index}", placeholder="Enter your certificate title", key=f"certificate_title_{index}")
            institution = st.text_input(f"Institution {index}", placeholder="Enter the issuing institution", key=f"institution_cert_{index}")
            year = st.text_input(f"Year {index}", placeholder="Enter the year received", key=f"year_cert_{index}")

            # Button to remove the specific certificate entry
            if st.button(f"Remove Certificate {index}", key=f"remove_certificate_{index}"):
                st.session_state.certificates.pop(index - 1)  # Remove entry from the list
                st.experimental_rerun()  # Rerun the app to refresh the display

            return (certificate_title, institution, year)

        # Display all certificates from session state
        for i in range(len(st.session_state.certificates)):
            display_certificate(i + 1)  # Display existing certificate entries

        # Button to add more certificates
        if st.button("Add Certificate"):
            new_index = len(st.session_state.certificates) + 1
            new_certificate = display_certificate(new_index)  # Display new entry
            st.session_state.certificates.append(new_certificate)  # Append new certificate


