### How to run it on your own machine

1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
### What is in this folder?
- .gitignore: This file instructs git on which file types should not be added to GitHub.
- LICENSE: This file contains the licensing agreement.
- README.md: The file you are currently in.
- find_core_job_details.py: Containing the code to scrap indeed.com job post.
- job_description.json: A json file that stores the scraped job post.
- loading_and_instantiate.py: Containing the code to load the web driver and set up indeed.com.
- pipeline.py: Contains the code which sets the web driver and initiates web scraping.
- role_read_logo.png: The logo of the website.
- role_ready_query.sql: The SQL for the data model we designed. The SQL code will create all the tables for the model.
- streamlit_app.py: the app itself, containing all the functions combined.
