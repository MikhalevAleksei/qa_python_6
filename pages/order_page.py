import allure

from helpers import generated_client, choose_rent_period, choose_metro_locator
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import Client


class OrderPage(BasePage):

    @allure.step("Fill name field")
    def set_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.NAME_FLD_LOCATOR, text)

    @allure.step("Fill last name field")
    def set_lastname_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.LASTNAME_FLD_LOCATOR, text)

    @allure.step("Fill address field")
    def set_address_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.ADDRESS_FLD_LOCATOR, text)

    @allure.step("Fill metro name field")
    def set_metro_name_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.METRO_FLD_LOCATOR, text)

    @allure.step("Fill phone name field")
    def set_phone_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.PHONE_FLD_LOCATOR, text)

    @allure.step("Click to further button")
    def click_to_further_button(self):
        self.click_to_element(OrderPageLocators.BUTTON_FURTHER)

    @allure.step("Fill date of order field")
    def set_date_of_order_to_field(self, text):
        self.set_text_to_element(OrderPageLocators.DATE_FIELD_LOCATOR, text)

#TODO
    @allure.step("Fill date of order field")
    def set_date_of_order_to_field(self):
        self.click_to_element(OrderPageLocators.DATE_FIELD_LOCATOR)
        all_dates = self.

    @allure.step("Fill period of rent field")
    def set_period_of_rent_to_field(self):
        self.click_to_element(OrderPageLocators.RENT_PERIOD_FIELD)

    @allure.step("Choose color for scooter")
    def set_black_color(self):
        self.click_to_element(OrderPageLocators.BLACK_COLOR_LOCATOR)

    @allure.step("Fill metro name field")
    def set_metro_name_to_field(self):
        metro_locator = choose_metro_locator()
        metro_name = choose_metro_locator().text
        self.set_text_to_element(metro_locator, metro_name)

    @allure.step("Click to order button")
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step("Check pop-up order window")
    def check_success_order(self):
        return self.find_my_element(OrderPageLocators.ORDER_WINDOW)

    @allure.step("Create order")
    def create_order(self):
        gen_data = next(generated_client())
        first_name = gen_data.first_name
        last_name = gen_data.last_name
        address = gen_data.address
        phone = gen_data.phone
        metro = Client.metro
        period = Client.period
        self.set_name_to_field(first_name)
        self.set_lastname_to_field(last_name)
        self.set_address_to_field(address)
        self.set_metro_name_to_field(metro)
        self.set_phone_to_field(phone)
        self.click_to_further_button()
        self.set_date_of_order_to_field(text)
        self.set_period_of_rent_to_field(period)
        self.set_black_color()
        self.click_to_order_button()
