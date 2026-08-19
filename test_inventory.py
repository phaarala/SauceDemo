from playwright.sync_api import expect
import inventory, cart, pytest

PRODUCTS = [
    "sauce-labs-backpack",
    "sauce-labs-bike-light",
    "sauce-labs-bolt-t-shirt",
    "sauce-labs-fleece-jacket",
    "sauce-labs-onesie",
    "test.allthethings()-t-shirt-(red)",
]

CUMULATIVE_CASES = [(PRODUCTS[:n], str(n)) for n in range(1, len(PRODUCTS) + 1)]

@pytest.mark.parametrize("items, expected", CUMULATIVE_CASES)
def test_add_items_to_cart_adjusts_badge_count(logged_in_page, items, expected):
    inventory_page = inventory.InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart(items)
    expect(inventory_page.shopping_cart_count).to_have_text(expected)

@pytest.mark.parametrize("item", PRODUCTS)
def test_remove_item_from_cart_button_appears(logged_in_page, item):
    inventory_page = inventory.InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart([item])
    expect(inventory_page.remove_button(item)).to_be_visible()

@pytest.mark.parametrize("item", PRODUCTS)
def test_remove_all_items_from_cart_hides_count(logged_in_page, item):
    inventory_page = inventory.InventoryPage(logged_in_page)
    inventory_page.add_items_to_cart([item])
    inventory_page.remove_items_from_cart([item])
    expect(inventory_page.shopping_cart_count).not_to_be_visible()

@pytest.mark.skip(reason="TODO: verify cart contents")
def test_correct_item_added_to_cart(logged_in_page):
    pass

