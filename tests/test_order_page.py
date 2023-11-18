import allure


class TestOrderPage:
    @allure.title('check creating order')
    def test_create_order_success(self, driver, order_page):
        order_page.create_order()
        assert order_page.check_success_order()

