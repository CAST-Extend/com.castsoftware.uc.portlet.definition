'''
Created on 6/27/2023

@author: Hugo JOBY - HJO
'''
import unittest
import cast.analysers.test

UA_NAME = 'JavaPortlet'

class Test(unittest.TestCase):

    def testRegisterPlugin(self):

        print("Launching Unit Test for Portlet Definition Analyzer")
        # Instanciate a UA analyzer for 'Batch' language defined by <category name="Batch" rid="4">

        print("Acquiring the analysis unit for the language '" + str(UA_NAME) + "'.")
        analysis = cast.analysers.test.UATestAnalysis(UA_NAME)
        print("Analysis unit acquired.")

        #add_selection for folder, absolute reference
        #analysis.add_selection('C:\CAST_Clients\ACMS\Development\DEV_14.2.1\CswDev\JOBS')
        
        #add_selection for folder under "tests" Eclipse folder, relative reference
        analysis.add_selection(r'samples')
        analysis.set_verbose(True)

        print("Running the analysis on the /samples folder..")
        analysis.run()
        print("Analysis completed..")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()