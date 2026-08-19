from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.get_by_placeholder("Username")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.login_error = page.locator('[data-test="error"]')

    def load(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()
