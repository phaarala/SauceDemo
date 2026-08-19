import pytest
import login

@pytest.fixture
def logged_in_page(page):
    login_page = login.LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")
    yield page

@pytest.fixture
def blank_login_page(page):
    lp = login.LoginPage(page)
    lp.load()
    yield lp

    