import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.guvi.in/")
homescreen_login = driver.find_element(By.XPATH,"//button[contains(text(),'Login')]")
homescreen_login.click()
time.sleep(3)
email = driver.find_element(By.XPATH,"//input[@id='email']")
email.send_keys("lokeshp0904@gmail.com")
password = driver.find_element(By.XPATH,"//input[@id='password']")
password.send_keys("L!9lokesh")
login = driver.find_element(By.XPATH,"//a[@id='login-btn']")
login.click()
time.sleep(5)
driver.quit()