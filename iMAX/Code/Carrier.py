from selenium import webdriver
import unittest
from Login_Page import *
from Excel_Read_Utility import *
import time
from selenium.webdriver.support.ui import Select
import xlrd, unittest
#from ddt import ddt, data, unpack
from decimal import Decimal

#@ddt
class Carrier(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()

    def test_CPG(self):
        homepage = Homepage(self.driver)
        homepage.navigate()
        signup_form = homepage.getSignupForm()
        signup_form.setName("admin", "brijesh84")
        time.sleep(5)
        self.driver.find_element_by_css_selector("li.company > a > div.menu_name").click()
        time.sleep(3)
        #self.driver.find_element_by_id("Pratik_test_c").click()
        #time.sleep(3)
        self.driver.find_element_by_link_text("Customer Product Group").click()

        x = "Read\CPG.xlsx"
        b =  get_data(x,1)
        for i in range(0,len(b)):
            print b[i]

        time.sleep(3)
        self.driver.find_element_by_id("sbtCustomerproductsgroupAdded").click()
        time.sleep(3)
        self.driver.find_element_by_id("txtProductGroupName").send_keys(b[0])
        self.driver.find_element_by_id("txtCustomerTrunkPrefix").send_keys(Decimal(b[1]))
        self.driver.find_element_by_id("txtCapacity").send_keys(Decimal(b[2]))
        self.driver.find_element_by_id("txtCallPerSecond").send_keys(Decimal(b[3]))
        DRG = Select(self.driver.find_element_by_id("cmbDigitRuleGroupID"))
        DRG.select_by_visible_text("QA_Customer DRG")
        #DRG.select_by_value("9")
        #DRG.select_by_index(2)
        ORT = Select(self.driver.find_element_by_id("cmbRouteProductID"))
        ORT.select_by_index(1)
        self.driver.find_element_by_id("rdoallowTranscoding-1").click()
        CCP = Select(self.driver.find_element_by_id("cmbCauseCodeProfileID"))
        CCP.select_by_index(1)
        self.driver.find_element_by_name("customertechprofile_listbox1[]").click()
        self.driver.find_element_by_id("txtGatewayAddress-0").send_keys(b[4])
        self.driver.find_element_by_id("txtSubnetMask-0").send_keys(Decimal(b[5]))
        self.driver.find_element_by_id("txtSIPPort-0").send_keys(Decimal(b[6]))
        self.driver.find_element_by_id("txtCapacity_Gateway-0").send_keys(Decimal(b[7]))
        self.driver.find_element_by_id("txtCallPerSecond_Gateway-0").send_keys(Decimal(b[8]))

        time.sleep(5)
        self.driver.save_screenshot("Images\Carrier\CPG.png")

    def tearDown(self):
        self.driver.close()