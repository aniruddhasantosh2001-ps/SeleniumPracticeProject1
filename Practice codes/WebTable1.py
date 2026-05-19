#1 Count no of rows and columns
#2 Read specific row and column data
#3 Read all rows and columns data
#4 Read data based on condition(List books name whose author is Mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"C:\Drivers\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")

#1
rows=driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
print("No of rows :", len(rows))  #No of rows : 7

columns=driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
print("No of columns :", len(columns)) #No of columns : 4

#2
data1=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text # tr[5]= 5th row & td[1]=1st column
print(data1) #Master In Selenium

#3
row_count=len(rows)
column_count=len(columns)

#for r in range(2, row_count+1):
 #   for c in range(1, column_count+1):
  #      data2=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
   #     print(data2, end='          ')
    #print()

#4
for r in range(2, row_count+1):
    authorName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorName=="Mukesh":
        bookName=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookName, "       ", authorName, "      ", price)






driver.quit()