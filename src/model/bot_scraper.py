from datetime import datetime
from re import U
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from .info import Info

class BotScraper:

    def __init__(self, PATH) -> None:
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
    ### @param is_url: bool
    def search_google(self, search_query, is_url):
        if is_url:
            self.driver.get(search_query)
        else:
            self.driver.get("https://www.google.com")

            # TODO handle the addition of 0 on the month if under 10th
            cookie_name = "YES+shp.gws-"+str(datetime.now().year)+"0"+str(datetime.now().month)+str(datetime.now().day)+"-0-RC2.en+FX+374"

            self.driver.delete_cookie("CONSENT")
            self.driver.add_cookie({'name': "CONSENT", 'value': cookie_name})
            self.driver.refresh()

            s_q = self.driver.find_element(By.NAME, 'q')
            s_q.send_keys(search_query)
            s_q.send_keys(Keys.RETURN)

    ### get the number of results and divide it by 10
    ### @return nb_pages: int
    def google_search_number_of_pages(self):
        el = self.driver.find_element(By.ID, 'result-stats').text
        
        number = ''
        for c in el.split():
            if c.isdigit():
                number += str(c)
        
        nb_pages = (int(number) / 10) + 1
        return int(nb_pages)

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
            page_info.append(Info(header, link))

        return page_info

    ### function to scrape google's search page
    ### @return page_info: []
    def google_deep_scrape(self):
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
            text = result.find_elements(By.CSS_SELECTOR, 'span')
            information = Info(header, link)
            for i in range(len(text)):
                if not(text[i].text.startswith('Tradui')):
                    information.add_new_attribute("info_%s" %i, text[i].text, True)
            
            page_info.append(information.to_dict())

        return page_info

    ### click button on page
    ### @param by: selenium.webdriver.common.by (the type of search)
    ### @param text: str (the thing to find)
    def click_button(self, by, text1, text2):
        try:
            button = self.driver.find_element(by, text1)
            button.click()
        except Exception as e1:
            print(e1)
            try:
                button = self.driver.find_element(by, text2)
                button.click()
            except Exception as e2:
                print(e2)
                self.driver.quit()

    def __del__(self):
        self.driver.quit()
        print("bot is dead")