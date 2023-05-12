import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomers:
    # create constractor driver
    def __init__(self, driver):
        self.driver = driver

    # to identify the locator of element of page
    lnk_customer_XPATH = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_submenucustomer_XPATH = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_newcustomer_XPATH = "//a[@class='btn btn-primary']"
    txtbox_email_XPATH = "//input[@id='Email']"
    txtbox_password_XPATH = "//input[@id='Password']"
    txtbox_firstname_XPATH = "//input[@id='FirstName']"
    txtbox_lastname_XPATH = "//input[@id='LastName']"
    txtbox_company_XPATH ="//input[@id='Company']"
    txtbox_comment_XPATH = "//textarea[@id='AdminComment']"
    rd_gender_male_XPATH = "//input[@id='Gender_Male']"
    rd_gender_fmale_XPATH ="//input[@id='Gender_Female']"
    box_tax_XPATH = "//label[@for='IsTaxExempt']"
    txt_birth_date_Xpath = "//input[@id='DateOfBirth']"
    box_active_XPATH = "//input[@id='Active']"
    btn_save_XPATH = "//button[@name='save']"
    list_newselter_XPATH = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    choices_xpath = "//*[@id='SelectedNewsletterSubscriptionStoreIds-list']/div[2]//ul//li"
    list_cust_roles = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    is_item_adm_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[1]"
    is_item_modertors_xpath= "//*[@id='SelectedCustomerRoleIds_listbox']/li[2]"
    is_item_Guests_xpath= "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    is_item_Registered_xpath= "//*[@id='SelectedCustomerRoleIds_listbox']/li[4]"
    is_item_Vendors_xpath= "//*[@id='SelectedCustomerRoleIds_listbox']/li[5]"
    list_manager_vendor_XPATH = "//select[@id='VendorId']"

    # add information action
    def selectNewsletters(self,value):
        self.driver.find_element(By.XPATH,self.list_newselter_XPATH).click()
        time.sleep(3)
        Newsletters = self.driver.find_elements(By.XPATH,self.choices_xpath)
        for new in Newsletters:
            if new.text == value:
                print(new.text)
                new.click()
                break

    def clickcustomer_menu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_XPATH).click()

    def clickcustomer_item(self):
        self.driver.find_element(By.XPATH, self.lnk_submenucustomer_XPATH).click()

    def clickonadd_cust(self):
        self.driver.find_element(By.XPATH, self.btn_add_newcustomer_XPATH).click()


    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtbox_email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.txtbox_email_XPATH).send_keys(email)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH,self.txtbox_password_XPATH).clear()
        self.driver.find_element(By.XPATH,self.txtbox_password_XPATH).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txtbox_firstname_XPATH).clear()
        self.driver.find_element(By.XPATH,self.txtbox_firstname_XPATH).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txtbox_lastname_XPATH).clear()
        self.driver.find_element(By.XPATH,self.txtbox_lastname_XPATH).send_keys(lastname)

    def setGender(self,gender):
        if gender == "male":
            self.driver.find_element(By.XPATH, self.rd_gender_male_XPATH).click()
        elif gender == "female":
            self.driver.find_element(By.XPATH, self.rd_gender_fmale_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.rd_gender_male_XPATH).click()

    def setDateBirth(self,date):
        self.driver.find_element(By.XPATH, self.txt_birth_date_Xpath).send_keys(date)

    def setcampanyName(self,campany):
        self.driver.find_element(By.XPATH, self.txtbox_company_XPATH).send_keys(campany)

    def setTax(self):
        self.driver.find_element(By.XPATH, self.box_tax_XPATH).click()

    def set_custRole(self,role):
        self.driver.find_element(By.XPATH, self.list_cust_roles).click()
        time.sleep(3)
        if role == "Registered":
            self.option = self.driver.find_element(By.XPATH,self.is_item_Registered_xpath)
        elif role == "Administrators":
            self.option = self.driver.find_element(By.XPATH,self.is_item_adm_xpath)
        elif role == "Moderators":
            self.option = self.driver.find_element(By.XPATH,self.is_item_modertors_xpath)

        elif role == "Vendors":
            self.option = self.driver.find_element(By.XPATH,self.is_item_Vendors_xpath)
        elif role == "Guests":
            time.sleep(3)
            # select reg or gueste
            self.driver.find_element(By.XPATH, "//span[@title='delete']").click()
            time.sleep(3)
            self.option = self.driver.find_element(By.XPATH,self.is_item_Guests_xpath)
        elif role == "Registered":
            self.option = self.driver.find_element(By.XPATH,self.is_item_Registered_xpath)
        else:
            self.option = self.driver.find_element(By.XPATH,self.is_item_Guests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.option)
        time.sleep(3)

    def setVendor(self,value):
        vendors = self.driver.find_element(By.XPATH, self.list_manager_vendor_XPATH)
        drop_option = Select(vendors)
        drop_option.select_by_visible_text(value)

    def addComment(self, text):
        self.driver.find_element(By.XPATH,self.txtbox_comment_XPATH).clear()
        self.driver.find_element(By.XPATH,self.txtbox_comment_XPATH).send_keys(text)

    def save_Customer(self):
        self.driver.find_element(By.XPATH,self.btn_save_XPATH).click()



