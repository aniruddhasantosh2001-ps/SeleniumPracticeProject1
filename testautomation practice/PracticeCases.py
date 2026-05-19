from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

driver.find_element(By.ID, "name").send_keys("Aniruddha S") #Name
driver.find_element(By.ID, "email").send_keys("anirudh.santosh@gmail.com") #Email
driver.find_element(By.ID, "phone").send_keys("9986928446") #Phone
driver.find_element(By.XPATH, "//textarea[@id='textarea']").send_keys("Vijayanagar Bengaluru 560010") #Address
driver.find_element(By.XPATH, "//input[@id='male']").click() #Gender

#Days
days=["monday", "tuesday", "wednesday", "thursday", "friday"]
for day in days:
    driver.find_element(By.ID, day).click()


#country
choose_country=Select(driver.find_element(By.ID, "country"))
choose_country.select_by_visible_text("India")

#Colours
colour=Select(driver.find_element(By.XPATH,"//select[@id='colors']"))
colour.select_by_visible_text("White")

#Sorted List
animal=Select(driver.find_element(By.XPATH, "//select[@id='animals']"))
animal.select_by_visible_text("Lion")

#Date Picker 1
date="24"
month="June"
year="2026"

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dat in dates:
    if dat.text==date:
        dat.click()
        break

# Date Picker 2

driver.find_element(By.XPATH, "//*[@id='txtDate']").click()

datepicker_month=Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
datepicker_month.select_by_visible_text("Jun")

datepicker_yr=Select(driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/div/select[2]"))
datepicker_yr.select_by_visible_text("2026")

dates2=driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for dat2 in dates2:
    if dat2.text=="24":
        dat2.click()
        break

# Date Picker 3

driver.find_element(By.XPATH, "//*[@id='start-date']").send_keys("24-06-2025")
driver.find_element(By.XPATH, "//*[@id='end-date']").send_keys("24-06-2026")
driver.find_element(By.XPATH, "//*[@id='post-body-1307673142697428135']/div[8]/button")

#Tabs

driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']").send_keys("Bugatti")
driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Bugatti Chiron").click()

driver.switch_to.window(driver.current_window_handle)


# Dynamic Button

driver.find_element(By.XPATH, "//*[@id='HTML5']/div[1]/button").click()

# Simple alert
driver.find_element(By.XPATH, "//button[@id='alertBtn']").click()
myalert=driver.switch_to.alert
myalert.accept()

# Confirmation alert
driver.find_element(By.XPATH, "//button[@id='confirmBtn']").click()
myalert2=driver.switch_to.alert
myalert2.dismiss()

# Prompt alert
driver.find_element(By.XPATH, "//button[@id='promptBtn']").click()
myalert3=driver.switch_to.alert
myalert3.send_keys("Aniruddha S")
myalert3.accept()

# New Tab
driver.find_element(By.XPATH, "//button[normalize-space()='New Tab']").click()
driver.switch_to.window(driver.window_handles[-1])
driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium with Python").click()
driver.close()

driver.switch_to.window(driver.window_handles[0])

# Popup Windows
driver.find_element(By.XPATH, "//button[@id='PopUp']").click()

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "Playwright" in driver.title:
        driver.find_element(By.XPATH, "//a[normalize-space()='Get started']").click()
        time.sleep(2)
        driver.close()
        break

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    if "Selenium" in driver.title:
        driver.close()
        break

driver.switch_to.window(driver.window_handles[0])

# Mouse Hover

hover=driver.find_element(By.XPATH, "//button[normalize-space()='Point Me']")
actions=ActionChains(driver)
actions.move_to_element(hover).perform()







time.sleep(10)



