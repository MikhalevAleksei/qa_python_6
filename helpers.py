import random as r

from faker import Faker

from data import Client
from locators.order_page_locators import OrderPageLocators

faker_ru = Faker('ru_Ru')
Faker.seed()


def generated_client():
    yield Client(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        address=faker_ru.adress(),
        phone=faker_ru.phone_number()
    )


def choose_metro_locator():
    metro_locators = (OrderPageLocators.METRO_FLD_LOCATOR,
                      OrderPageLocators.METRO_2_FLD_LOCATOR)
    r_metro_locator = r.choice(metro_locators)
    return r_metro_locator


def choose_rent_period_locator():
    period_locators = (OrderPageLocators.RENT_PERIOD,
                       OrderPageLocators.RENT_2_PERIOD)
    r_period_locator = r.choice(period_locators)
    return r_period_locator


