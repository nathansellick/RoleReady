# pip install streamlit_tags

# Import packages
import streamlit as st
from PIL import Image
from streamlit_tags import st_tags

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

# Initialize session state for projects if not already initialized
if 'projects' not in st.session_state:
    st.session_state.projects = []

# Initialize session state for projects if not already initialized
if 'certifications' not in st.session_state:
    st.session_state.certifications = []

# Initialize session state for skills if not already initialized
if 'skills' not in st.session_state:
    st.session_state.skills = []



# Create multiple tabs for application
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
                experience['work_period'] = st.text_input("", experience['work_period'], key=f"work_period_{index}")
                
                st.markdown('<span style="color: white;">Location</span>', unsafe_allow_html=True)
                experience['location'] = st.text_input("", experience['location'], key=f"location_{index}")
                
            with col2:
                st.markdown('<span style="color: white;">Job Description</span>', unsafe_allow_html=True)
                experience['job_description'] = st.text_area("", experience['job_description'], key=f"job_description_{index}")

            if st.button(f"Remove Work Experience {index + 1}", key=f"remove_work_exp_{index}"):
                st.session_state.work_experiences.pop(index)
                st.experimental_rerun()  # Refresh the app to reflect the removal

        # Button to add new work experience
        if st.button("Add Work Experience"):
            st.session_state.work_experiences.append({
                "job_title": "",
                "company": "",
                "work_period": "",
                "location": "",
                "job_description": ""
            })
            st.experimental_rerun()  # Refresh the app to reflect the addition
    
    st.markdown('<h2 style="color: white;">Education</h2>', unsafe_allow_html=True)

    # Create a collapsible section for Education
    with st.expander("Add Education", expanded=True):
        for index, education in enumerate(st.session_state.education_entries):
           
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

    st.markdown('<h2 style="color: white;">Projects</h2>', unsafe_allow_html=True)

    with st.expander("Add Projects", expanded=True):

        for index, project in enumerate(st.session_state.projects):
            # Heading for each project e.g. project 1, project 2
            st.markdown(f'<h4 style="color: white;">Project {index + 1}</h4>', unsafe_allow_html=True)

            # Display labels in white and input fields below
            st.markdown('<span style="color: white;">Project Title</span>', unsafe_allow_html=True)
            project['project_title'] = st.text_input("", project.get('project_title', ''), key=f"project_title_{index}")

            st.markdown('<span style="color: white;">Period</span>', unsafe_allow_html=True)
            project['project_period'] = st.text_input("", project.get('project_period', ''), key=f"project_period_{index}")

            st.markdown('<span style="color: white;">Desciption</span>', unsafe_allow_html=True)
            project['project_description'] = st.text_input("", project.get('project_description', ''), key=f"project_description_{index}")

            if st.button(f"Remove Project {index + 1}", key=f"remove_project{index}"):
                st.session_state.projects.pop(index)
                st.experimental_rerun()  # Refresh the app to reflect the removal

        # Button to add new project
        if st.button("Add Project"):
            st.session_state.projects.append({
                "project_title": "",
                "project_period": "",
                "project_description": ""
            })
            st.experimental_rerun()  # Refresh the app to reflect the addition

    
    st.markdown('<h2 style="color: white;">Certifications</h2>', unsafe_allow_html=True)

    with st.expander("Add Certifications", expanded=True):

        for index, certification in enumerate(st.session_state.certifications):
            # Heading for each project e.g. project 1, project 2
            st.markdown(f'<h4 style="color: white;">Certification {index + 1}</h4>', unsafe_allow_html=True)

            # Display labels in white and input fields below
            st.markdown('<span style="color: white;">Certification Title</span>', unsafe_allow_html=True)
            certification['certification_title'] = st.text_input("", certification.get('certification_title', ''), key=f"certification_title_{index}")


            if st.button(f"Remove Certification {index + 1}", key=f"remove_certification{index}"):
                st.session_state.certifications.pop(index)
                st.experimental_rerun()  # Refresh the app to reflect the removal

        # Button to add new project
        if st.button("Add Certication"):
            st.session_state.certifications.append({
                "certification_title": ""
            })
            st.experimental_rerun()  # Refresh the app to reflect the addition


    
    


    st.markdown('<h2 style="color: white;">Skills</h2>', unsafe_allow_html=True)

    with st.expander("Add Skills", expanded=True):
    

        # Use st_tags to create an input field for adding skills
        skills = st_tags(
            label='',
            text='Add a skill...',
            value=st.session_state.skills,  # Pre-populate with existing skills
            suggestions=[],  # You can add skill suggestions if needed
            maxtags=10,  # Limit to 10 skills (optional)
            key='skills_input'
        )

        # Store the skills back into the session state after modification
        st.session_state.skills = skills

        # Display the skills in a tag format
        if st.session_state.skills:
            st.markdown('<h4 style="color: white;">Your Skills:</h4>', unsafe_allow_html=True)
            for skill in st.session_state.skills:
                st.markdown(f'<span style="display:inline-block; background-color:#0072B2; color:white; padding:5px 10px; border-radius:5px; margin:5px;">{skill}</span>', unsafe_allow_html=True)

with tab3:
    st.markdown('<h2 style="color: white;">Matched Job</h2>', unsafe_allow_html=True)

    # Simulated scraped data (replace with your actual scraped data)
    job_data = {
        "job_title": "Software Engineer",
        "company": "Tech Innovations Inc.",
        "location": "New York, NY",
        "job_description": """
            As a Software Engineer at Tech Innovations Inc., you will be responsible for developing and maintaining high-quality software solutions. 
            Your key responsibilities will include:
            - Collaborating with cross-functional teams to define, design, and ship new features.
            - Writing clean, maintainable code following best practices.
            - Participating in code reviews and providing constructive feedback.
        """,
        "requirements": [
            "Bachelor's degree in Computer Science or a related field.",
            "Proficiency in Python, JavaScript, or similar programming languages.",
            "Strong problem-solving skills and attention to detail."
        ],
        "salary": "$80,000 - $100,000 per year",
        "application_link": "http://example.com/apply"
    }

    # Create a tab for Job Details
    with st.expander("Job Details", expanded=True):
      

        # Job title and company information
        st.markdown(f"<h2 style='color: white;'>{job_data['job_title']}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='color: white;'>{job_data['company']} - {job_data['location']}</h4>", unsafe_allow_html=True)

        # Job description
        st.markdown("<h3 style='color: white;'>Job Description</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{job_data['job_description']}</p>", unsafe_allow_html=True)

        # Requirements
        st.markdown("<h3 style='color: white;'>Requirements</h3>", unsafe_allow_html=True)
        st.markdown(
            "<ul style='color: white;'>" +
            "".join(f"<li>{req}</li>" for req in job_data['requirements']) +
            "</ul>",
            unsafe_allow_html=True
        )

        # Salary
        st.markdown("<h3 style='color: white;'>Salary</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color: white;'>{job_data['salary']}</p>", unsafe_allow_html=True)

        # Application link
        st.markdown("<h3 style='color: white;'>Apply Here</h3>", unsafe_allow_html=True)
        st.markdown(f"<a href='{job_data['application_link']}' target='_blank' style='color: white;'>Click to Apply</a>", unsafe_allow_html=True)

     # Buttons with icons for additional functionality
    st.markdown("---")  # Divider line for visual separation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.button("🤖 Generate CV")
    with col2:
        st.button("💾 Save Job")
    with col3:
        st.button("➡️ Next Job")
