import pytest

from selenium import webdriver

from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size-1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(Urls.url_main)
    driver.find_element(*MainPageLocators.COOKIE_LOCATOR).click()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def main_page():
    page = MainPage(driver)
    return page


@pytest.fixture(scope='function')
def order_page():
    page = OrderPage(driver)
    return page


