from pages.main_page import MainPage


class TestMainPage:
    @pytest.mark.parametrize('number, result',
                             [(0, "Стоимость - 400 рублей"),
                              (1, "Какой то ответ")
                              ]
                             )
    def test_check_question_and_answer(driver, number, result):
        MainPage(driver).get_question(number)
        assert MainPage(driver).get_answer(number) == result
