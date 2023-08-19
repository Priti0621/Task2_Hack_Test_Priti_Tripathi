from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class NopCommerce:

    def __init__(self,driver):
        self.login_driver = driver

    login_link_locator = "//a[text()='Log in']"
    email_id_locator = "//input[@id='Email']"
    password_locator = "//input[@id='Password']"
    login_button_locator = "//button[text()='Log in']"
    incorrect_email_id_locator = "//span[text()='Wrong email']"
    incorrect_password_locator = "//div[text()='Login was unsuccessful. Please correct the errors and try again.']"
    empty_emailid_locator = "//span[text()='Please enter your email']"

    def click_login_link(self):
            self.login_driver.find_element(By.XPATH, self.login_link_locator).click()

    def input_emailid(self, email):
            self.login_driver.find_element(By.XPATH, self.email_id_locator).send_keys(email)

    def input_password(self, password):
            self.login_driver.find_element(By.XPATH, self.password_locator).send_keys(password)

    def click_login_button(self):
            self.login_driver.find_element(By.XPATH, self.login_button_locator).click()

    def invalid_email_id(self, emailid):
        self.login_driver.find_element(By.XPATH, self.incorrect_email_id_locator).send_keys(emailid)

    def invalid_password(self, password):
        self.login_driver.find_element(By.XPATH, self.incorrect_password_locator).send_keys(password)

    def verify_empty_fields(self):
        invalid_element = WebDriverWait(self.login_driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                         self.empty_emailid_locator)))
        return invalid_element