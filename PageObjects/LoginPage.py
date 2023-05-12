# file define element web of page
from selenium.webdriver.common.by import By
class Login:
    # create constractor driver
    def __init__(self, driver):
        self.driver = driver

    # to identify the locator of element of page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout = "Logout"

    # implementer action
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout).click()
