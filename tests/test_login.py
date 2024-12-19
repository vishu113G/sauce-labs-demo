import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from utils.config import BASE_URL, USERNAME, PASSWORD


@pytest.mark.parametrize("username, password, expected_result", [
    (USERNAME, PASSWORD, True),             # Valid credentials
    (USERNAME, "invalid_pass", False)       # Invalid credentials
])
def test_login(page: Page, username: str, password: str, expected_result: bool, request):
    """Test the login functionality with valid and invalid credentials."""
    login_page = LoginPage(page)
    login_page.goto(BASE_URL)
    login_page.login(username, password)
    test_name = request.node.name
    print(f"Running test: {test_name}")

    if expected_result:
        # Assert that the user is logged in by checking for the visibility of the navigation panel
        expect(login_page.page.locator(login_page.menu_button)).to_be_visible()
    else:
        # Assert that the appropriate error message is displayed
        expect(login_page.page.locator(login_page.invalid_login_label)).to_contain_text('Username and password do not match any user')

