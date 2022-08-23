from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        mpage = MainPage(browser, link)
        mpage.open()
        mpage.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/"
        mpage = MainPage(browser, link)
        mpage.open()
        mpage.should_be_login_link()
        mpage.go_to_login_page()
        lpage = LoginPage(browser, browser.current_url)
        lpage.should_be_login_url()
        lpage.should_be_login_form()
        lpage.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    m_page = MainPage(browser, link)
    m_page.open()
    m_page.go_to_basket()
    b_page = BasketPage(browser, browser.current_url)
    b_page.should_not_be_basket_items()
    b_page.should_be_basket_empty_text()
