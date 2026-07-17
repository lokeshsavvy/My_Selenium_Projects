from selenium.webdriver.common.by import By
from GUVI_Task16.pages.base_page import BasePage

class PopulationPage(BasePage):

    population_count = (By.XPATH,"//div[@class='counter-ticker is-size-2-mobile']")

    def get_population(self):
        return self.get_text(self.population_count)