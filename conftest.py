import pytest

from selenium import webdriver

from data import Urls
from locators.main_page_locators import MainPageLocators


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
