from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_question(self, num):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text()

    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text()
