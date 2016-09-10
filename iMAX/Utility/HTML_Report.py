__author__ = 'Pratik'
from TestResultUtility import Report
import unittest
from selenium import webdriver


def browser():
    temp=1
    if (temp>2):
        #driver = webdriver.Chrome()
        #driver.maximize_window()
        #driver.get('https://www.google.com')
        2+2>5
        return "pass"
    else:
        return "fail"


report=Report()
report.WriteReportHeader()
print browser()
report.AppendToReport("001","Login","click on login button",browser())
report.WriteReportFooter()
report.WriteToFile("TestResult.html")

