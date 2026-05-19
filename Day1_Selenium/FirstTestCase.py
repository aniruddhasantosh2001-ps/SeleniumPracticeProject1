from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by   import By
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)

driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()

actual_title = driver.title
expected_title = "OrangeHRM"

if expected_title == actual_title:
    print("Login test passes without any worry!")
else:
    print("Login test fails")

driver.quit()