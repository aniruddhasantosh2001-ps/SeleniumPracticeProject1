from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time


serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

slider1=driver.find_element(By.XPATH, "//div[@id='HTML7']//span[1]")
slider2=driver.find_element(By.XPATH, "//div[@id='HTML7']//span[2]")

print("Location of sliders before moving")
print(slider1.location) #{'x': 975, 'y': 2025}
print(slider2.location) #{'x': 1105, 'y': 2025}

actions=ActionChains(driver)

actions.drag_and_drop_by_offset(slider1, 20, 0).perform()
actions.drag_and_drop_by_offset(slider2, -40, 0).perform()

print("Location of sliders after moving")
print(slider1.location) #{'x': 1000, 'y': 2025}
print(slider2.location) #{'x': 1004, 'y': 2025}


time.sleep(10)

