import time
from selenium.webdriver.common.by import By

class SearchCustomers:
    # create constractor driver
    def __init__(self, driver):
        self.driver = driver

        # to identify the locator of element of page
    customer_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p"
    searchBtn_XPATH = "//div[@class='search-text']"
    emailTxt_XPATH  = "//input[@id='SearchEmail']"
    firstnameTxt_XPATH = "//input[@id='SearchFirstName']"
    lastnameTxt_XPATH = "//input[@id='SearchLastName']"
    table_XPATH = "//div[@id='customers-grid_wrapper']"
    table_Rows_XPATH = "//div[@id='customers-grid_wrapper']//tr"
    table_Col_XPATH = "//div[@id='customers-grid_wrapper']//tr//td"

    def getemail(self,email):
        self.driver.find_element(By.XPATH,self.emailTxt_XPATH).clear()
        self.driver.find_element(By.XPATH,self.emailTxt_XPATH).send_keys(email)
    def getFirstName(self,name):
        self.driver.find_element(By.XPATH, self.firstnameTxt_XPATH).clear()
        self.driver.find_element(By.XPATH, self.firstnameTxt_XPATH).send_keys(name)
    def getlastName(self,lastname):
        self.driver.find_element(By.XPATH, self.lastnameTxt_XPATH).clear()
        self.driver.find_element(By.XPATH, self.lastnameTxt_XPATH).send_keys(lastname)
    def clickbtn(self):

        self.driver.find_element(By.XPATH, self.searchBtn_XPATH).click()
    # identify the number of rows in table
    def  getlenRows(self):
        return len(self.driver.find_elements(By.XPATH,self.table_Rows_XPATH))

    # identify the number of colunms in table
    def  getlenCols(self):
        return len(self.driver.find_elements(By.XPATH,self.table_Col_XPATH))

    def serchByEmail(self,email):
        flag = False
        for r in range(2,self.table_Rows_XPATH + 1):
            table = self.driver.find_element(By.XPATH,self.table_XPATH)
            emailcol = table.driver.find_element(By.XPATH,"//table[@id='customers-grid_wrapper']/tbody/tr["+str(r)+"]/td[2]").text
            time.sleep(5)
            if emailcol == email:
                flag = True
                time.sleep(5)
                break
        return flag
    def searchByName(self,name):
        flag = False
        for r in  range(1,self.table_Rows_XPATH + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            namecol = table.driver.find_element(By.XPATH,"//div[@id='customers-grid_wrapper']//tr[" + str(r) + "]//td[2]").text
            if namecol == name:
                flag = True
                break
        return flag

    # daydt_XPATH = "//select[@id='SearchDayOfBirth']"
    # regDtFROM_XPATH = "//input[@id='SearchRegistrationDateFrom']"
    # regDtTO_XPATH = "//input[@id='SearchRegistrationDateTo']"
    # LastActivityFrom_XPATH = "//input[@id='SearchLastActivityFrom']"
    # LastActivityTo_XPATH = "//input[@id='SearchLastActivityTo']"
    # camany_XPATH = "//input[@id='SearchCompany']"
    # address_XPATH = "//input[@id='SearchIpAddress']"
    # btnsearch_xpath = "//button[@id='search-customers']"
    # rloe_XPATH = "//div[@role='listbox']"
    # rolesList_xpath = "//*[@id='SelectedCustomerRoleIds-list']/div[2]//ul//li"





