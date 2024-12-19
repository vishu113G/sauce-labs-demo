from playwright.sync_api import Page, expect, ElementHandle
from typing import Optional


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        """
        Navigate to the specified URL.

        :param url: The URL to navigate to.
        """
        self.page.goto(url)

    def click(self, selector: str) -> None:
        """
        Click on the element specified by the selector.

        :param selector: The CSS selector of the element to click.
        """
        self.page.locator(selector).click()

    def fill(self, selector: str, text: str) -> None:
        """
        Clear the input field and fill it with the specified text.

        :param selector: The CSS selector of the input field.
        :param text: The text to fill into the input field.
        """
        self.page.locator(selector).clear()
        self.page.locator(selector).fill(text)

    def find_elements(self, selector: str) -> list[ElementHandle]:
        """
        Returns all the elements matching the selector.

        :param selector: The common CSS selector for all the elements.
        :return: The inner text of the element.
        """
        return self.page.query_selector_all(selector)

    def get_text(self, selector: str) -> str:
        """
        Get the inner text of the element specified by the selector.

        :param selector: The CSS selector of the element.
        :return: The inner text of the element.
        """
        return self.page.text_content(selector)

    def is_visible(self, selector: str) -> None:
        """
        Check if the element specified by the selector is visible.

        :param selector: The CSS selector of the element to check visibility for.
        """
        expect(self.page.locator(selector)).to_be_visible()

    def get_attribute(self, selector: str, attribute: str = 'aria-label') -> Optional[str]:
        """
        Get the specified attribute of the element.

        :param selector: The CSS selector of the element.
        :param attribute: The attribute name to retrieve. Defaults to 'aria-label'.
        :return: The value of the specified attribute, or None if it doesn't exist.
        """
        return self.page.locator(selector).get_attribute(attribute)

    def wait_for_element_to_be_visible(self, selector: str) -> None:
        """
        Waits for the element to be visible.

        :param selector: The CSS selector of the element to check visibility for.
        """
        self.page.locator(selector).wait_for()


