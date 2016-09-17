import pytest
import os
from selenium import webdriver


@pytest.fixture(scope='session')
def abc(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver


def test_google(abc):
    abc.get("http://www.google.com")
    assert 'Google' in abc.title


def test_yahoo(abc):
    abc.get("http://www.yahoo.com")
    assert 'Yahoo' in abc.title

