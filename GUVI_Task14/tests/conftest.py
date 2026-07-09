import pytest
from selenium import webdriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
# @pytest.fixture
# def driver():
#     options = Options()
#     options.add_argument("--headless=new")
#     options.add_argument("--window-size=1920,1080")
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#     yield driver
#     driver.quit()
