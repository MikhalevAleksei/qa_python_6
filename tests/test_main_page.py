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
