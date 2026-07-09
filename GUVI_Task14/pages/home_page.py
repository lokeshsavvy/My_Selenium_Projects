from selenium.webdriver.common.by import By
from GUVI_Task14.pages.base_page import basepage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(basepage):

    ClOSE_POPUP = (By.XPATH,"//button[contains(@class,'custom-close-button')]")

    PROFILE_MENU = (By.XPATH,"//p[@class='avatar-profile-name d-flex fs-normal m-0']")

    LOGOUT_BTN = (By.XPATH,"//div[text()='Log out']")

    def close_popup(self):
        self.click_element(self.ClOSE_POPUP)

    def logout(self):

        self.click_element(self.PROFILE_MENU)
        logout_btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BTN))
        logout_btn.click()

