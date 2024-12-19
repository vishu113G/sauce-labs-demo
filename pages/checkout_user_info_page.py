
from playwright.sync_api import Page
from pages.base_page import BasePage


class CheckoutUserInfoPage(BasePage):
    def __init__(self, page: Page) -> None:
        """
        Initializes the DataSourceConfigurePage with the given Playwright page object.

        :param page: The Playwright page instance used to interact with the browser.
        """
        super().__init__(page)

        self.first_name_field = "#first-name"
        self.last_name_field = "#last-name"
        self.zip_field = "#postal-code"
        self.continue_button = "#continue"

    def fill_user_info(self, first_name='Rudra', last_name='Swami', zip_code='4320'):
        self.fill(self.first_name_field, first_name)
        self.fill(self.last_name_field, last_name)
        self.fill(self.zip_field, zip_code)

    def continue_to_overview(self):
        self.click(self.continue_button)
