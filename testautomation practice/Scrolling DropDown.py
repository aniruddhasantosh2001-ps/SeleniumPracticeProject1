from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

item=driver.find_element(By.XPATH, "//input[@id='comboBox']")
actions=ActionChains(driver)
actions.click(item).perform()

item_options=driver.find_element(By.XPATH, "//div[normalize-space()='Item 69']")
actions.move_to_element(item_options).click().perform()

time.sleep(5)
