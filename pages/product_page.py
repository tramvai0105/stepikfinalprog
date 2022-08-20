from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_button_click(self):
        self.browser.find_element(*ProductPageLocators.ADD_BUTTON).click()

    def should_be_message_price_equal(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "Product price missing"
        assert self.is_element_present(*ProductPageLocators.BACKET_TOTAL), "Basket total missing"
        basket_total = self.browser.find_element(*ProductPageLocators.BACKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert product_price in basket_total, "Product price not equals to basket total"

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        product_name += " has been added to your basket."
        assert product_name == message, "No product name in the message"
