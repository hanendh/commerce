import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import Login
from Utilities.Readproperties import Config # USE  the method from readproperties
from Utilities.CustomLogger import LogGen # creation of logging
from Utilities import XlUtilies


class Test_TC02_Login_ddt:
    URL = Config.GetUrl() # don't create obj of class because it is static
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("*********** Test_TC02_Login_ddt ***********")
        self.logger.info("*********** Verifying the login case ddt ***********")

        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()

        # create obj to class login
        self.lp = Login(self.driver)  # class contain constructor

        # step 1: count the rows
        self.rows = XlUtilies.getRowCount(self.path,"Feuil1")
        # step 2 : create list
        list_status = [] #Empty list of test driven

        # step 3:  loop for test all data of file

        for r in range(2, self.rows+1):
            self.usernames = XlUtilies.ReadData(self.path,"Feuil1",r,1) # read the users
            self.passwords = XlUtilies.ReadData(self.path, "Feuil1", r, 2) # read password of user
            self.exp = XlUtilies.ReadData(self.path, "Feuil1", r, 3) # read expected of test case
            self.lp.setUserName(self.usernames)
            self.lp.setPassword(self.passwords)
            self.lp.login()
            time.sleep(5)
            act_title = self.driver.title
            expt_title = "Dashboard / nopCommerce administration"

            # step 4: validation of test case
            if act_title == expt_title: # test the test case
                if self.exp == "Pass": # test data driven (data in excel)
                    self.logger.info("*** test-case is passed ***")
                    self.lp.logout();
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("******** Fail ***")
                    self.lp.logout()
                    list_status.append("Fail")  #test case ddt is failed

            elif act_title != expt_title: # test the test case
                if self.exp == "Pass": # test data driven (data in excel)
                    self.logger.info("******** test-case is failed")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("******** passed *******")
                    list_status.append("Pass") #test case ddt is passed

    #*************************** VALIDATION OF tEST CASE LOGIN 3***************************

        if "Fail" not in list_status:
            self.logger.info("************ test case login is passed ************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************ test case login is passed ************")
            self.driver.close()
            assert False

        self.logger.info("*********** Test_TC02_Login_ddt is finished ***********")
        self.logger.info("*********** End of Test_TC02_Login_ddt  ***********")








