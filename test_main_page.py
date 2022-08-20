from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    mpage = MainPage(browser, link)
    mpage.open()
    mpage.should_be_login_link()
    mpage.go_to_login_page()
    lpage = LoginPage(browser, browser.current_url)
    lpage.should_be_login_url()
    lpage.should_be_login_form()
    lpage.should_be_register_form()