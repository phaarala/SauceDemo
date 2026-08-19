from playwright.sync_api import Page
import inventory

class Cart:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="checkout")

    def go_to_cart(self, logged_in_page):
        inventory_page = logged_in_page(self.page)
        self.cart_load = inventory_page.page.locator("")

    def get_cart_contents(self):
        cart = []
        cart_item_title = self.page.locator(".inventory_item_name")
        cart_item_price = self.page.locator(".inventory_item_price")
        cart.append(cart_item_title, cart_item_price)