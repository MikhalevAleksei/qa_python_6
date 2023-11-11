from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD_LOCATOR = [By.XPATH, "//*[contains(@class, "
                                    "'Input_Responsible') and text()='* Имя']"]
    LASTNAME_FIELD_LOCATOR = [By.XPATH, "//*[text()='* Фамилия']"]

    ADRESS_FIELD_LOCATOR =

    METRO_FIELD_LOCATOR =

    PHONE_FIELD_LOCATOR =

    BUTTON_FURTHER = [By.XPATH, "//*[text()='Далее']"]

    BLACK_COLOR_LOCATOR =

    UP_ORDER_BUTTON = [By.XPATH, "//*[text()='Заказать']"]
    DOWN_ORDER_BUTTON = [By.XPATH, "//*[contains(@class, 'Button_Middle')]"]

    ORDER_WINDOW
