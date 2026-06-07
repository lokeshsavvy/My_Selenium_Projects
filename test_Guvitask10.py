import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
def test_Sauce_Demo(driver):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)
    assert "Swag Labs" in driver.title
    assert driver.current_url == "https://www.saucedemo.com/"
    driver.quit()
def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.XPATH,'//input[@id="user-name"]').send_keys("lokesh")
    driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("12345678")
    driver.find_element(By.CSS_SELECTOR,"#login-button").click()
    assert "inventory" not in driver.current_url
    driver.quit()





