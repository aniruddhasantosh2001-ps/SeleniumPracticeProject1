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

circle=driver.find_element(By.XPATH, "//*[name()='circle' and contains(@cx,'15')]")
rectangle=driver.find_element(By.XPATH, "//*[name()='rect' and contains(@x,'3')]")
triangle=driver.find_element(By.XPATH, "//*[name()='polygon' and contains(@points,'15,3 3,27 ')]")

circle.click()
rectangle.click()
triangle.click()

time.sleep(5)