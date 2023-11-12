from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD_LOCATOR = [By.XPATH, "//*[contains(@class, "
                                    "'Input_Responsible') and text()='* Имя']"]
    LASTNAME_FIELD_LOCATOR = [By.XPATH, "//*[text()='* Фамилия']"]

    ADRESS_FIELD_LOCATOR = [By.XPATH, \
                            "//*[text()='* Адрес: куда привезти заказ']"]

    METRO_FIELD_LOCATOR = [By.XPATH, "//*[@value='Бульвар Рокоссовского']"]

    PHONE_FIELD_LOCATOR = \
        [By.XPATH, "//*[@placeholder='* Телефон: на него позвонит курьер']"]


    BUTTON_FURTHER = [By.XPATH, "//*[text()='Далее']"]

    RENT_PERIOD_FIELD = [By.XPATH, "//*[text()='* Срок аренды']"]

    DATE_FIELD_LOCATOR = \
        [By.XPATH, "//*[@placeholder='* Когда привезти самокат']"]

    BLACK_COLOR_LOCATOR = [By.ID, "black"]

    UP_ORDER_BUTTON = [By.XPATH, "//*[text()='Заказать']"]
    DOWN_ORDER_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]

    ORDER_WINDOW = [By.XPATH, "//*[text()='Хотите оформить заказ?']"]
