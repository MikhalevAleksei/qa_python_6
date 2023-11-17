import allure

from locators.main_page_locators import MainPageLocators


class TestTransitByClickOnLogo:

    @allure.title('test transit by click on logo yandex')
    def test_click_to_logo_yandex(self, driver, main_page):
        window_after = driver.window_handles[1]
        main_page.click_to_logo_yandex()
        driver.switch_to.window(window_after)
        assert driver.check_click_to_logo_yandex_for_transit()

    @allure.title('test transit by click on logo scooter')
    def test_click_to_logo_scooter(self, driver, main_page):
        main_page.click_to_element(MainPageLocators.BTN_UPPER_ORDER)
        driver.click_to_logo_scooter()
        assert driver.check_click_to_logo_scooter_for_transit()
