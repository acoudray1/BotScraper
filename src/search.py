from fileinput import filename
import time
from selenium.webdriver.common.by import By
from model.bot_scraper import BotScraper
import constant.variables as Consts
import pandas as pd

PATH = "../assets/drivers/chromedriver.exe"

bot = BotScraper(PATH)

bot.auth_to_linkedin(Consts.linkedin_username, Consts.linkedin_password)

bot.search_google(Consts.search_query)

nb_pages = 5
info_all = []
info_all.extend(bot.google_scrape())

for i in range(0, nb_pages - 1):
    bot.click_button(By.LINK_TEXT, 'Suivant')
    info_all.extend(bot.google_scrape())

df = pd.DataFrame(info_all)
df.to_csv('../out/' + Consts.file_name)