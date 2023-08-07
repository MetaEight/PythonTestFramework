from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME_FORM = (By.NAME, 'user-name')
    PASSWORD_FORM = (By.NAME, 'password')
    SUBMIT_LOGIN_BUTTON = (By.NAME, 'login-button')
    LOGIN_ERROR_BLOCK = (By.TAG_NAME, "h3[data-test='error']")
    LOGIN_LOGO = (By.CLASS_NAME, 'login_logo')


class MainPageLocators(object):
    # Main menu
    OPEN_MENU_ICON = (By.ID, 'react-burger-menu-btn')
    CLOSE_MENU_ICON = (By.ID, 'react-burger-cross-btn')
    LOGOUT_LINK = (By.ID, 'logout_sidebar_link')

    # Cart container
    CART_ICON = (By.CLASS_NAME, 'shopping_cart_link')
    ITEMS_IN_THE_CART_ICON = (By.CLASS_NAME, 'shopping_cart_badge')

    # Drop-down filters list container
    OPEN_FILTERS_LIST = (By.CLASS_NAME, 'product_sort_container')

    ITEMS_LIST = (By.CLASS_NAME, 'product_sort_container')

    # Card item container
    CARD_ITEM = (By.CLASS_NAME, 'inventory_item')
    ITEM_IMAGE = (By.CLASS_NAME, 'inventory_item_img')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    ITEM_DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ADD_ITEM_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name*='add-to-cart']")
    REMOVE_ITEM_AT_CART_BUTTON = (By.CSS_SELECTOR, "button[name*='remove']")

    # Cart page
    ITEM_IN_CART_PAGE = (By.CLASS_NAME, 'cart_item')


class CartPageLocators(object):
    CONTINUE_SHOPPING_BUTTON = (By.NAME, 'continue-shopping')
    CHECKOUT_BUTTON = (By.NAME, 'checkout')


class OrderPageLocators(object):
    # Users data fields
    FIRST_NAME_FORM = (By.NAME, 'firstName')
    LAST_NAME_FORM = (By.NAME, 'lastName')
    POSTAL_CODE_FORM = (By.NAME, 'postalCode')

    CANCEL_BUTTON = (By.NAME, 'cancel')
    CONTINUE_BUTTON = (By.NAME, 'continue')

    FINISH_BUTTON = (By.NAME, 'finish')

    # Finish page
    COMPLETE_ORDER_HEADER_CONTAINER = (By.CLASS_NAME, 'complete-header')
    COMPLETE_ORDER_TEXT_CONTAINER = (By.CLASS_NAME, 'complete-text')
