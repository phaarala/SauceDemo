from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_count = self.page.locator('[data-test="shopping-cart-badge"]')

    def add_items_to_cart(self, items):
        for item in items:
            self.page.locator(f'[data-test="add-to-cart-{item}"]').click()

    def remove_items_from_cart(self, items):
        for item in items:
            self.page.locator(f'[data-test="remove-{item}"]').click()

    def remove_button(self, item):
        return self.page.locator(f'[data-test="remove-{item}"]')


