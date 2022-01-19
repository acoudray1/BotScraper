from fileinput import filename
import time
from selenium.webdriver.common.by import By
from model.bot_scraper import BotScraper
from model.info import Info
import constant.variables as Consts
import pandas as pd

PATH = "../assets/drivers/chromedriver.exe"

bot = BotScraper(PATH)

bot.auth_to_linkedin(Consts.linkedin_username, Consts.linkedin_password)

bot.search_google(Consts.search_query, False)

time.sleep(30)

nb_pages = bot.google_search_number_of_pages()
info_all = []
info_all.extend(bot.google_deep_scrape())

page_scrapped = 0
last_url_scrapped = ''

while page_scrapped < nb_pages - 1:
    try:
        bot.click_button(By.LINK_TEXT, 'Suivant', 'Next')
        info_all.extend(bot.google_deep_scrape())
        page_scrapped += 1
        last_url_scrapped = bot.driver.current_url
    except Exception as e:
        print(e)
        print(page_scrapped)
        print(last_url_scrapped)
        
        del bot
        
        bot = BotScraper(PATH)
        bot.auth_to_linkedin(Consts.linkedin_username, Consts.linkedin_password)
        bot.search_google(last_url_scrapped, True)

        df = pd.DataFrame(info_all)
        df.to_csv('../out/' + 'tmp-' + str(page_scrapped) + Consts.file_name)
        time.sleep(30)

df = pd.DataFrame(info_all)
df.to_csv('../out/' + Consts.file_name)