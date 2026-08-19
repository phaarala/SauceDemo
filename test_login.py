from playwright.sync_api import Page, expect 
import re, login, pytest

"""
Accepted usernames are:
    standard_user
    locked_out_user
    problem_user
    performance_glitch_user
    error_user
    visual_user

Accepted password:
    secret_sauce
"""

# Verify correct username & password moves user to inventory page --------------------------------------
def test_login(blank_login_page):
    blank_login_page.login("standard_user", "secret_sauce")
    expect(blank_login_page.page).to_have_url(re.compile(".*inventory"))

# Test login cases -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
        "username, password, error",
        [
            ("wrong_username", "secret_sauce", "Username and password do not match any user"),
            ("standard_user", "wrong_password", "Username and password do not match any user"),
            ("", "secret_sauce", "Username is required"),
            ("standard_user", "", "Password is required"),
            ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out.")
        ]    
)
def test_invalid_credentials(blank_login_page, username, password, error):
    blank_login_page.login(username, password)
    expect(blank_login_page.login_error).to_contain_text(error)  
