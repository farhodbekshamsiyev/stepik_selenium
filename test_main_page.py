from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"
link1 = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"


# link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    login_page = page.go_to_login_page()
    login_page.should_be_login_form()

# def test_guest_can_login(browser):
#     page = LoginPage(browser, link1)
#     page.open()
#     page.should_be_login_page()
