import pytest

from pages.product_page import ProductPage

nums = [pytest.param(num, marks=pytest.mark.xfail) if num == 7 else num for num in range(10)]


@pytest.mark.parametrize("nth", nums)
def test_guest_can_add_product_to_basket(browser, nth):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{nth}'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_thing_in_basket(page.return_book_name())
    page.should_be_same_price(page.return_book_price())
