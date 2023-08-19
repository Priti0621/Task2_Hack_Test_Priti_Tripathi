import json
import time
import unittest
from selenium import webdriver
from Task2_automation.page_class.ecommerce_login_page import NopCommerce


class LoginTestClass(unittest.TestCase):
    driver = None
    data_dict = None

    @classmethod
    def setUpClass(cls) -> None:
        print("Launching chrome browser before all  test cases")
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(40)
        cls.driver.maximize_window()
        cls.driver.get("https://demo.nopcommerce.com/")

        json_file_path = "C:\\Users\\Hp\\PycharmProjects\\pythonProjectLect1\\Task2_automation\\credential.json"
        with open(json_file_path) as json_file:
            cls.data_dict = json.load(json_file)

    @classmethod
    def tearDownClass(cls) -> None:
        print("I am after the test class")

    # Test case_1 : Successfull login
    def test_successfull_login(self):
        nopcobject = NopCommerce(self.driver)
        nopcobject.click_login_link()
        nopcobject.click_login_link()
        nopcobject.input_emailid(self.data_dict.get("Login_test").get("correct_email_id"))
        nopcobject.input_password(self.data_dict.get("Login_test").get("correct_password"))
        nopcobject.click_login_button()
        time.sleep(20)

    # Test case_2 : Not a valid user / Invalid user
    def test_invalid_user(self):
        nopcobject = NopCommerce(self.driver)
        nopcobject.click_login_link()
        nopcobject.input_emailid(self.data_dict.get("Login_test").get("incorrect_email_id"))
        nopcobject.input_password(self.data_dict.get("Login_test").get("correct_password"))
        nopcobject.click_login_button()
        time.sleep(20)

    # Test case_3 : Incorrect password /Invalid password
    def test_incorrect_passowrd(self):
        nopcobject = NopCommerce(self.driver)
        nopcobject.click_login_link()
        nopcobject.input_emailid(self.data_dict.get("Login_test").get("correct_email_id"))
        nopcobject.input_password(self.data_dict.get("Login_test").get("incorrect_password"))
        nopcobject.click_login_button()
        time.sleep(20)
        
    # Test_case_4 : Verify_empty_fields
    def validate_empty_fields(self):
        nopcobject = NopCommerce(self.driver)
        nopcobject.click_login_link()
        nopcobject.click_login_button()
        assert nopcobject.verify_empty_fields()

