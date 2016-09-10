__author__ = 'Pratik'
import urllib2
from cStringIO import StringIO
class Report(object):
    _report_string=None

    def __init__(self):
        self._report_string=""

        # Write Report Header
    def WriteReportHeader(self):


        self._report_string+="<html><body><h1>Welcome to iMAX</h1><p>iMAX Automation Report.</p></body></html>"
        self._report_string+="<!DOCTYPE html><html><body><a href=\"http://www.google.com\">google link</a></body></html>"
        self._report_string+="<!DOCTYPE html><html><body><img src=\"abc.png\" alt=\"W3Schools.com\" width=\"104\" height=\"142\"></body></html>"
        self._report_string+="<html><header><title>Test Result Report</title></header><body>"
        self._report_string+="<table border=\"5\">"
        self._report_string+="<tr>"
        self._report_string+="<td>Test ID</td>"
        self._report_string+="<td>Test Case</td>"
        self._report_string+="<td>Action</td>"
        self._report_string+="<td>Pass/Fail</td>"
        self._report_string+="<tr>"

        #Append to report
    def AppendToReport(self,test_id,test_case_name,action,pass_fail):
        if(pass_fail.lower()=='pass'):
            self._report_string+="<tr style=\"background-color:#33cc33\">"
        else:
            self._report_string+="<tr style=\"background-color:#FFFF00\">"
        self._report_string+="<td>"+ test_id + "</td>"
        self._report_string+="<td>"+ test_case_name +"</td>"
        self._report_string+="<td>"+ action +"</td>"
        self._report_string+="<td>"+ pass_fail +"</td>"
        self._report_string+="<tr>"

        #write footer
    def WriteReportFooter(self):
        self._report_string+="</table></body></html>"

        #Write to file
    def WriteToFile(self,filename):
        final_string=self._report_string
        report_file =open(filename,'w')
        report_file.write(final_string)
        report_file.close()

