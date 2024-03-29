import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('get question')
    def get_question(self, num):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator))

    @allure.step('get answer')
    def get_answer(self, num):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(num)
        return self.find_my_element((method, locator)).text()

    @allure.step('click to logo yandex')
    def click_to_logo_yandex(self):
        self.click_to_element(MainPageLocators.YANDEX_LOGO_LOCATOR)

    @allure.step('click to logo scooter')
    def click_to_logo_scooter(self):
        self.click_to_element(MainPageLocators.SCOOTER_LOGO_LOCATOR)

    @allure.step('Check transit to dzen.ru')
    def check_click_to_logo_yandex_for_transit(self):
        return self.find_my_element(MainPageLocators.DZEN_LOGO_LOCATOR)

    @allure.step('check tranzit to ya.ru')
    def check_click_to_logo_scooter_for_transit(self):
        return self.find_my_element(
            MainPageLocators.YANDEX_LOGO_LOCATOR)

