from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_FIELD = (By.CSS_SELECTOR, ".alert .alertinner p:first-child")
    PRICE_FIELD_START = (By.CLASS_NAME, "col-sm-6.product_main > p")
    PRODUCT_FIELD = (By.CLASS_NAME, "alertinner > strong")
    PRODUCT_FIELD_START = (By.CLASS_NAME, "col-sm-6.product_main > h1")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")
