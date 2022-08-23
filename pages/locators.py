from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_INPUT_PASSWORD1 = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_INPUT_PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    BACKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner > p')