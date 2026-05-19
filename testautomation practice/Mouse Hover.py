from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)


hover=driver.find_element(By.XPATH, "//button[normalize-space()='Point Me']")
actions=ActionChains(driver)
actions.move_to_element(hover).perform()

laptops_option=driver.find_element(By.XPATH, "//a[normalize-space()='Mobiles']")
actions.move_to_element(laptops_option).click().perform()

time.sleep(5)