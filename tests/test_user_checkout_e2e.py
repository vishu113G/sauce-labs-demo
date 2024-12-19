
import pytest

from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_user_info_page import CheckoutUserInfoPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


# Define a fixture for user data
from utils.common_utils import calculate_total_price
from utils.logger import setup_logger

logger = setup_logger()


@pytest.fixture
def user_info():
    return {
        "first_name": "John",
        "last_name": "Doe",
        "zip_code": "12345"
    }


def test_user_checkout_e2e(page, user_info):
    """Test to check the customer flow of selecting 3 random items and completing the checkout flow."""

    # Step 1: Login
    login_page = LoginPage(page)
    login_page.login()
    logger.info('Login successful')

    # Step 2: Navigate to the product page and select random items
    product_page = ProductPage(page)
    added_items = product_page.select_random_items(3)
    product_page.navigate_to_cart()

    # Calculate total price including tax (used for assertions later)
    tax_percent = 8     # Tax looks like 8 % at sauce demo
    item_total, total_including_tax = calculate_total_price(added_items, tax_percent)

    # Step 3: Verify items in the cart and proceed to checkout
    cart_page = CartPage(page)
    items_name_list = cart_page.get_items_in_cart()
    assert all(item in added_items for item in items_name_list)
    cart_page.proceed_to_checkout()

    # Step 4: Fill user info on the checkout page
    checkout_user_info_page = CheckoutUserInfoPage(page)
    checkout_user_info_page.fill_user_info(
        user_info["first_name"],
        user_info["last_name"],
        user_info["zip_code"],
    )
    checkout_user_info_page.continue_to_overview()

    # Step 5: Verify order summary and complete checkout
    checkout_overview_page = CheckoutOverviewPage(page)
    checkout_overview_page.verify_total_price(item_total, total_including_tax)
    checkout_overview_page.complete_checkout()

    # Step 6: Assert final confirmation message
    order_success_msg = "Thank you for your order!"
    assert order_success_msg in page.content()




