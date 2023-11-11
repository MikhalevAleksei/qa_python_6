from selenium.webdriver.common.by import By


class MainPageLocators:

    QUESTION_LOCATOR = [By.ID, "accordion__button-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}/child::p"]

    COOKIE_LOCATOR = [By.ID, "rcc-confirm-button"]