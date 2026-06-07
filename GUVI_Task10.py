import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)
user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
user_name.send_keys("standard_user")
time.sleep(5)
password = driver.find_element(By.XPATH,'//input[@id="password"]')
password.send_keys("secret_sauce")
time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR,"#login-button")
login.click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
text = driver.page_source
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
    file.write(text)
print("content saved successfully")
