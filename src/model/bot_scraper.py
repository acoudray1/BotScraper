from datetime import datetime
from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import parsel
import time

class BotScraper:

    def __init__(self, PATH):
        self.driver = webdriver.Chrome(PATH)
        print("bot is alive")

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

    ### this function navigates to google and make a search
    ### @param search_query: str
    def search_google(self, search_query):
        self.driver.get("https://www.google.com")

        # TODO handle the addition of 0 on the month if under 10th
        cookie_name = "YES+shp.gws-"+str(datetime.now().year)+"0"+str(datetime.now().month)+str(datetime.now().day)+"-0-RC2.en+FX+374"

        self.driver.delete_cookie("CONSENT")
        self.driver.add_cookie({'name': "CONSENT", 'value': cookie_name})
        self.driver.refresh()

        s_q = self.driver.find_element(By.NAME, 'q')
        s_q.send_keys(search_query)
        s_q.send_keys(Keys.RETURN)

    ### function to scrape google's search page
    ### @return page_info: []
    def google_scrape(self):
        page_info = []
        try:
            # wait for search results to be fetched
            WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "g"))
            )
        except Exception as e:
            print(e)
            self.driver.quit()
        # contains the search results
        search_results = self.driver.find_elements(By.CLASS_NAME, 'g')

        for result in search_results:
            element = result.find_element(By.CSS_SELECTOR, 'a') 
            link = element.get_attribute('href')
            header = result.find_element(By.CSS_SELECTOR, 'h3').text
            page_info.append({
            'header' : header, 'link' : link
            })

        return page_info

    ### click button on page
    ### @param by: selenium.webdriver.common.by (the type of search)
    ### @param text: str (the thing to find)
    def click_button(self, by, text):
        button = self.driver.find_element(by, text)
        button.click()

    def __del__(self):
        self.driver.quit()
        print("bot is dead")