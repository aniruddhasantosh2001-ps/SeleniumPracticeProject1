from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os

serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

location=os.getcwd()

driver.get_screenshot_as_file(location+"\\homepage.png")

time.sleep(5)

driver.quit()