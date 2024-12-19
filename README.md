# Sauce-Labs-Demo - Playwright Python framework
Automating customer flow in sauce labs demo. Framework used - Playwright Python


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Running Tests](#running-tests)
4. [Test Structure](#test-structure)
5. [HTML Report](#html-report)
6. [Logging](#logging)

---

## Prerequisites

Before running the tests, ensure you have the following installed:

- Python 3.7 or later
- pip (Python package installer)

The tests use the **Playwright** library for browser automation, **pytest** as the test framework, and **pytest-html** for generating HTML reports.

---

## Setup

1. **Clone the Repository**:
   First, clone this repository to your local machine.

   ```bash
   git clone https://github.com/vishu113G/sauce-labs-demo.git
   git checkout master
   
2. **Create a Virtual Environment (optional but recommended)**: 
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install dependencies**: 
   ```bash
    pip install -r requirements.txt
   
4. **Install playwright**: 
   After installing dependencies, you also need to install Playwright’s browser binaries:
   ```bash
    playwright install
    
## Running Tests

To run the tests, simply use **pytest** from the command line.

### Running all tests:
    pytest

### Running tests with HTML Report:
To generate an HTML report of your test results, you can use the pytest-html plugin:

    pytest --maxfail=1 --disable-warnings --html=report.html

### Test Structure
The project is structured as follows:
   
      playwright-python-automation/
      │
      ├── pages/                         # Page Object Model (POM) classes for different pages
      │   ├── cart_page.py               # Cart page interactions
      │   ├── checkout_overview_page.py  # Checkout overview page interactions
      │   ├── checkout_user_info_page.py # User info page interactions
      │   ├── login_page.py              # Login page interactions
      │   ├── product_page.py            # Product page interactions
      │
      ├── tests/                         # Test scripts
      │   ├── test_checkout.py           # Test case for end-to-end checkout process
      │
      ├── utils/                         # Utility functions like price calculation
      │   ├── common_utils.py            # Utility functions (e.g., calculate_total_price)
      │
      ├── requirements.txt               # List of dependencies
      ├── pytest.ini                     # Pytest configuration
      ├── README.md                      # Project README
      └── report.html                    # Generated test report

#### Key Files:
- **Page Object Model (POM)**: The pages directory contains classes that represent various pages in the application under test. Each class encapsulates actions and elements related to a particular page.
  - LoginPage, ProductPage, CartPage, etc.
- **Test Case**: The test case test_checkout.py in the tests folder orchestrates the user flow of logging in, selecting products, adding them to the cart, and completing checkout.
- **Utilities**: The utils/common_utils.py file contains helper functions like calculate_total_price, which is used to compute the price of items including tax.
## HTML Report

By using **pytest-html**, you can generate detailed HTML reports for your tests. Once you run the tests with the `--html=report.html` flag, you can open the `report.html` file in a browser to view:

- Test execution results (pass/fail)
- Detailed logs of each test
- Screenshots or other outputs (if configured)

### Sample Report Example:

The report will display test execution status with the following sections:

- **Summary**: Overall test pass/fail status
- **Test Results**: Individual test cases and their outcomes
- **Logs**: Detailed logs, which can include the steps of the test, assertions, and any errors or failures

## Logging

We use **Python's logging module** to capture important details about the test execution. This helps with debugging and understanding the flow of the tests. You can find logs for key actions, such as logging in, adding items to the cart, and completing the checkout.

### Logging Configuration:

The logger is set up at the beginning of each test file where it is used:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

