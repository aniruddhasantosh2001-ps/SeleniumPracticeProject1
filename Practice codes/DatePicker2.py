from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://www.dummyticket.com/dummy-ticket-for-visa-application/")

time.sleep(2)

#Date of birth
driver.find_element(By.XPATH,"//input[@id='dob']").click()

datepicker_month=Select(driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']"))
datepicker_month.select_by_visible_text("Jun")

datepicker_year=Select(driver.find_element(By.XPATH, "//select[@data-handler='selectYear']"))
datepicker_year.select_by_visible_text("2001")

dates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text=="24":
        date.click()
        break



time.sleep(2)