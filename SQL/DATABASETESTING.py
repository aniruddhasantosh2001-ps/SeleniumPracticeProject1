import re
from multiprocessing import connection

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import mysql.connector
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get(r"https://www.sbisecurities.in/calculators/fd-calculator")


connection=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="cal")
cursor=connection.cursor() #create cursor
cursor.execute("select * from caldata") #execute query through cursor

for row in cursor:
        #reading data from excel
    price=row[0]
    roi=row[1]
    per1=row[2]
    per2=row[3]
    freq=row[4]
    exp_mvalue=row[5]

    #passing data to application
    driver.find_element(By.XPATH, "//div[@class='input-group']//input[@id='input_fd_investment']").send_keys(price)
    driver.find_element(By.XPATH, "//input[@id='input_interest']").send_keys(roi)
    driver.find_element(By.XPATH, "//body/app-root/app-fd-calculator[@class='ng-star-inserted']/div[@class='container']/div[@class='col-md-12 pt-5 mt-5']/div[@class='row pdt-30']/div[@class='col-xl-9 col-lg-7 col-md-7']/div[@class='border']/form[@id='validForm']/div[@class='row mt-2 d-flex']/div[@class='form-group col-md-6 mb-3']/input[1]").send_keys(per1)
    comp_freq=Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    comp_freq.select_by_visible_text(per2)
    driver.find_element(By.XPATH, "//div[@class='form-group col-md-6 mb-3 align']").click()
    act_mvalue=driver.find_element(By.XPATH, "//div[@class='border']//p[1]").text
    act_clean=re.sub(r"[^\d]", "", act_mvalue)    #keeps only digits


    #validation
    if int(act_clean)==int(exp_mvalue):
       print("test Passed")
    else:
        print("Test Failed")

    driver.find_element(By.XPATH, "//a[@class='btn sidebar-btn w-100 current-page']").click()
    time.sleep(2)

connection.close()
