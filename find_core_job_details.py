from loading_and_instantiate import *

company_xpath_list = ['//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/span/a','//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span/a']



def find_company(driver):
    """
    This function returns the name of the company from a job post.
    Iterates through multiple possible XPaths to locate the company name.
    """
    company_xpath_list = [
        '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div[1]/span/a',
        '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/span/a'
    ]

    company_name = "No Company Name"  # Default value if all XPaths fail

    for xpath in company_xpath_list:
        try:
            # Wait for the element corresponding to the current XPath
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Get the text if the element is found
            company_name = element.text
            if company_name:  # Stop if a non-empty text is found
                break
        except (TimeoutException, NoSuchElementException):
            continue  # Try the next XPath if the current one fails
        except Exception as e:
            return f"An error occurred: {e}"  # Catch unexpected exceptions

    return company_name

def find_job_title(driver):
    """
    This function will return the job title on the job post.
    Iterates through multiple possible XPaths to locate the job title
    """
    job_title_xpath_list = ['//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/h2/span', '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/h2/span']
    job_title = "No Job Title"
    for xpath in job_title_xpath_list:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Get the text if the element is found
            job_title = element.text.rsplit("-", 1)[0]
            if job_title:
                break
        except (TimeoutException, NoSuchElementException):
            continue  # Try the next XPath if the current one fails
        except Exception as e:
            return f"An error occurred: {e}"  # Catch unexpected exceptions
        
    return job_title

def find_location(driver):
    """
    This function will return the location of the job on the job post.
    Iterates through multiple possible XPaths to locate the location
    """
    location_xpath_list = ['xpath', '//*[@id="jobLocationText"]/div/span', '//*[@id="jobsearch-ViewjobPaneWrapper"]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div']
    for xpath in location_xpath_list:
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            # Get the text if the element is found
            location = element.text
            if location:
                break
        except (TimeoutException, NoSuchElementException):
            continue  # Try the next XPath if the current one fails
        except Exception as e:
            return f"An error occurred: {e}"  # Catch unexpected exceptions
    return location

def find_salary(driver):
    """
    This function will return the salary on the job description.
    """
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.js-match-insights-provider-tvvxwd.ecydgvn1')))
        salary = driver.find_element(By.CSS_SELECTOR, '.js-match-insights-provider-tvvxwd.ecydgvn1').text
    except:
        salary = 'No Salary'
    return salary

def find_employment_type(driver):
    """
    This function will return the employment type e.g. part-time, full-time.
    """
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-k5flys.eu4oa1w0')))
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.jobsearch-JobComponent-description.css-16y4thd.eu4oa1w0')))
        job_description = driver.find_element(By.CSS_SELECTOR, '.jobsearch-JobComponent-description.css-16y4thd.eu4oa1w0').text
    except:
        job_description = 'No Job Description'
    return job_description

def find_company_rating(driver):
    """
    The function returns the company rating found on the job post.
    """
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-ppxtlp.e1wnkr790')))
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
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1234qe1.e8ju0x51')))
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
    driver.find_element('xpath', '/html/body/main/div/div[2]/div/div[5]/div/div[1]/div[5]/div/ul/li[2]').click()
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
