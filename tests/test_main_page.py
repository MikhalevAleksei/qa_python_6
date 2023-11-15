import pytest

from pages.main_page import MainPage
from data import Answers


class TestMainPage:
    @pytest.mark.parametrize('number, result',
                             [(0, Answers.one),
                              (1, Answers.two),
                              (3, Answers.three),
                              (4, Answers.four),
                              (5, Answers.five),
                              (6, Answers.six),
                              (7, Answers.seven),
                              (8, Answers.eight)
                              ]
                             )
    def test_check_question_and_answer(self, driver, number, result):
        MainPage(driver).get_question(number)
        assert MainPage(driver).get_answer(number) == result

    def test_click_to_logo_yandex(self, driver):
        MainPage(driver).click_to_logo_yandex()
        assert MainPage(driver).check_click_to_logo_yandex_for_transit()

    def test_click_to_logo_scooter(self, driver):
        MainPage(driver).click_to_logo_scooter()
        assert MainPage(
            driver).check_click_to_logo_scooter_for_transit()
