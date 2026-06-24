from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

source=driver.find_element(By.XPATH, "//div[@id='draggable']")
target=driver.find_element(By.XPATH, "//div[@id='droppable']")

actions=ActionChains(driver)
actions.drag_and_drop(source,target).perform()

time.sleep(10)