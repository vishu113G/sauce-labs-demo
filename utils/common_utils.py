import os
import re
import uuid
from math import ceil
from typing import Dict, Optional

import pytest
from PIL import Image, ImageChops


def calculate_total_price(items_info: dict, tax_percent: float):
    item_prices = items_info.values()
    item_total = 0
    for item_price in item_prices:
        item_total += float(item_price[1:])
    total_tax = item_total * tax_percent * 0.01          # Tax looks like 8 %
    total_including_tax = round((item_total + total_tax), 2)
    return item_total, total_including_tax


def delete_test_screenshots() -> None:
    # Define the folder to scan
    folder_path: str = "./screenshots"

    # Loop through all files in the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a .png file and contains "test" in its name
            if file.endswith(".png") and "test" in file:
                file_path: str = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")


def generate_unique_id() -> str:
    # Generates a 6-digit random UUID
    random_uuid: str = str(uuid.uuid4().int)[:6]
    return random_uuid


def parse_test_results(test_output: str) -> Dict[str, Optional[Dict[str, str]]]:
    # Function to extract test summary from pytest output

    # Regular expressions to match the summary lines
    total_tests_pattern = re.compile(r'collected (\d+) items')
    summary_pattern = re.compile(r'(\d+) passed, (\d+) failed')
    final_summary_pattern = re.compile(r'=(\s+)(\d+) passed')

    # Initialize variables
    total_tests: str = "Unknown"
    passed: str = "0"
    failed: str = "0"
    failures: Dict[str, str] = {}

    # Find total tests collected
    total_tests_match = total_tests_pattern.search(test_output)
    if total_tests_match:
        total_tests = total_tests_match.group(1)

    # Find summary line (pass/fail counts)
    summary_match = summary_pattern.search(test_output)
    if summary_match:
        passed = summary_match.group(1)
        failed = summary_match.group(2)
    else:
        # Check the final summary line
        final_summary_match = final_summary_pattern.search(test_output)
        if final_summary_match:
            passed = final_summary_match.group(2)

    # Extract the failures section, if any
    failures_start: int = test_output.find("FAILURES")
    if failures_start != -1:
        failures_section = test_output[failures_start:]
        failures_pattern = re.compile(r'__________________________ (.+?) __________________________\n(.*?)\n', re.DOTALL)
        failure_details = failures_pattern.findall(failures_section)
        for test_name, failure_message in failure_details:
            # Clean up the failure message to include only the assertion error
            failure_message = failure_message.split("E       ")[-1].strip() if "E       " in failure_message else "Unknown error"
            failures[test_name.strip()] = failure_message  # Clean test name to remove extra spaces

    # Create a clean summary
    summary: Dict[str, Optional[Dict[str, str]]] = {
        "total_tests": total_tests,
        "passed": passed,
        "failed": failed,
        "failures": failures
    }

    return summary

