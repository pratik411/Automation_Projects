import pytest
from selenium import webdriver


@pytest.mark.fast
def test_google_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://www.google.com")
    driver.quit()


@pytest.mark.slow
def test_amazone_browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get("http://www.amazon.in/")
    driver.quit()
