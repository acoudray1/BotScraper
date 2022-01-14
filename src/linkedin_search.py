from datetime import datetime
from os import link
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import variables
import parsel

# opening the chrome window
PATH = "assets/drivers/chromedriver.exe" 
driver = webdriver.Chrome(PATH) 

# login to linkedin
driver.get("https://www.linkedin.com")

username = driver.find_element(By.ID, 'session_key')
username.send_keys(variables.linkedin_username)

password = driver.find_element(By.ID, 'session_password')
password.send_keys(variables.linkedin_password) 

log_in_button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button') 
log_in_button.click()

# search
driver.get("https://www.google.com")

# TODO handle the addition of 0 on the month if under 10th
cookie_name = "YES+shp.gws-"+str(datetime.now().year)+"0"+str(datetime.now().month)+str(datetime.now().day)+"-0-RC2.en+FX+374"

driver.delete_cookie("CONSENT")
driver.add_cookie({'name': "CONSENT", 'value': cookie_name})
driver.refresh()

search_query = driver.find_element(By.NAME, 'q')
search_query.send_keys(variables.search_query)
search_query.send_keys(Keys.RETURN)

linkedin_urls = driver.find_elements(By.TAG_NAME, 'cite')
print(len(linkedin_urls))

# linkedin_urls = driver.find_elements(By.CLASS_NAME, 'iUh30')
# print(len(linkedin_urls))

linkedin_urls = [url.text for url in linkedin_urls]
print(linkedin_urls)