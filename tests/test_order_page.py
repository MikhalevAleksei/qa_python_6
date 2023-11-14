from pages.order_page import OrderPage


class TestOrderPage:
    def test_create_order_success(self, driver):
        OrderPage(driver).create_order(data.NAME, data.LASTNAME)
        assert OrderPage(driver).check_success_order()
