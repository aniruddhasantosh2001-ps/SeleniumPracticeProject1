from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()

countries_list=driver.find_elements(By.XPATH, "//ul[@id='select2-billing_country-results']/li")
print(len(countries_list))

for country in countries_list:
    if country.text=="India":
        country.click()
        break

time.sleep(5)
