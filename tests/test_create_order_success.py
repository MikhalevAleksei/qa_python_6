from pages.order_page import OrderPage


def test_create_order_success(driver):
    OrderPage(driver).create_order(data.NANE, data.LASTNAME)
    assert OrderPage(driver).check_success_order()