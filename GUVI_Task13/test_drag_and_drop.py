from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
def test_drag_and_drop_positive(driver):
    driver.get("https://jqueryui.com/droppable/")
    iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
    driver.switch_to.frame(iframe)
    source = driver.find_element(By.XPATH, "//div[@id='draggable']")
    target = driver.find_element(By.XPATH, "//div[@id='droppable']")
    ActionChains(driver).drag_and_drop(source, target).perform()
    assert "Dropped!" in target.text
    driver.switch_to.default_content()

def test_drag_and_drop_negative(driver):
    driver.get("https://jqueryui.com/droppable/")
    iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
    driver.switch_to.frame(iframe)
    target = driver.find_element(By.XPATH, "//div[@id='droppable']")
    assert "dropped!" not in target.text
    driver.switch_to.default_content()