from utils.pages.CartPage import CartPage
from utils.locators.locators import OrderPageLocators as Locators
from utils.test_data.testData import get_value as TD


class OrderPage(CartPage):
    def __init__(self, driver):
        super().__init__(driver)

    def input_user_data(self):
        self.input_first_name()
        self.input_last_name()
        self.input_postal_code()

    def click_to_continue_button(self):
        button = self.find_element(Locators.CONTINUE_BUTTON)
        button.click()

    def click_to_finish_button(self):
        button = self.find_element(Locators.FINISH_BUTTON)
        button.click()

    def go_to_order_form(self):
        self.click_to_continue_button()

    def input_first_name(self):
        first_name_input_field = self.find_element(Locators.FIRST_NAME_FORM)
        first_name_input_field.send_keys(TD('OrderPage', 'first_name'))

    def input_last_name(self):
        first_name_input_field = self.find_element(Locators.LAST_NAME_FORM)
        first_name_input_field.send_keys(TD('OrderPage', 'last_name'))

    def input_postal_code(self):
        first_name_input_field = self.find_element(Locators.POSTAL_CODE_FORM)
        first_name_input_field.send_keys(TD('OrderPage', 'postal_code'))

    def check_complete_order(self):
        self.page_has_loaded()
        result_header = self.find_elements(Locators.COMPLETE_ORDER_HEADER_CONTAINER)
        expected_header = TD('OrderPage', 'order_complete_header')
        if result_header:
            assert result_header[0].text == expected_header, f"Expected '{expected_header}', " \
                                                             f"actual '{result_header[0].text}'"
        else:
            raise Exception('Order is uncompleted')

        result_text = self.find_elements(Locators.COMPLETE_ORDER_TEXT_CONTAINER)
        expected_text = TD('OrderPage', 'order_complete_text')
        if result_text:
            assert result_text[0].text == expected_text, f"Expected '{expected_text}', " \
                                                             f"actual '{result_text[0].text}'"
        else:
            raise Exception('Order is uncompleted')
