from utils.pages.MainPage import MainPage
from utils.locators.locators import CartPageLocators as Locators


class CartPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_checkout_button(self):
        button = self.find_element(Locators.CHECKOUT_BUTTON)
        button.click()
        self.page_has_loaded()

    def click_to_continue_shopping_button(self):
        button = self.find_element(Locators.CONTINUE_SHOPPING_BUTTON)
        button.click()
        self.page_has_loaded()
