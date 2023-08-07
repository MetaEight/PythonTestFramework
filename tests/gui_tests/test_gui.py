import allure
import pytest

from utils.pages.LoginPage import LoginPage
from utils.pages.MainPage import MainPage
from utils.pages.OrderPage import OrderPage


@pytest.mark.smoke
class TestSmoke:
    @allure.title("User login")
    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self, driver):
        page = LoginPage(driver)
        with allure.step("Go to the login page"):
            page.go_to_login_page()
        with allure.step("Enter test data and login"):
            page.auth()
        with allure.step("Checking results"):
            page.check_auth_is_correct()

    @allure.title("Add item to cart")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_item_to_cart(self, driver):
        page = MainPage(driver)
        with allure.step("Authorization"):
            page.go_to_login_page()
            page.auth()
        with allure.step("Check the cart is empty"):
            page.check_cart_is_empty()
        with allure.step("Add item to cart"):
            page.click_to_button_add_item_to_cart()
        with allure.step("Checking results"):
            page.check_success_add_item_to_cart()

    @allure.title("Create order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_ordering_item(self, driver):
        page = OrderPage(driver)
        with allure.step("Authorization"):
            page.go_to_login_page()
            page.auth()
        with allure.step("Add item to cart"):
            page.add_multiple_items_to_cart(1)
        with allure.step("Сonfirm selection in cart"):
            page.go_to_cart_page()
            page.click_to_checkout_button()
        with allure.step("Enter test data"):
            page.input_user_data()
        with allure.step("Confirm order creation"):
            page.go_to_order_form()
            page.click_to_finish_button()
        with allure.step("Checking results"):
            page.check_complete_order()


@allure.title("User bad login")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.xfail  # 'user 3' have bad user data, expected error message
def test_bad_login(driver):
    page = LoginPage(driver)
    with allure.step("Go to the login page"):
        page.go_to_login_page()
    with allure.step("Enter test data and login"):
        page.auth('user_3')
    with allure.step("Checking results"):
        page.check_auth_is_correct()


@allure.title("Add multiple items to cart")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.parametrize('items', [2, 4, 5])
def test_add_multiple_items_to_cart(driver, items):
    page = MainPage(driver)
    with allure.step("Authorization"):
        page.go_to_login_page()
        page.auth()
    with allure.step("Check the cart is empty"):
        page.check_cart_is_empty()
    with allure.step("Add item to cart"):
        page.add_multiple_items_to_cart(items)
    with allure.step("Checking results"):
        page.check_success_add_item_to_cart(items)
