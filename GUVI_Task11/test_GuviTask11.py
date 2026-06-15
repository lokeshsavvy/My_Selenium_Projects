import time
from selenium.webdriver.common.by import By
def test_Guvi(driver):
    driver.get("https://www.guvi.in/")
    driver.maximize_window()
    homescreen_login = driver.find_element(By.XPATH,"//button[contains(text(),'Login')]")
    homescreen_login.click()
    time.sleep(3)
    assert "https://www.guvi.in/sign-in/" in driver.current_url

def test_fields_visibility(driver):
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    email = driver.find_element(By.XPATH, "//input[@id='email']")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    assert email.is_displayed(),"Email field is not visible"
    assert password.is_enabled(),"Password field is not enabled"

def test_submit_btn(driver):
    driver.get("https://www.guvi.in/sign-in/")
    driver.maximize_window()
    login = driver.find_element(By.XPATH, "//a[@id='login-btn']")
    login.click()
    time.sleep(3)
    assert login.is_enabled(),"Login button is not working"


