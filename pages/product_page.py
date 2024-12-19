import random

from playwright.sync_api import expect, Page
from pages.base_page import BasePage
from utils.logger import setup_logger


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logger = setup_logger()
        self.product_list_locator = ".inventory_item"  # Locator for product items
        self.product_item_name = ".inventory_item_name"
        self.product_item_price = ".inventory_item_price"
        self.add_to_cart_button_locator = "button[class='btn btn_primary btn_small btn_inventory ']"  # Locator for Add to Cart buttons
        self.cart_icon_locator = "a.shopping_cart_link"  # Locator for cart icon

    def select_random_items(self, count):
        products = self.find_elements(self.product_list_locator)
        selected_products = random.sample(products, count)
        product_info = {}
        for product in selected_products:
            product_name = product.query_selector(self.product_item_name).inner_text()
            product_price = product.query_selector(self.product_item_price).inner_text()
            product_info.update({product_name: product_price})
            add_button = product.query_selector(self.add_to_cart_button_locator)
            add_button.click()

        self.logger.info(f'Added {count} items to the cart')
        return product_info

    def navigate_to_cart(self):
        self.click(self.cart_icon_locator)
