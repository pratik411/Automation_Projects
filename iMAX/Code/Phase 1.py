__author__ = 'Pratik'

import os
import unittest

import HTMLRunner
import Switch

direct = os.getcwd()
print(direct)

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):

        Phase1 = unittest.TestSuite()
        Phase1.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Switch.switch),
            #unittest.defaultTestLoader.loadTestsFromTestCase(Carrier.Carrier),
            #unittest.defaultTestLoader.loadTestsFromTestCase(Main_tab_access.All_tab),
            #unittest.defaultTestLoader.loadTestsFromTestCase(Monitoring_BF.Monitoring),
        ])

        outfile = open(direct + "\HTML Reports\Phase1.html", "w")

        runner1 =  HTMLRunner.HTMLTestRunner(
           stream=outfile,
           title='iMAX Version 1.6.2 Test Report',
           description='Functional Testing'
        )


        runner1.run(Phase1)
        #xmlrunner.XMLTestRunner(verbosity=2, output='reports').run(smoke_test)





if __name__ == '__main__':
    unittest.main()
