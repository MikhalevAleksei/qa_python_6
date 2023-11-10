from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):

    def get_question(self, num):
        method, locator = MainPageLocator.QUESTION_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text()

    def get_answer(self, num):
        method, locator = MainPageLocator.ANSWER_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text()


class MainPageLocator:
    # TODO
    QUESTION_LOCATOR = By.XPATH, "//*[@class="my-qustion-locator-{}"]