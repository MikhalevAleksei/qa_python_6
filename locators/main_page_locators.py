from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}/child::p"]

    COOKIE_LOCATOR = [By.ID, "rcc-confirm-button"]

    YANDEX_LOGO_LOCATOR = [By.XPATH, "//*[@alt= 'Yandex']"]
    SCOOTER_LOGO_LOCATOR = [By.XPATH, "//*[@alt= 'Scooter']"]
    DZEN_LOGO_LOCATOR = [By.XPATH, "//*[@data-testid= 'logo']"]
