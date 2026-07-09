from selenium.webdriver.common.by import By
from GUVI_Task14.pages.base_page import basepage

class LoginPage(basepage):
    EMAIL = (By.XPATH,"//input[@id=':r1:']")
    PASSWORD = (By.XPATH,"//input[@id=':r2:']")
    LOGIN_BTN = (By.XPATH,"//button[@class='primary-btn sign-in-pad']")

    def login(self,username,password):
        self.enter_text(self.EMAIL,username)
        self.enter_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BTN)

    def is_username_displayed(self):
            return self.is_element_displayed(self.EMAIL)

    def is_password_displayed(self):
        return self.is_element_displayed(self.PASSWORD)

    def is_login_button_displayed(self):
        return self.is_element_displayed(self.LOGIN_BTN)


