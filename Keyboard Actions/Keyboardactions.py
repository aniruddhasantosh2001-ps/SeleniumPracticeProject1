#CTRL+A
#CTRL+C
#TAB
#CTRL+V

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(r"https://text-compare.com/")

input1=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH, "//textarea[@id='inputText1']")

input1.send_keys("Welcome to Selenium")

act=ActionChains(driver)

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform() #CTRL+A
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform() #CTRL+C
act.send_keys(Keys.TAB).perform() #TAB
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform() #CTRL+V

driver.find_element(By.XPATH, "//div[@class='compareButtonText']").click()

time.sleep(5)