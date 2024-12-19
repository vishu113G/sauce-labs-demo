from playwright.sync_api import Page
from pages.base_page import BasePage
from utils.logger import setup_logger


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logger = setup_logger()
        self.item_total_locator = "div.summary_subtotal_label"
        self.total_locator = "div.summary_total_label"
        self.finish_button_locator = "#finish"

    def verify_total_price(self, item_total, total_including_tax):

        item_total_text = self.get_text(self.item_total_locator)
        total_text = self.get_text(self.total_locator)
        assert f"{item_total}" in item_total_text and f"{total_including_tax}" in total_text, f"Item total {item_total} and total price " \
                                                                                              f"{total_including_tax} were not as expected -" \
                                                                                              f"{item_total_text} and {total_text}"

    def complete_checkout(self):
        self.click(self.finish_button_locator)
        self.logger.info("Checkout complete")

    
