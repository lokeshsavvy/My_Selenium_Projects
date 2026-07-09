from GUVI_Task14.pages.login_page import LoginPage
from GUVI_Task14.pages.home_page import HomePage

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_url("https://v2.zenclass.in/login")
    login_page.login("lokesh12345@gmail.com","Lokesh12345")

    home_page.close_popup()

    assert "dashboard" in driver.current_url.lower()

def test_unsuccesful_login(driver):
    login_page = LoginPage(driver)

    login_page.open_url("https://v2.zenclass.in/login")
    login_page.login("lokesh12345@gmail.com", "Lokesh1234")

    assert "dashboard" not in driver.current_url.lower()

def test_user_name_input_box(driver):
    login_page = LoginPage(driver)

    login_page.open_url("https://v2.zenclass.in/login")

    assert login_page.is_username_displayed()

def test_password_input_box(driver):
    login_page = LoginPage(driver)

    login_page.open_url("https://v2.zenclass.in/login")

    assert login_page.is_password_displayed()

def test_submit_button(driver):
    login_page = LoginPage(driver)

    login_page.open_url("https://v2.zenclass.in/login")

    assert login_page.is_login_button_displayed()

def test_logout_functionality(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open_url("https://v2.zenclass.in/login")
    login_page.login("lokesh12345@gmail.com","Lokesh12345")

    home_page.close_popup()
    home_page.logout()

    WebDriverWait(driver, 10).until(EC.url_contains("login"))

    assert "login" in driver.current_url.lower()

