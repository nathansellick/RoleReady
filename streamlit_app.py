# pip install streamlit_tags

# Import packages
import pandas as pd
import os
import openai
import json
import subprocess
import psycopg2
import datetime
import streamlit as st
import atexit
from find_core_job_details import *
from PIL import Image
from streamlit_tags import st_tags
from dotenv import load_dotenv
from streamlit import session_state as state

# Load the environment variables from the .env file
load_dotenv()

# Get the current date
current_date = datetime.date.today()

# Retrieve the environment variables
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
APIKEY = os.getenv('APIKEY')

# Now you can use the loaded environment variables to connect to your database
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

client = openai.OpenAI(api_key = APIKEY)


# Setup Chrome options to disable popups and redirections
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Defining functions

def get_completion(prompt, model="gpt-4o-mini", temperature=0):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature = temperature
    )
    return response.choices[0].message.content

def insert_user(username: str, password: str):
    """
    insert new username and password into PostgreSQL database
    """
    # Parameterized query to prevent SQL injection
    sql_query = '''
    INSERT INTO users (user_name, user_password)
    VALUES (%s, %s)
    '''
    cursor = conn.cursor()
    cursor.execute(sql_query, (username, password))
    conn.commit()  # Commit the transaction
    st.success(f"Account created for {username}!")
    cursor.close() # closes cursor object

def insert_work_exp_entry(user_id: int, work_experience: dict):
    """
    Function inserts inputted work experience information for user into database
    """
    user_id = st.session_state['user_id']
    insert_query = """
    INSERT INTO work_experiences(user_id, job_title, company, start_date, end_date, city, country, job_description)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(insert_query, (user_id, work_experience['job_title'], work_experience['company'], work_experience['start_date'], work_experience['end_date'],work_experience['city'],
                                  work_experience['country'],work_experience['job_description']))
    conn.commit()
    cursor.close()

def insert_education_entry(user_id: int, education: dict):
    """
    Function inserts inputted education information for user into database
    """
    user_id = st.session_state['user_id']
    insert_query = """
    INSERT INTO education(user_id, university, degree, graduation_year, grade)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(insert_query, (user_id, education['university'], education['degree'], education['grad_year'], education['grade']))
    conn.commit()
    cursor.close()

