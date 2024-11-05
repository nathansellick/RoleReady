from loading_and_instantiate import *

def find_company(driver):
    """
    This function will return the name of the job on the job post.
    """
    try:
        company_name = driver.find_element(By.CSS_SELECTOR, '.css-1ioi40n.e19afand0').text
    except:
        company_name = 'No Company Name'
    return company_name

def find_job_title(driver):
    """
    This function will return the job title on the job post.
    """
    try:
        job_title = driver.find_element(By.CSS_SELECTOR, '.jobsearch-JobInfoHeader-title.css-1t78hkx.e1tiznh50').text.split('\n')[0]
    except:
        job_title = 'No Job Title'
    return job_title

def find_location(driver):
    """
    This function will return the location of the job on the job posting.
    """
    try:
        location = driver.find_element(By.CSS_SELECTOR, '[data-testid="inlineHeader-companyLocation"]').text
    except:
        location = 'No Location'
    return location

def find_salary(driver):
    """
    This function will return the salary on the job description.
    """
    try:
        salary = driver.find_element(By.CSS_SELECTOR, '.css-19j1a75.eu4oa1w0').text
    except:
        salary = 'No Salary'
    return salary

def find_employment_type(driver):
    """
    This function will return the employment type e.g. part-time, full-time.
    """
    try:
        employment_type = driver.find_element(By.CSS_SELECTOR, '.css-k5flys.eu4oa1w0').text
        if employment_type.startswith('-'):
            employment_type = employment_type[1:].strip()
    except:
        employment_type = 'No Employment Type'
    return employment_type

def find_job_description(driver):
    """
    This function return the job description from the job post.
    """
    try:
        job_description = driver.find_element(By.CSS_SELECTOR, '.jobsearch-JobComponent-description.css-16y4thd.eu4oa1w0').text
    except:
        job_description = 'No Job Description'
    return job_description

def find_company_rating(driver):
    """
    The function returns the company rating found on the job post.
    """
    try:
        company_rating = driver.find_element(By.CSS_SELECTOR, '.css-ppxtlp.e1wnkr790').text
    except:
        company_rating = 'No Rating'
    return company_rating

def find_apply_link(driver):
    """
    This function will look for the link to apply for the job via company's website. If this can't be found, it will direct you to the job post
    on indeed.
    """
    try:
        apply_link = driver.find_element(By.CSS_SELECTOR, '.css-1234qe1.e8ju0x51').get_attribute('href')
    except:
        apply_link = driver.current_url
    return apply_link

def self_scroll(driver):
    """
    The function is intended to self-scroll after the job search and after extracting information from the first post.
    The function will scroll down the list and center on the next job post.
    """
    global post_number  # Ensure post_number is global here too
    driver.execute_script(f'window.scrollTo(0, {(post_number-1) * 400})')  # Scroll based on post_number
    return

def click_on_job_post(driver): 
    """
    The function will click on the post by the defined sequence.
    """
    global post_number  # Ensure post_number is global here too
    driver.find_element('xpath', f'/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[{post_number}]/div/div/div/div/div/div/table/tbody/tr/td[1]/div[1]/h2/a').click()
    return

post_number = 1
def next_job_posting(driver):
    """
    This function automatically scrolls and clicks on the next post. To use this function, add post_number = 1
    """
    global post_number  # Declare that you are using the global post_number
    self_scroll(driver)
    click_on_job_post(driver)
    post_number += 1  # Move to the next post by incrementing the post_number
    return

def save_job_information(driver):
    """
    The function retunr the job description dictionary which contain informations of the job post
    """
    job_dic = {'job_title' : find_job_title(driver),
               'company' : find_company(driver),
               'company_rating' : find_company_rating(driver),
               'location' : find_location(driver),
               'salary' : find_salary(driver),
               'employment_type' : find_employment_type(driver),
               'job_description' : find_job_description(driver),
               'application_link': find_apply_link(driver)}
    return job_dic
