from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

serv_obj=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=serv_obj)
driver.maximize_window()

driver.get(r"https://testautomationpractice.blogspot.com/")
wait=WebDriverWait(driver,10)

original_url=driver.current_url

laptop_links=["Apple", "Lenovo", "Dell"]
for link in laptop_links:
    elem=wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link)))
    elem.click()
    wait.until(EC.url_changes(original_url))

    driver.back()

    wait.until(EC.url_to_be(original_url))
    wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link)))

driver.quit()






