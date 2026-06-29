from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
iframe = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(iframe)
source = driver.find_element(By.XPATH,"//div[@id='draggable']")
target = driver.find_element(By.XPATH,"//div[@id='droppable']")
actions = ActionChains(driver)
actions.drag_and_drop(source,target).perform()
driver.switch_to.default_content()
