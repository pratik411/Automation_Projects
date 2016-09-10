from selenium import webdriver
import unittest
from Login_Page import *
import time
from selenium.webdriver.support.ui import Select


class All_tab(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_all_tab_access(self):
        homepage = Homepage(self.driver)
        homepage.navigate()
        signup_form = homepage.getSignupForm()
        signup_form.setName("admin", "brijesh84")
        self.driver.save_screenshot("Images\login.png")

        time.sleep(5)

        list = ["monitoring","company","product","switch","billing","template","report","admin","tools"]

        for name in list:
            self.driver.find_element_by_css_selector("li.%s > a > div.menu_name"%(name)).click()
            time.sleep(5)
            self.driver.save_screenshot("Images\%s.png"%(name))
            log = open("Log Files\log.txt","a+")
            log.write("%s module tab is successfully get open\r\n"%(name))
            log.close()

    def tearDown(self):
        self.driver.close()