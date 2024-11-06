import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def browser_context():
 with sync_playwright() as p:
 browser = p.chromium.launch(headless=False)
 context = browser.new_context()
 yield context
 context.close()
 browser.close()

@pytest.mark.usefixtures("browser_context")
def test_search_resultsautosuggestion(browser_context):
 page = browser_context.new_page()
 page.goto("https://www.britinsurance.com/")
 page.get_by_role("link", name="Allow all cookies").click()
 page.get_by_label("Search button").click()
 page.get_by_placeholder("Search for people, services").click()
 page.get_by_placeholder("Search for people, services").fill("ifrs 17")
 page.keyboard.press('Space')
 page.wait_for_selector("div.header--search__results > div.result")
 results = page.locator(".result").all_text_contents()
 # Assert the number of results
 print("results:",results)
 assert len(results) == 5, f"Expected 5 results, but found {len(results)}"
 # Check for a specific result
 expected_title = "Interim results for the six"
 assert any(expected_title in result for result in results), f"'{expected_title}' not found in results"

@pytest.mark.usefixtures("browser_context")
def test_search_results(browser_context):
 page = browser_context.new_page()
 page.goto("https://www.britinsurance.com/")
 page.get_by_role("link", name="Allow all cookies").click()
 page.get_by_label("Search button").click()
 page.get_by_placeholder("Search for people, services").click()
 page.get_by_placeholder("Search for people, services").fill("ifrs 17")
 page.get_by_placeholder("Search for people, services").press("Enter")
 page.wait_for_selector("div.s-results")
 titles = page.locator("div.s-results > a").all_text_contents()
 print(titles)# Adjust selector based on actual results
 assert len(titles) == 8, f"Expected 5 results, but found {len(titles)}"
 expected_title = "Interim results for the six"
 assert any(expected_title in title for title in titles)

