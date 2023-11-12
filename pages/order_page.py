import allure

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Fill name field")
    def set_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.NAME_FLD_LOCATOR, text)

    @allure.step("Fill last name field")
    def set_lastname_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FLD_LOCATOR, text)

    @allure.step("Choose color for scooter")
    def  set_black_color(self):
        self.click_to_element(OrderPageLocators.BLACK_COLOR_LOCATOR)

    @allure.step("Click to order button")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Check pop-up order window")
    def check_success_order(self):
        return self.find_my_element(OrderPageLocators.ORDER_WINDOW)

    def create_order(self, first_name, lastname):
        self.set_name_to_field(first_name)
        self.set_lastname_to_field(lastname)
        self.set_black_color()
        self.click_to_order_button()
