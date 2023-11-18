from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_my_element(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))

    def find_all_elements(self, locator, timeout=5):
        return Wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator))

    def click_to_element(self, locator, timeout=5):
        Wait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    def set_text_to_element(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text_from_element(self, locator):
        text_element = self.driver.find_element(*locator).text
        return text_element

    def transit_to_another_page(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

