from .LoginPage import LoginPage
from locators.locators import MainPageLocators as Locators


class MainPage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    items_name = []

    def go_to_cart_page(self):
        cart_button = self.find_element(Locators.CART_ICON)
        cart_button.click()

    def click_to_button_add_item_to_cart(self):
        item_card = self.find_elements(Locators.CARD_ITEM)

        for item in item_card:
            add_button = self.find_elements(Locators.ADD_ITEM_TO_CART_BUTTON, element=item)
            if add_button:
                add_button[0].click()
                name = self.find_element(Locators.ITEM_NAME, element=item).text
                self.items_name.append(name)
                break

    def add_multiple_items_to_cart(self, items):
        self.items_name = []
        for item in range(items):
            self.click_to_button_add_item_to_cart()

    def check_success_add_item_to_cart(self, items=1):
        self.check_change_button_in_the_added_item_card(items)
        self.check_update_cart_icon_count(items)
        self.go_to_cart_page()
        self.check_count_items_in_the_cart(items)

    def check_cart_is_empty(self):
        items_in_the_cart_icon = self.find_elements(Locators.ITEMS_IN_THE_CART_ICON)
        if items_in_the_cart_icon:
            raise AssertionError(f"Cart is not empty")

    def check_change_button_in_the_added_item_card(self, items):
        remove_buttons = self.find_elements(Locators.REMOVE_ITEM_AT_CART_BUTTON)
        assert len(remove_buttons) == items, f"Find '{len(remove_buttons)}' remove buttons in items container, " \
                                             f"expected '{items}' "

    def check_update_cart_icon_count(self, items):
        items_in_the_cart_icon = self.find_elements(Locators.ITEMS_IN_THE_CART_ICON)
        if len(items_in_the_cart_icon) == 1:
            count = int(items_in_the_cart_icon[0].text)
            assert count == items, f"There are '{count}' items in the cart, expected '{items}'"
        else:
            raise AssertionError("Cart is empty")

    def check_count_items_in_the_cart(self, items):
        items_in_cart = self.find_elements(Locators.ITEM_IN_CART_PAGE)
        assert len(items_in_cart) == items, f"Expected '{items}' items in cart page, actual '{len(items_in_cart)}'"

        i = 0
        for item in items_in_cart:
            cart_item_name = self.find_element(Locators.ITEM_NAME, element=item)
            assert self.items_name[i] == cart_item_name.text, f"Expected name '{self.items_name[i]}'," \
                                                              f" actual '{cart_item_name.text}' "
            i += 1
