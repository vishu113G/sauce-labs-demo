import os

import pytest
import logging
from playwright.sync_api import sync_playwright, Playwright, Browser, Page, BrowserContext
from typing import Generator
from utils.common_utils import delete_test_screenshots


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    pw = sync_playwright().start()  # Starting Playwright
    yield pw  # Playwright instance
    pw.stop()


@pytest.fixture(scope="session", params=["chromium"])
def browser(playwright_instance: Playwright, request) -> Generator[Browser, None, None]:
    browser = playwright_instance[request.param].launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser) -> Generator[Page, None, None]:
    context: BrowserContext = browser.new_context(viewport={"width": 1280, "height": 720})
    page: Page = context.new_page()
    yield page
    delete_test_screenshots()
    context.close()


# Hook that is called after each test
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Capture a screenshot if a test fails.
    """
    # Execute the test, then get the test report
    outcome = yield
    report = outcome.get_result()

    # We only want to capture a screenshot for the 'call' phase when the test fails
    if report.when == 'call' and report.failed:
        # Access the page object from the test
        page = item.funcargs.get("page", None)

        # If a page object exists, take a screenshot
        if page:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)  # Create the directory if it doesn't exist

            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            page.screenshot(path=screenshot_path)
            pytest_html = item.config.pluginmanager.getplugin('html')
            if pytest_html:
                extra = getattr(report, 'extra', [])
                extra.append(pytest_html.extras.png(screenshot_path))
                report.extra = extra
            print(f"Screenshot saved at {screenshot_path}")

