from playwright.sync_api import sync_playwright

def test_valid_login():
    with sync_playwright() as w:
        browser=w.chromium.launch(headless=True, args=["--no-sandbox"])
        page=browser.new_page()
        try:
            page.goto("https://www.saucedemo.com/")
            page.fill('#user-name', 'standard_user')
            page.fill('#password', 'secret_sauce')
            page.click('#login-button')
            page.wait_for_timeout(2000)
            assert "inventory" in page.url

        except Exception:
             page.screenshot(path="screenshots/login_failure.png")
             raise
        finally:
            browser.close()
     
