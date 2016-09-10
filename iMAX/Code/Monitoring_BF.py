from selenium import webdriver
import unittest
from Login_Page import *
import time
import autoit
from selenium.webdriver.support.ui import Select


class Monitoring(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_Ping_Traceroute(self):
        homepage = Homepage(self.driver)
        homepage.navigate()
        signup_form = homepage.getSignupForm()
        signup_form.setName("admin", "brijesh84")

        time.sleep(5)

        self.driver.find_element_by_css_selector("li.monitoring > a > div.menu_name").click()
        time.sleep(5)
        my_select = Select(self.driver.find_element_by_id("rdoPingtracert"))
        my_select.select_by_visible_text("Trace route")

        gateway =  Select(self.driver.find_element_by_id("cmbPingtracertBy"))
        gateway.select_by_visible_text("FQDN")

        self.driver.find_element_by_id("txtToFQDNIP").send_keys("www.google.com")
        self.driver.find_element_by_id("txtPacketSize").send_keys("100")
        self.driver.find_element_by_id("txtPacketCount").send_keys("5")

        self.driver.find_element_by_id("Pingtracertsearch").submit()

        #time.sleep(10)

        self.driver.save_screenshot("TraceRoute.png")


    def test_CDR(self):
        homepage = Homepage(self.driver)
        homepage.navigate()
        signup_form = homepage.getSignupForm()
        signup_form.setName("admin", "brijesh84")


        autoit.run("C:\Program Files (x86)\Zoiper\Zoiper.exe")
        autoit.win_wait_active("Zoiper",5)
        autoit.control_send("Zoiper", "Edit1","121919898222221")
        time.sleep(5)
        autoit.send("{ENTER}")

        time.sleep(60)

        time.sleep(5)
        self.driver.find_element_by_css_selector("li.monitoring > a > div.menu_name").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("CDR Trace").click()
        time.sleep(3)
        self.driver.find_element_by_id("rdoCdrSearchType-1").click()
        self.driver.find_element_by_id("txtCustomerIPAddress").send_keys("192.168.20.155")
        self.driver.find_element_by_id("cdrtracesearch").click()
        time.sleep(5)
        temp = "CDR_Print"
        self.driver.save_screenshot("%s.png"%(temp))


    def tearDown(self):
        self.driver.close()