from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    # Add your test logic here
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
