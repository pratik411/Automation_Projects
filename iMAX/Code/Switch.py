# import needed python-selenium library
from selenium import webdriver
import time
import logging
from selenium.webdriver.support.ui import Select
import unittest
from decimal import Decimal

# import custom created files for POM
from TestResultUtility import Report
from Login_Page import *
from Excel_Read_Utility import *

# Define date and logging parameters
x = time.strftime("%Y_%m_%d")
print "Today's Date is :" ,x
open("Log Files\Switch\/" + x + ".txt","w+") #will create log files with today's date time stamp and below is logging related configuration
logging.basicConfig(filename= "Log Files\Switch\/" + x + ".txt",format='%(asctime)s %(message)s',level=logging.INFO)


class switch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        logging.info("============================================================================================")
        logging.info("Browser Opened Successfully with session ID : %s"%(self.driver.session_id))
        logging.info("Browser capabilities : %s"%(self.driver.capabilities))

    def CSC_Profile(self):

        logging.info("Lets get started for CSC Profile sub-module")

        try:
            logging.info("Reading data from xlsx file")
            x = "Read\Switch.xlsx"
            p = get_data(x,1)
            b = get_data(x,2)
            for i in range(0,len(b)):
                print "value of %s parameter is : %s"%(p[i],b[i])
                logging.info("value of %s parameter is : %s"%(p[i],b[i]))
            logging.info("Data reading functionality completed successfully")
        except:
            logging.error("file path related issue")

        logging.info("Creating CSC Profile using ADD form")
        self.driver.find_element_by_id("sbtCscprofilesAdded").click()
        time.sleep(2)
        BC = Select(self.driver.find_element_by_id("cmbSipprofileBusinessCompany"))
        BC.select_by_index(1)
        time.sleep(2)
        type = Decimal(b[4])
        logging.info("CSC Profile Type :",type)
        if (type==1):
            self.driver.find_element_by_id("rdoCSCProfiletype-1").click()
            Call_Manager = Select(self.driver.find_element_by_id("AllowServerPoolIP"))
            Call_Manager.select_by_index(1)
        else:
            Call_Manager = Select(self.driver.find_element_by_id("AllowServerPoolIP"))
            Call_Manager.select_by_index(1)
            self.driver.find_element_by_id("txtCSCPort").send_keys(Decimal(b[0]))

        self.driver.find_element_by_id("txtSipProfileName").send_keys(b[1])
        Media_IP = Select(self.driver.find_element_by_id("cmbMediaIP1"))
        Media_IP.select_by_index(1)
        self.driver.find_element_by_css_selector("#sbtCscprofilesadd > div.button_text").click()
        time.sleep(5)
        temp = self.driver.find_element_by_css_selector("body > div:nth-child(30) > div.ui-dialog-content.ui-widget-content")
        try:
            self.assertTrue(temp.text,'CSC Profile has been Added')
            return "PASS"
        except:
            return "FAIL"

        self.driver.find_element_by_class_name("ui-button-text").click()
        logging.info("CSC Profile added Successfully")

    def digit_rule(self):

        logging.info("Lets get started for digit rule Profile sub-module")

        try:
            logging.info("Reading data from xlsx file")
            x = "Read\Switch.xlsx"
            r = get_data(x,4)
            c = get_data(x,5)
            for i in range(0,len(c)):
                print "value of %s parameter is : %s"%(r[i],c[i])
                logging.info("value of %s parameter is : %s"%(r[i],c[i]))
            logging.info("Data reading functionality completed successfully")
        except:
            logging.error("file path related issue")

        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_css_selector("li.switch > a > div.menu_name").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("Digit Rule").click()
        time.sleep(5)
        logging.info("Creating digit rule using ADD form")
        self.driver.find_element_by_id("sbtRuleAdded").click()
        time.sleep(2)
        self.driver.find_element_by_id("txtDigitRuleName").send_keys(c[0])
        digit_rule_type = Decimal(c[8])
        if (digit_rule_type==1):
            logging.info("Creating vendor digit rule...")
            self.driver.find_element_by_id("rdoDigitRuleType-1").click()
        else:
            logging.info("Creating Customer digit rule..")
            self.driver.find_element_by_id("txtMinDNIDLength").clear()
            self.driver.find_element_by_id("txtMinDNIDLength").send_keys(Decimal(c[3]))
            self.driver.find_element_by_id("txtMaxDNIDLength").clear()
            self.driver.find_element_by_id("txtMaxDNIDLength").send_keys(Decimal(c[4]))

        self.driver.find_element_by_id("txtANI").send_keys(c[1])
        self.driver.find_element_by_id("txtDNID").send_keys(c[2])
        ANI_Rule = Select(self.driver.find_element_by_id("cmbANIRuleType"))
        ANI_Rule.select_by_index(0)
        ANI_Left_Strip = Select(self.driver.find_element_by_id("cmbANILeftStrip"))
        ANI_Left_Strip.select_by_index(1)
        ANI_Right_Strip = Select(self.driver.find_element_by_id("cmbANIRightStrip"))
        ANI_Right_Strip.select_by_index(1)
        DNID_Rule = Select(self.driver.find_element_by_id("cmbDNIDRuleType"))
        DNID_Rule.select_by_index(0)
        ANI_Left_Strip = Select(self.driver.find_element_by_id("cmbDNDILeftStrip"))
        ANI_Left_Strip.select_by_index(1)
        ANI_Right_Strip = Select(self.driver.find_element_by_id("cmbDNDIRightStrip"))
        ANI_Right_Strip.select_by_index(1)
        self.driver.find_element_by_css_selector("#sbtRuleadd > div.button_text").click()
        logging.info("Digit rule has been added Successfully")
        time.sleep(5)

        try:
            self.driver.find_element_by_class_name("ui-button-text").click()
            return "PASS"
        except:
            return "FAIL"


    def digit_rule_group(self):
        logging.info("Lets get started for digit rule group sub-module")
        try:
            logging.info("Reading data from xlsx file")
            x = "Read\Switch.xlsx"
            t = get_data(x,7)
            d = get_data(x,8)
            for i in range(0,len(d)):
                print "value of %s parameter is : %s"%(t[i],d[i])
                logging.info("value of %s parameter is : %s"%(t[i],d[i]))
            logging.info("Data reading functionality completed successfully")
        except:
            logging.error("file path related issue")

        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_css_selector("li.switch > a > div.menu_name").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("Digit Rule Group").click()
        time.sleep(3)
        self.driver.find_element_by_id("sbtRulegroupAdded").click()
        time.sleep(3)
        digit_rule_type = Decimal(d[1])
        if (digit_rule_type==1):
            logging.info("Creating vendor digit rule group...")
            self.driver.find_element_by_id("rdoDigitRuleType-1").click()
        else:
            logging.info("Creating Customer digit rule group...")

        self.driver.find_element_by_id("txtDigitRuleGroupName").send_keys(d[0])
        self.driver.find_element_by_name("rulegroup_listbox1[]").click()
        self.driver.find_element_by_css_selector("#sbtRulegroupadd > div.button_text").click()
        logging.info("Digit rule group has been added Successfully")
        time.sleep(5)
        try:
            self.driver.find_element_by_class_name("ui-button-text").click()
            return "PASS"
        except:
            return "FAIL"

    def Stop_Route_Profile(self):
        logging.info("Lets get started for stop route profile sub-module")
        try:
            logging.info("Reading data from xlsx file")
            x = "Read\Switch.xlsx"
            k = get_data(x,10)
            e = get_data(x,11)
            for i in range(0,len(e)):
                print "value of %s parameter is : %s"%(k[i],e[i])
                logging.info("value of %s parameter is : %s"%(k[i],e[i]))
            logging.info("Data reading functionality completed successfully")
        except:
            logging.error("file path related issue")

        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_css_selector("li.switch > a > div.menu_name").click()
        time.sleep(5)
        self.driver.find_element_by_link_text("Stop Route Profile").click()
        time.sleep(3)
        self.driver.find_element_by_id("sbtStoprouteprofileAdd").click()

        self.driver.find_element_by_id("txtStoprouteprofileName").send_keys(e[0])
        for i in range(1,3):
            x = i
            self.driver.find_elements_by_xpath("//input[@name='SipTrunkStopCauseCodesSearchList[]']")[x].click()

        for j in range(1,3):
            x = j
            self.driver.find_elements_by_xpath("//input[@name='SipGlobalStopCauseCodesSearchList[]']")[x].click()

        for k in range(1,3):
            x = k
            self.driver.find_elements_by_xpath("//input[@name='H323TrunkStopCauseCodesSearchList[]']")[x].click()

        for l in range(1,3):
            x = l
            self.driver.find_elements_by_xpath("//input[@name='H323GlobalStopCauseCodesSearchList[]']")[x].click()

    def Cause_Code_Profile(self):
        print "Cause code Profile start"
        self.driver.find_element_by_link_text("Cause Code Profile").click()
        time.sleep(3)
        self.driver.find_element_by_id("sbtCausecodeprofileAdd").click()

        x = "Read\Switch.xlsx"
        f =  get_data(x,9)
        for i in range(0,len(f)):
            print f[i]
        time.sleep(5)

        self.driver.find_element_by_id("txtCausecodeprofileName").send_keys(f[0])
        for i in range(1,3):
            x = i
            a = [400,401,402,403]
            self.driver.find_elements_by_xpath("//input[@name='SIPReceivedTOTransmitSIPCauseCodeID[]']")[x].clear()
            self.driver.find_elements_by_xpath("//input[@name='SIPReceivedTOTransmitSIPCauseCodeID[]']")[x].send_keys(a[i])

        for j in range(1,3):
            x = j
            m = [21,16,17,63]
            self.driver.find_elements_by_xpath("//input[@name='SIPReceivedTOTransmitH323CauseCodeID[]']")[x].clear()
            self.driver.find_elements_by_xpath("//input[@name='SIPReceivedTOTransmitH323CauseCodeID[]']")[x].send_keys(m[j])

        for k in range(1,3):
            x = k
            c = [488,503,404]
            self.driver.find_elements_by_xpath("//input[@name='H323ReceivedTOTransmitSIPCauseCodeID[]']")[x].clear()
            self.driver.find_elements_by_xpath("//input[@name='H323ReceivedTOTransmitSIPCauseCodeID[]']")[x].send_keys(c[k])

        for l in range(1,3):
            x = l
            d = [63,17,25]
            self.driver.find_elements_by_xpath("//input[@name='H323ReceivedTOTransmitH323CauseCodeID[]']")[x].clear()
            self.driver.find_elements_by_xpath("//input[@name='H323ReceivedTOTransmitH323CauseCodeID[]']")[x].send_keys(d[l])

    def SIP_Register(self):
        print "SIP Register start"
        self.driver.find_element_by_link_text("SIP Registrar").click()
        time.sleep(3)
        self.driver.find_element_by_id("sbtSipregistrarAdd").click()

        x = "Read\Switch.xlsx"
        g =  get_data(x,11)
        for i in range(0,len(g)):
            print g[i]
        time.sleep(5)

        TRUNK = Select(self.driver.find_element_by_id("cmbTrunkId"))
        TRUNK.select_by_index(1)
        time.sleep(2)
        DOMIN = Select(self.driver.find_element_by_id("cmbDomain"))
        DOMIN.select_by_index(1)
        self.driver.find_element_by_id("txtUsername").clear()
        self.driver.find_element_by_id("txtUsername").send_keys(g[0])
        self.driver.find_element_by_id("txtPassword").clear()
        self.driver.find_element_by_id("txtPassword").send_keys(g[1])
        self.driver.find_element_by_id("txtCapacity").send_keys(Decimal(g[2]))
        self.driver.find_element_by_id("txtCalls").send_keys(Decimal(g[3]))

    def LNP_Provider(self):
        print "LNP Provider start"
        self.driver.find_element_by_link_text("LNP Provider").click()
        time.sleep(3)
        self.driver.find_element_by_id("sbtLnpproviderAdded").click()

        x = "Read\Switch.xlsx"
        h =  get_data(x,13)
        for i in range(0,len(h)):
            print h[i]
        time.sleep(5)
        self.driver.find_element_by_id("txtLnpprovidername").send_keys(h[0])
        HUNT = Select(self.driver.find_element_by_id("cmbHuntingtype"))
        HUNT.select_by_index(1)
        RETRY = Select(self.driver.find_element_by_id("cmbResendtries"))
        RETRY.select_by_index(3)
        self.driver.find_element_by_id("txtProviderGatewayIP-0").send_keys(h[1])
        self.driver.find_element_by_id("txtProviderGatewayPort-0").send_keys(Decimal(h[2]))

    def test_main(self):
        logging.info("Switch Module execusion has started...")
        homepage = Homepage(self.driver)
        homepage.navigate()
        signup_form = homepage.getSignupForm()
        logging.info("iMax URL get successfully open")
        signup_form.setName("admin", "brijesh84")
        time.sleep(5)
        logging.info("You have successfully login to iMax")
        self.driver.find_element_by_css_selector("li.switch > a > div.menu_name").click()
        time.sleep(5)
        result_CSC = self.CSC_Profile()
        print "Test Case Pass/fail for CSC ADD Functionality: ",result_CSC
        logging.info("Add functionality of CSC Profile has been done successfully")
        time.sleep(5)
        result_rule = self.digit_rule()
        print "Test Case Pass/fail for Digit rule ADD functionality: ",result_rule
        logging.info("Add functionality of digit rule has been done successfully")
        time.sleep(5)
        result_rule_group = self.digit_rule_group()
        print "Test Case Pass/fail for Digit rule group ADD functionality: ",result_rule_group
        logging.info("Add functionality of digit rule group has been done successfully")
        '''
        self.Stop_Route_Profile()
        logging.info("Add functionality of Stop route profile has been done successfully")
        self.Cause_Code_Profile()
        logging.info("Add functionality of Cause code profile has been done successfully")
        self.SIP_Register()
        logging.info("Add functionality of SIP register has been done successfully")
        self.LNP_Provider()
        logging.info("Add functionality of LNP Provider has been done successfully")
        '''

        report = Report()
        report.WriteReportHeader()
        x = "Read\TCT.xlsx"
        TC_ID = get_data(x,1)
        TCT_ID = get_data(x,2)
        Summary = get_data(x,3)
        result = [result_CSC,result_rule]
        for i in range(len(TCT_ID)):
            report.AppendToReport(TC_ID[i],TCT_ID[i],Summary[i],result[i])
        report.WriteReportFooter()
        report.WriteToFile("Switch.html")


    def tearDown(self):
        self.driver.close()
        logging.info("Browser Closed Successfully with session ID : %s"%(self.driver.session_id))
        logging.info("============================================================================================")


if __name__ == "__main__":
    unittest.main()