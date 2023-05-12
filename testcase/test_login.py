import time
from selenium import webdriver
import pytest
from PageObjects.LoginPage import Login
from Utilities.Readproperties import Config # USE  the method from readproperties
from Utilities.CustomLogger import LogGen
import pytest


class Test_TC01_Login:
    URL = Config.GetUrl() # don't create obj of class because it is static
    email = Config.GetEmail()
    password = Config.GetPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression

    def test_homepage(self, setup):

        self.logger.info("***********Test_TC01_Login***********")
        self.logger.info("*********** Verifying the homepage case ***********")

        self.driver = setup # define obj to setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***********  the homepage case is passed ***********")
        else:
            self.driver.save_screenshot("C:\projet\commerce\screenshot\\test_homepage.png")
            self.driver.close()
            self.logger.error("***********  the homepage case is failed ***********")
            assert False
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("*********** Verifying the login case ***********")

        self.driver = setup
        self.driver.get(self.URL)
        self.driver.maximize_window()
        # create obj to class login
        self.lp = Login(self.driver)  # class contain constructor

        self.lp.setUserName(self.email)
        self.lp.setPassword(self.password)
        self.lp.login()
        act_title = self.driver.title

        # check the title of each page and compare between it
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***********  the login case is passed ***********")

        else:
            self.driver.get_screenshot_as_file("C:\projet\commerce\screenshot\\test_login.png")
            self.driver.close()
            self.logger.error("***********  the login case is failed ***********")

            assert False