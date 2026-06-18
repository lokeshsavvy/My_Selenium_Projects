from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.guvi.in/")
driver.maximize_window()

# 3) Relative Xpath
live_class = driver.find_element(By.XPATH,"//p[contains(text(),'LIVE Classes')]")
live_class.click()
data_science = driver.find_element(By.XPATH,"//p[contains(text(),'Data Science')]")
parent = driver.find_element(By.XPATH,"//p[contains(text(),'Data Science')]/parent::div")
print(parent.text)
ancestor = driver.find_element(By.XPATH,"//p[contains(text(),'Data Science')]/ancestor::div[3]")
print(ancestor.text)
sibling = driver.find_element(By.XPATH,"//p[contains(text(),'Data Science')]/ancestor::div/following-sibling::div[1]")
print(sibling.text)
href_element = driver.find_element(By.XPATH,"//a[@href]/parent::*")
print(" ".join(href_element.text.split()))

#Finding all ancestor elements
ancestors = driver.find_elements(By.XPATH,"//p[contains(text(),'VLSI Design Programme')]/ancestor::*")
print(len(ancestors))
#following siblings
following = driver.find_elements(By.XPATH,"//p[contains(text(),'UI/UX Design')]/ancestor::div/following-sibling::div")
for i in following:
    print(i.text)
#select all preceding elements
precedings = driver.find_elements(By.XPATH,"//p[contains(text(),'AI DevOps Program')]/preceding::*")
print(len(precedings))





