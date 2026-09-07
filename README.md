# SauceDemo — Automated Test Suite (Playwright + pytest)

Automated end-to-end and regression tests for the [SauceDemo](https://www.saucedemo.com) web store, built with **Python, Playwright, and pytest** using the **Page Object Model**.

This project demonstrates practical UI test automation: reliable locators, data-driven tests, shared fixtures, and clean, maintainable structure. It was built as a hands-on portfolio project during a career transition into QA — with an emphasis on *understanding*, so every pattern below was chosen for a reason that's explained.

## What it covers

**Login / authentication**
- Successful login lands the user on the inventory page
- Invalid credentials, blank username, blank password, and a locked-out user each display the correct error message (data-driven)

**Cart / inventory**
- Adding items updates the cart badge count correctly (data-driven, 1–6 items)
- Each product's **Remove** button appears after that product is added
- Removing an item hides its Remove button

## Tech stack

| Purpose - Tool |
| Language - Python |
| Browser automation - Playwright |
| Test runner - pytest (`pytest-playwright`) |
| Version control - Git / GitHub |

## Project structure

```
login.py            # LoginPage page object  — locators + load() / login() actions
inventory.py        # InventoryPage page object — cart badge, add/remove actions
conftest.py         # Shared fixtures: logged_in_page, blank_login_page
test_login.py       # Login and credential-validation tests
test_inventory.py   # Cart / inventory tests
```

## Design decisions

- **Page Object Model** — each page's locators and actions live in a single class (`LoginPage`, `InventoryPage`). A UI change is fixed in one place, and tests read as intent (`login_page.login(...)`) rather than raw mechanics.
- **Stable locators** — targets `data-test` attributes and user-facing roles/placeholders instead of brittle CSS paths or display text, so tests survive cosmetic redesigns.
- **Auto-waiting assertions** — uses Playwright's `expect()`, which waits for the app to be ready instead of checking once and failing on timing. This keeps tests from becoming flaky.
- **Fixtures for setup** — `conftest.py` provides a `logged_in_page` (already authenticated) and a `blank_login_page` (loaded but unauthenticated) so tests start from a known, isolated state without repeating login steps.
- **Data-driven tests** — `@pytest.mark.parametrize` runs one test body across many inputs (credential cases, product counts). Test data is generated from a single `PRODUCTS` source of truth, so adding a product updates every generated case automatically.
- **Separation of concerns** — page objects *perform actions*; tests *own the assertions*.

## Running the tests

```bash
# 1. Clone and enter the project
git clone <your-repo-url>
cd <repo>

# 2. Create and activate a virtual environment
python -m venv venv
# Windows:  .\venv\Scripts\Activate
# macOS:    source venv/bin/activate

# 3. Install dependencies and browsers
pip install pytest-playwright
playwright install

# 4. Run the suite
pytest -v

# ...or watch it run in a real browser:
pytest -v --headed --slowmo 500
```

## Roadmap

- [ ] Continuous integration with GitHub Actions (run the suite on every push)
- [ ] Checkout flow — full end-to-end: cart → checkout → order confirmation
- [ ] `CartPage` page object + cart-contents verification
- [ ] Cross-browser runs (Firefox, WebKit) and an HTML test report

---

*Portfolio project — feedback welcome.*
