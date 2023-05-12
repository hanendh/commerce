from selenium import webdriver
from PageObjects.LoginPage import Login
from PageObjects.AddCustomersPage import AddCustomers
from Utilities.CustomLogger import LogGen
from Utilities.Readproperties import Config
from selenium.webdriver.common.by import By
import time
import random
import string


class Test_0003_AddCustomer:
    Url = Config.GetUrl()
    password = Config.GetPassword()
    Email = Config.GetEmail()
    logger = LogGen.loggen()
    def generate_email(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))
    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("********* Test_0003_AddCustomer ********* ")
        self.logger.info("********* launch browser  ********* ")
        self.driver = setup
        self.driver.get(self.Url)
        self.driver.maximize_window()
        self.logger.info("********* login test case ********* ")
        self.lp = Login(self.driver)
        self.lp.setUserName(self.Email)
        self.lp.setPassword(self.password)
        self.lp.login()
        self.logger.info("********* verifing addCustomer test case ********* ")
        self.cust = AddCustomers(self.driver)
        self.cust.clickcustomer_menu()
        time.sleep(3)
        self.cust.clickcustomer_item()
        self.cust.clickonadd_cust()
        self.logger.info("******* adding the info of customer********")
        self.email = generate_email() + "@gmail.com"
        self.cust.setEmail(self.email)
        self.cust.setpassword("1234552")
        self.cust.setFirstName("ahmed")
        self.cust.setLastName("dhifi")
        self.cust.setGender("female")
        self.cust.setDateBirth("07/05/1985")
        self.cust.setcampanyName("hadooc")
        self.cust.selectNewsletters("Test store 2")
        self.cust.set_custRole("Administrators")
        self.cust.setVendor("Vendor 1")
        self.cust.addComment("test pargh ")

        self.cust.save_Customer()
        time.sleep(5)
        self.logger.info("********** adding a customer***********")

        self.logger.info("****** verfication test case ******")
        self.msg = self.driver.find_element(By.TAG_NAME, "body")
        self.test = self.msg.text

        if 'customer has been added successfully.' in self.test:
            assert True
            self.driver.close()
            self.logger.info("****** customer added ****")
        else:
            # self.driver.get_screenshot_as_file("C:\projet\commerce\screenshot\\cust.png")
            self.driver.close()
            self.logger.info("****** add customer failed ****")
            assert False



# create methode randam that generate email

def generate_email(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))













