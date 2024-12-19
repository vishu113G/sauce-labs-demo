from typing import List

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: 'Page') -> None:
        super().__init__(page)

        self.cart_items_locator = "div.cart_item"
        self.cart_item_name = ".inventory_item_name"
        self.checkout_button_locator = "#checkout"

    def get_items_in_cart(self) -> List[str]:
        """
        Retrieves the list of item names currently in the cart.

        Returns:
            List[str]: The names of items in the cart.
        """
        items_name_list = []
        cart_items = self.find_elements(self.cart_items_locator)
        for item in cart_items:
            item_name = item.query_selector(self.cart_item_name).inner_text()
            items_name_list.append(item_name)
        return items_name_list

    def proceed_to_checkout(self) -> None:
        """
        Proceeds to the checkout page by clicking the checkout button.

        Raises:
            Exception: If the checkout button is not clickable or is not found.
        """
        self.click(self.checkout_button_locator)

