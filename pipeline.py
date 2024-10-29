from find_core_job_details import *
import json

# Setup Chrome options to disable popups and redirections
chrome_options = Options()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
# Instantiate the driver
driver = uc.Chrome(options=chrome_options)
load_and_search(driver)

# Find the job information
job_dic = save_job_information(driver)

with open("job_description.json", "w") as outfile: 
    json.dump(job_dic, outfile)