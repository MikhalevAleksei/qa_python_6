from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FLD_LOCATOR = [By.XPATH, "//*[contains(@class, "
                                    "'Input_Responsible') and text()='* Имя']"]
    LASTNAME_FLD_LOCATOR = [By.XPATH, "//*[text()='* Фамилия']"]

    ADDRESS_FLD_LOCATOR = [By.XPATH, \
                            "//*[text()='* Адрес: куда привезти заказ']"]

    METRO_FLD_LOCATOR = [By.XPATH, "//*[@value='Бульвар Рокоссовского']"]
    METRO_2_FLD_LOCATOR = [By.XPATH, "//*[@value='Черкизовская']"]

    PHONE_FLD_LOCATOR = \
        [By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"]


    BUTTON_FURTHER = [By.XPATH, "//*[text()='Далее']"]

    RENT_PERIOD_FIELD = [By.XPATH, "//*[text()='* Срок аренды']"]

    RENT_PERIOD = [By.XPATH, "//*[text()='* сутки']"]
    RENT_2_PERIOD = [By.XPATH, "//*[text()='* двое суток']"]

    DATE_FIELD_LOCATOR = \
        [By.XPATH, "//*[@placeholder='* Когда привезти самокат']"]
    TODAY_DATE_LOCATOR = [By.XPATH, "//*[@tabindex='0']"]

    BLACK_COLOR_LOCATOR = [By.ID, "black"]

    UP_ORDER_BUTTON = [By.XPATH, "//*[text()='Заказать']"]
    DOWN_ORDER_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]

    MARKER_2_ORDER_STEP = [By.XPATH, "//*[text()='Про аренду']"]

    FINAL_ORDER_BUTTON = \
        [By.XPATH, "//button[contains(@class, Button_Middle') \
                    and text()='Заказать']"]

    ORDER_WINDOW = [By.XPATH, "//*[text()='Хотите оформить заказ?']"]
