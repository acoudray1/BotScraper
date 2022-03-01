from datetime import datetime
from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from .info import Info

class LinkedinBot:

    def __init__(self, PATH) -> None:
        self.driver = webdriver.Chrome(PATH)
        print("linkedin bot is alive")

    ### this functions auth the bot to linkedIn
    ### @param username: str
    ### @param password: str
    def auth_to_linkedin(self, username, password):
        self.driver.get("https://www.linkedin.com")

        l_u = self.driver.find_element(By.ID, 'session_key')
        l_u.send_keys(username)

        l_p = self.driver.find_element(By.ID, 'session_password')
        l_p.send_keys(password) 

        log_in_button = self.driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button') 
        log_in_button.click()

    def __del__(self):
        self.driver.quit()
        print("bot is dead")