def insert_project_entry(user_id: int, project: dict):
    """
    Function inserts inputted project information for user into database
    """
    user_id = st.session_state['user_id']
    insert_query = """
    INSERT INTO projects(user_id, start_date, end_date, description)
    VALUES (%s, %s, %s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(insert_query, (user_id, project['start_date'], project['end_date'], project['description']))
    conn.commit()
    cursor.close()

def insert_certification_entry(user_id: int, certification: dict):
    """
    Function inserts inputted certifications for user into database
    """
    user_id = st.session_state['user_id']
    insert_query = """
    INSERT INTO certifications(user_id, certificate)
    VALUES (%s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(insert_query, (user_id, certification['title']))
    conn.commit()
    cursor.close()

def insert_skills_query(user_id: int, skills_list: list):
    # Convert the Python list to the PostgreSQL array format
    skills_array = '{' + ','.join(f'"{skill}"' for skill in skills_list) + '}'
    insert_query = """
    INSERT INTO skills(user_id, skill)
    VALUES (%s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET skill = EXCLUDED.skill
    """
    cursor = conn.cursor()
    cursor.execute(insert_query,(user_id, skills_array))
    conn.commit()
    cursor.close()

def save_job_query(user_id: int, job_dic: dict):
    insert_query_1 = """
    INSERT INTO jobs(job_title, company_name, location, salary, employment_type, job_description, company_rating, link_to_application)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """
    insert_query_2 = """
    INSERT INTO users_jobs(user_id, saved_date)
    VALUES(%s, %s)
    """
    cursor = conn.cursor()
    cursor.execute(insert_query_1, (job_dic['job_title'], job_dic['company'], job_dic['location'], job_dic['salary'], job_dic['employment_type'],
                                    st.session_state['job_desc_summary'], job_dic['company_rating'], job_dic['application_link']))
    cursor.execute(insert_query_2, (user_id, current_date))
    conn.commit()
    cursor.close()

def display_job_details():
    job_dic = st.session_state['job_dic']
    job_description = job_dic['job_description']
    job_description_prompt = f"""
    In 200 words and In a single paragraph, summarise the job post, including all the important details such as company, position, pay, location, projects, skills and tools required. 
    The job post is provided below, delimited by 3 backticks.
    ```{job_description}```
    """
    job_desc_summary = get_completion(job_description_prompt)
    st.session_state['job_desc_summary'] = job_desc_summary


    with st.expander("Job Details", expanded=True):
        
            
            # Job Title
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Job Title</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: white; font-weight: normal;'>{job_dic['job_title']}</h3>", unsafe_allow_html=True)

            # Company
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Company</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: white; font-weight: normal;'>{job_dic['company']}</h3>", unsafe_allow_html=True)
        
            #Location 
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Location</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: white; font-weight: normal;'>{job_dic['location']}</h3>", unsafe_allow_html=True)
            
            # Employment type
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Employment Type</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: white; font-weight: normal;'>{job_dic['employment_type']}</h3>", unsafe_allow_html=True)
          
            # Salary
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Salary</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color: white; font-weight: normal;'>{job_dic['salary']}</h3>", unsafe_allow_html=True)

            #Job description
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Job Description</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='color: white;'>{job_desc_summary}</p>", unsafe_allow_html=True)
            #st.markdown(f"<p style='color: white;'>{job_dic['job_description']}</p>", unsafe_allow_html=True)
            
            # Application link
            st.markdown("<h2 style='color: lightgrey; font-weight: bold; text-decoration: underline;'>Apply Here</h2>", unsafe_allow_html=True)
            st.markdown(f"<a href='{job_dic['application_link']}' target='_blank' style='color: white;'>{job_dic['application_link']}</a>", unsafe_allow_html=True)




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

# Custom CSS to style the labels
st.markdown("""
    <style>
        /* Change the color of labels to white */
        .stTextInput label {
            color: white !important;
        }
        .stPasswordInput label {
            color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for work experiences if not already initialized
if 'work_experiences' not in st.session_state:
    st.session_state.work_experiences = {}

# Initialize session state for education if not already initialized
if 'education_entries' not in st.session_state:
    st.session_state.education_entries = {}

# Initialize session state for projects if not already initialized
if 'projects' not in st.session_state:
    st.session_state.projects = {}

# Initialize session state for projects if not already initialized
if 'certifications' not in st.session_state:
    st.session_state.certifications = {}

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
    st.markdown("<h2 style='color: white;'>Create an Account</h2>", unsafe_allow_html=True)

    # Input fields for username and password
    username = st.text_input("Username", placeholder="Enter your username", key = "create_account_username")
    password = st.text_input("Password", placeholder="Enter your password", type="password", key = "create_account_password")

    # Button to create account and add user to PostgreSQL database
    if st.button("Create Account"):
        cursor = conn.cursor()
        select_user_count_query = """SELECT COUNT(user_name) from users 
        WHERE user_name = %s """
        cursor.execute(select_user_count_query, (username,))
        result = cursor.fetchone()
        num_of_users = result[0]
        if num_of_users == 0:
            insert_user(username, password)
        else:
            st.error("Account already exists")
    

    # Login section
    st.markdown("<h2 style='color: white;'>Login</h2>", unsafe_allow_html=True)

    # Input fields for username and password login
    username_login = st.text_input("Username", placeholder="Enter your username", key = "login_username")
    password_login = st.text_input("Password", placeholder="Enter your password", type="password", key="login_password")

    # Button to login
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Login"):
        
            # Query to authenticate the user
            login_query = '''
            SELECT user_id FROM users
            WHERE user_name = %s AND user_password = %s
            '''
            cursor = conn.cursor()
            cursor.execute(login_query, (username_login, password_login))
            result = cursor.fetchone()
            
            if result:
                # Store user_id in session state if login is successful
                state["user_id"] = result[0]
                st.success(f"Welcome back, {username_login}!")
            else:
                st.error("Invalid username or password.")
            
            cursor.close()

    with col2:
    
        if "user_id" in st.session_state:
            # Display the logout button if the user is logged in
            if st.button("Logout"):
                # Clear the session state to log out the user
                for key in st.session_state.keys():
                    del st.session_state[key]
                st.success("You have been logged out.")
                
  

with tab2:
    st.markdown('<h2 style="color: white;">Work Experience</h2>', unsafe_allow_html=True)

    # Check if the user is logged in by checking if user_id exists in session_state
    if 'user_id' in st.session_state:
        with st.expander("Add Work Experience", expanded=True):
            # Loop through each work experience entry stored in session_state
            for index, (key, work_experience) in enumerate(st.session_state.work_experiences.items()):
                st.markdown(f'<h4 style="color: white;">Work Experience {index + 1}</h4>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown('<span style="color: white;">Job Title</span>', unsafe_allow_html=True)
                    work_experience['job_title'] = st.text_input("", work_experience.get('job_title', ''), key=f"job_title_{key}")

                    st.markdown('<span style="color: white;">Start Date</span>', unsafe_allow_html=True)
                    work_experience['start_date'] = st.text_input("", work_experience.get('start_date', ''), key=f"job_start_date_{key}")

                    st.markdown('<span style="color: white;">City</span>', unsafe_allow_html=True)
                    work_experience['city'] = st.text_input("", work_experience.get('city', ''), key=f"city_{key}")

                with col2:
                    st.markdown('<span style="color: white;">Company</span>', unsafe_allow_html=True)
                    work_experience['company'] = st.text_input("", work_experience.get('company', ''), key=f"company_{key}")

                    st.markdown('<span style="color: white;">End Date</span>', unsafe_allow_html=True)
                    work_experience['end_date'] = st.text_input("", work_experience.get('end_date', ''), key=f"job_end_date_{key}")

                    st.markdown('<span style="color: white;">Country</span>', unsafe_allow_html=True)
                    work_experience['country'] = st.text_input("", work_experience.get('country', ''), key=f"country_{key}")

                st.markdown('<span style="color: white;">Job Description</span>', unsafe_allow_html=True)
                work_experience['job_description'] = st.text_input("", work_experience.get('job_description', ''), key=f"job_description_{key}")

                # Add the Remove Work Experience button
                if st.button(f"Remove Work Experience {index + 1}", key=f"remove_work_experience_{key}"):
                    st.session_state.work_experiences.pop(key)
                    st.experimental_rerun()  # Refresh the page to reflect the removal

            # Button to add a new education entry
            if st.button("Add Work Experience"):
                new_key = f"school_{len(st.session_state.work_experiences) + 1}"
                st.session_state.work_experiences[new_key] = {
                    "job_title": "",
                    "company": "",
                    "start_date": "",
                    "end_date": "",
                    "city":"",
                    "country":"",
                    "job_description":""
                }
                st.experimental_rerun()  # Refresh the page to reflect the addition

            # Button to save all education entries to the database
            if st.button("Save Work Experiences to Database"):
                user_id = st.session_state["user_id"]
                for work_experience in st.session_state.work_experiences.values():
                    insert_work_exp_entry(user_id, work_experience)
                st.success("All work experiences have been saved to the database.")

    else:
        st.info("Please log in to add your education details.")


    st.markdown('<h2 style="color: white;">Education</h2>', unsafe_allow_html=True)
    # Check if the user is logged in by checking if user_id exists in session_state
    if 'user_id' in st.session_state:
        with st.expander("Add Education", expanded=True):
            # Loop through each education entry stored in session_state
            for index, (key, education) in enumerate(st.session_state.education_entries.items()):
                st.markdown(f'<h4 style="color: white;">Education {index + 1}</h4>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)

                with col1:
                    # Display labels in white and input fields below
                    st.markdown('<span style="color: white;">University</span>', unsafe_allow_html=True)
                    education['university'] = st.text_input("", education.get('university', ''), key=f"university_{key}")

                    st.markdown('<span style="color: white;">Degree</span>', unsafe_allow_html=True)
                    education['degree'] = st.text_input("", education.get('degree', ''), key=f"degree_{key}")

                with col2:
                    st.markdown('<span style="color: white;">Graduation Year</span>', unsafe_allow_html=True)
                    education['grad_year'] = st.text_input("", education.get('grad_year', ''), key=f"graduation_year_{key}")

                    st.markdown('<span style="color: white;">Grade</span>', unsafe_allow_html=True)
                    education['grade'] = st.text_input("", education.get('grade', ''), key=f"grade_{key}")

                # Add the Remove Education button
                if st.button(f"Remove Education {index + 1}", key=f"remove_education_{key}"):
                    st.session_state.education_entries.pop(key)
                    st.experimental_rerun()  # Refresh the page to reflect the removal

            # Button to add a new education entry
            if st.button("Add Education"):
                new_key = f"school_{len(st.session_state.education_entries) + 1}"
                st.session_state.education_entries[new_key] = {
                    "university": "",
                    "degree": "",
                    "graduation year": "",
                    "grade": ""
                }
                st.experimental_rerun()  # Refresh the page to reflect the addition

            # Button to save all education entries to the database
            if st.button("Save Education Entries to Database"):
                user_id = st.session_state["user_id"]
                for education in st.session_state.education_entries.values():
                    insert_education_entry(user_id, education)
                st.success("All education entries have been saved to the database.")

    else:
        st.info("Please log in to add your education details.")

    
    st.markdown('<h2 style="color: white;">Projects</h2>', unsafe_allow_html=True)
    # Check if user is logged in 
    if 'user_id' in st.session_state:
        with st.expander("Add Project", expanded=True):
            # Loop through each project entry stored in session_state
            for index, (key, project) in enumerate(st.session_state.projects.items()):
                st.markdown(f'<h4 style="color: white;">Project {index + 1}</h4>', unsafe_allow_html=True)
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown('<span style="color: white;">Start Date</span>', unsafe_allow_html=True)
                    project['start_date'] = st.text_input("", project.get('start_date', ''), key=f"project_start_date_{index}")
                with col2:
                    st.markdown('<span style="color: white;">End Date</span>', unsafe_allow_html=True)
                    project['end_date'] = st.text_input("", project.get('end_date', ''), key=f"project_end_date_{index}")

                st.markdown('<span style="color: white;">Project Description</span>', unsafe_allow_html=True)
                project['description'] = st.text_input("", project.get('description', ''), key=f"project_description_{index}")

                # Add the Remove Education button
                if st.button(f"Remove Project {index + 1}", key=f"remove_project_{key}"):
                    st.session_state.projects.pop(key)
                    st.experimental_rerun()  # Refresh the page to reflect the removal

            # Button to add a new education entry
            if st.button("Add Project"):
                new_key = f"school_{len(st.session_state.projects) + 1}"
                st.session_state.projects[new_key] = {
                    "start_date": "",
                    "end_date": "",
                    "description": ""
                }
                st.experimental_rerun()  # Refresh the page to reflect the addition

                 # Button to save all education entries to the database
            if st.button("Save Projects to Database"):
                user_id = st.session_state["user_id"]
                for project in st.session_state.projects.values():
                    insert_project_entry(user_id, project)
                st.success("All project entries have been saved to the database.")

    else:
        st.info("Please log in to add your projects.")


    
    st.markdown('<h2 style="color: white;">Certifications</h2>', unsafe_allow_html=True)

    if 'user_id' in st.session_state:
        with st.expander("Add Certification", expanded=True):
            # Loop through each project entry stored in session_state
            for index, (key, certification) in enumerate(st.session_state.certifications.items()):
                st.markdown(f'<h4 style="color: white;">Certiciate {index + 1}</h4>', unsafe_allow_html=True)

                st.markdown('<span style="color: white;">Certificate Title</span>', unsafe_allow_html=True)
                certification['title'] = st.text_input("", certification.get('title', ''), key=f"certificate_{index}")

                # Add the Remove Education button
                if st.button(f"Remove Certification {index + 1}", key=f"remove_certification_{key}"):
                    st.session_state.certifications.pop(key)
                    st.experimental_rerun()  # Refresh the page to reflect the removal

            # Button to add a new certification
            if st.button("Add Certification"):
                new_key = f"school_{len(st.session_state.certifications) + 1}"
                st.session_state.certifications[new_key] = {
                    "title":""
                }
                st.experimental_rerun()  # Refresh the page to reflect the addition

            if st.button("Save Certifications to Database"):
                user_id = st.session_state["user_id"]
                for certification in st.session_state.certifications.values():
                    insert_certification_entry(user_id, certification)
                st.success("All certifications have been saved to the database.")

    else:
        st.info("Please log in to add your certifications.")



    st.markdown('<h2 style="color: white;">Skills</h2>', unsafe_allow_html=True)
    if 'user_id' in st.session_state:
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

            if st.button("Save Skills to Database"):
                user_id = st.session_state["user_id"]
                insert_skills_query(user_id,st.session_state.skills)
                st.success("Your skills have been saved to the database.")
    else:
        st.info("Please log in to add your skills.")
with tab3:

    st.markdown('<h2 style="color: white;">Job Search</h2>', unsafe_allow_html=True)
    job_title_search = st.text_input("Job Title", placeholder="Enter job title")
    location_search = st.text_input("Location", placeholder="Enter location")

    if st.button("Job Search"):
        # Instantiate the driver
        driver = uc.Chrome(options=chrome_options)

        load_and_search(driver, job_title_search, location_search)
        

        # Find the job information
        job_dic = save_job_information(driver)

        # Save job_dic to session state so it can be accessed outside this block
        st.session_state['job_dic'] = job_dic
        st.session_state['driver'] = driver

        with open("job_description.json", "w") as outfile: 
            json.dump(job_dic, outfile)

        display_job_details()
        
            
    if st.button("➡️ Next Job"):
        driver = st.session_state.get('driver')
        if driver:
            # Get the next job posting and save it to session state
            next_job_posting(driver)  # Scrolls to the next job in the job listing
            job_dic = save_job_information(driver)  # Fetch the new job details
            st.session_state['job_dic'] = job_dic

            display_job_details()
        else:
            st.error("Please start the job search first by clicking 'Job Search'.")
                    


    # Buttons with icons for additional functionality
    st.markdown("---")  # Divider line for visual separation

    if st.button("💾 Save Job", key= 'yoyoyo'):
        user_id = st.session_state.get("user_id")
        #job_dic = save_job_information(driver)
        if user_id and st.session_state["job_dic"]:  # Ensure both exist
            save_job_query(user_id, st.session_state["job_dic"])
            st.success("This job has been saved")
        else:
            st.error("User ID or job data is missing.")
        

#col1, col2,= st.columns(2)
#st.button("🤖 Generate CV")
atexit.register(lambda: conn.close())
#conn.close() #closes connection


    


    
    






            


    

   

   
    


    

