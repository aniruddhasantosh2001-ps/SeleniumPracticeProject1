# ID
# NAME
# LINK TEXT & PARTIAL LINK TEXT
# CLASS NAME
# TAG NAME

# CSS SELECTORS - Customized locators
# 1. Tag id = tagname#valueofID
# 2. tag class = tagname.valueofclass
# 3. tag attribute = tagname[attribute=value]
# 4. tag class attribute =tagname.valueofclass[attribute=value]

# XPATH - Customized locators
# 1. Absolute Xpath - starts with / and only use tags/nodes
# 2. Relative xpath - starts with // and use attributes
# Syntax for relative xpath = //tagname[@attribute='value']

# How to capture xpath automatically - Right click on element --> Inspect --> Highlight HTML Code --> Right Click --> Copy Xpath

# Using 'or , 'and' , #contains() , start-with() and text()
# OR --> driver.find_element(By.XPATH, "//tag[@attribute1='value' or @attribute2='value']")
# AND --> driver.find_element(By.XPATH, "//tag[@attribute1='value' and @attribute2='value']")
# contains() --> driver.find_element(By.XPATH,"//tag[contains(@tag, 'value')]")
# start-with() --> driver.find_element(By.XPATH,"//tag[start-with(@tag, 'value')]")
#text() --> driver.find_element(By.XPATH, "//tag[text()='text']")


# XPATH AXES-------------
# 1. self
# 2. parent
# 3. child
# 4. ancestor
# 5. descendant
# 6. following
# 7. following-sibling
# 8. preceding
# 9. preceding-sibling

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by   import By
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//input[@class='form-control' and@id='name']").send_keys("Aniruddha")
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("anirudh.santosh123@gmail.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9986928446")
driver.find_element(By.XPATH, "//textarea[@class='form-control']").send_keys("#2011 Vijayanagar, bengaluru - 560102")
driver.find_element(By.XPATH, "//input[@id='male']").click()
time.sleep(5)

driver.quit()