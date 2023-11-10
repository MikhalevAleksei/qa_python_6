from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_my_element(self, locator, time_out=5):
        return Wait(self.driver, time_out).until(
            EC.visibility_of_element_located(locator))

    def click_to_element(self, locator, time_out=5):
        Wait(self.driver, time_out).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

