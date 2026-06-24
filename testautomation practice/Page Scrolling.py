from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(10)

#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
#value=driver.execute_script("return window.pageYOffset;")
#print("Number of pixels moved:", value)

element=driver.find_element(By.XPATH, "//label[@id='samsung']")
driver.execute_script("arguments[0].scrollIntoView();", element)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

time.sleep(5)

driver.execute_script("window.scrollTo(0,0)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

time.sleep(5)