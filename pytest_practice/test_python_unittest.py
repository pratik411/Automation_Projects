import unittest
from selenium import webdriver


class Python_unittets(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def test_open_browser(self):
        self.driver.get("http://www.google.com")

    def tearDown(self):
        # close the browser window
        self.driver.quit()
