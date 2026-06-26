# To Open Chrome and launch the website
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# To Use WebdriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# To Connect To MySQL Server
import mysql.connector

# To Use By. and select class
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# For Regular Expressions
import re


serv_obj=Service(ChromeDriverManager().install())

driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://www.sbisecurities.in/calculators/fd-calculator")

wait=WebDriverWait(driver,10)

connection=mysql.connector.connect(host="localhost",user="root",password="admin",database="cal")
cursor=connection.cursor() # Create cursor
cursor.execute("select * from caldata") # Execute Query through cursor

# Reading data from excel
for row in cursor:
    price=row[0]
    roi=row[1]
    per1=row[2]
    per2=row[3]
    freq=row[4]
    exp_mvalue=row[5]

    # Passing data to Application
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='fd_investment']"))).send_keys(price)

    wait.until(EC.visibility_of_element_located((By.ID, "input_interest"))).send_keys(roi)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter Number of Years']"))).send_keys(per1)

    freq_elem=wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select[id='frequency']")))
    comp_freq=Select(freq_elem)
    comp_freq.select_by_visible_text(per2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='form-group col-md-6 mb-3 align']"))).click()

    act_mvalue=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='border']//p[1]"))).text
    act_clean = re.sub(r"[^\d]", "", act_mvalue)  # keeps only digits

    # validation
    if int(act_clean) == int(exp_mvalue):
        print("test Passed")
    else:
        print("Test Failed")

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn sidebar-btn w-100 current-page']"))).click()

connection.close()



