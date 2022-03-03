from fileinput import filename
import time
from selenium.webdriver.common.by import By
from model.linkedin_bot import LinkedinBot
from model.info import Info
import constant.variables as Consts
import constant.ids as Ids
import pandas as pd

PATH = "../assets/drivers/chromedriver.exe"

bot = LinkedinBot(PATH)
bot.auth_to_linkedin(Ids.linkedin_username, Ids.linkedin_password)
