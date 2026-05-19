from outcome import Maybe
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)

#driver.find_element(By.XPATH, "//*[@id='datepicker']").send_keys("05/11/2025") #mm/dd/yyyy

year="2026"
month="June"
date="24"

driver.find_element(By.XPATH, "//*[@id='datepicker']").click() #open datpicker

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()
        #driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()

dates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dat in dates:
    if dat.text==date:
        dat.click()
        break


time.sleep(5)

