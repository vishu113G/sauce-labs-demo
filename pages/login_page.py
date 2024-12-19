from playwright.sync_api import expect, Page
from pages.base_page import BasePage
from utils.config import USERNAME, PASSWORD, BASE_URL


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.login_container: str = '#login_button_container'
        self.username_input: str = '#user-name'
        self.password_input: str = '#password'
        self.submit_button: str = '#login-button'

        self.menu_button: str = '#react-burger-menu-btn'
        self.invalid_login_label: str = '.error-message-container'

    def login(self, username: str = USERNAME, password: str = PASSWORD) -> None:
        """Log in to the application using the provided username and password."""
        # Wait for the login container

        self.goto(BASE_URL)
        self.wait_for_element_to_be_visible(self.login_container)

        # Fill in the username and password fields
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)

        # Click the submit button
        self.click(self.submit_button)


