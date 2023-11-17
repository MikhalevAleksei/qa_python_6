import allure
import pytest

from data import Answers


class TestMainPage:
    @allure.title('check question and answer')
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
    def test_check_question_and_answer(self, driver, main_page, number,
                                       result):
        main_page.get_question(number)
        assert main_page.get_answer(number) == result
