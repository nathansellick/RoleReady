from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import undetected_chromedriver as uc

import time
import pandas as pd
from IPython.display import display, Image

def reject_cookies(driver):
    """
    This function rejects cookies on the indeed webpage.
    """

    reject_cookie_button_xpath = '/html/body/div[2]/div[2]/div/div[1]/div/div[2]/div/button[2]'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, reject_cookie_button_xpath))) # Page Loads
    driver.find_element(By.XPATH, reject_cookie_button_xpath).click()
    return

def search_job(driver, job_title_search):
    """
    This function adds job name into the indeed job search box.
    """
    search_bar_xpath = '/html/body/div[1]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[1]/div/div/span/input'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, search_bar_xpath))) # Page Loads
    search_box = driver.find_element(By.XPATH, search_bar_xpath)
    search_box.send_keys(job_title_search)  # Change this dynamically later
    return search_box  # Returning search_box so it can be used later

def search_location(driver,  location_search):
    """
    This function adds location to the indeed location search box.
    """
    location_input_bar_xpath = '/html/body/div[1]/div[1]/div/span/div[4]/div[1]/div/div/div/div/form/div/div[1]/div[3]/div/div/span/input'
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location_input_bar_xpath))) # Page Loads
    location_input_bar = driver.find_element(By.XPATH, location_input_bar_xpath)
    location_input_bar.send_keys(location_search)  # Change this dynamically later
    return

def load_and_search(driver, job_title_search, location_search):
    """
    This function instantiates the web driver, loads the Indeed webpage, rejects the cookies, and searches the job and location.
    """    
    # Load the Indeed webpage
    driver.get('https://uk.indeed.com/?from=gnav-homepage')
    time.sleep(1)  # Wait for the page to load
    
    # Reject cookies and perform job search
    reject_cookies(driver)
    search_box = search_job(driver, job_title_search)  # Capture the search_box element
    search_location(driver, location_search)
    
    # Simulate pressing "Enter" to submit the job search
    search_box.send_keys(Keys.ENTER)
    return
