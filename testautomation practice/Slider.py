from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

slider1=driver.find_element(By.XPATH, "//div[@id='HTML7']//span[1]")

actions=ActionChains(driver)
actions.click_and_hold(slider1).move_by_offset(25,0).release().perform()


slider2=driver.find_element(By.XPATH, "//div[@id='HTML7']//span[2]")

actions=ActionChains(driver)
actions.move_to_element(slider2).click_and_hold(slider2).move_by_offset(-50,0).release().perform()

time.sleep(10)

