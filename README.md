# Sauce-Labs-Demo - Playwright Python framework
Automating customer flow in sauce labs demo. Framework used - Playwright Python


## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Setup](#setup)
3. [Running Tests](#running-tests)
4. [Test Structure](#test-structure)
5. [HTML Report](#html-report)
6. [Logging](#logging)
7. [Contributing](#contributing)

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
   git clone https://github.com/your-username/playwright-python-automation.git
   cd playwright-python-automation
   
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
    playwright install

### Running tests with HTML Report:
To generate an HTML report of your test results, you can use the pytest-html plugin:

    pytest --maxfail=1 --disable-warnings --html=report.html

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

The logger is set up at the beginning of each test file:

```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

