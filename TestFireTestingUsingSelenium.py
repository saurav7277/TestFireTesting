import unittest
import HtmlTestRunner
from selenium import webdriver
from configparser import ConfigParser



class TestFireTesting(unittest.TestCase):
    parser = ConfigParser()
    parser.read('configuration.ini')
    firefox_driver_path = parser.get('driver_path', 'firefox_driver_path')

    def setUp(self, parser=parser):
        chrome_driver_path = parser.get('driver_path', 'chrome_driver_path')
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get("http://demo.testfire.net/")


    def test_available_balance_and_Rent_balance(self, parser=parser):
        signin_locator = parser.get('locator', 'signin_locator')
        sigin_link = self.driver.find_element_by_id(signin_locator)
        sigin_link.click()

        username_locator = parser.get('locator', 'username_locator')
        username = self.driver.find_element_by_id(username_locator)
        username_value = parser.get('login_credentials', 'username')
        username.send_keys(username_value)

        password_locator = parser.get('locator', 'password_locator')
        password = self.driver.find_element_by_name(password_locator)
        password_value = parser.get('login_credentials', 'password')
        password.send_keys(password_value)

        login_btn_locator = parser.get('locator', 'login_btn_locator')
        login_btn = self.driver.find_element_by_name(login_btn_locator)
        login_btn.click()

        account_details_list_locator = parser.get('locator', 'account_details_locator')
        account_details_list = self.driver.find_element_by_name(account_details_list_locator)
        account_details_list.click()

        account_details_select_locator = parser.get('locator', 'account_details_select_locator')
        account_details_select = self.driver.find_element_by_xpath(account_details_select_locator)
        account_details_select.click()

        account_details_submit_button_locator = parser.get('locator', 'go_btn_locator')
        account_details_submit_button = self.driver.find_element_by_id(account_details_submit_button_locator)
        account_details_submit_button.click()

        available_balance_locator = parser.get('locator', 'available_balance_locator')
        available_balance = self.driver.find_element_by_xpath(available_balance_locator)
        available_balance_value = available_balance.text

        try:
            self.assertNotEqual(available_balance_value, "", msg="Available Balance value is empty")

        except AssertionError:
            print("Available balance is empty")

        else:
            print("Available balance value is not empty")

        rent_balance_locator = parser.get('locator', 'rent_balance_locator')
        rent = self.driver.find_element_by_xpath(rent_balance_locator)
        rent_balance_value = rent.text

        print("Rent value:", rent_balance_value)


    def tearDown(self):
        self.driver.quit();


suite = unittest.TestLoader().loadTestsFromTestCase(TestFireTesting)
unittest.TextTestRunner(verbosity=2)
runner = HtmlTestRunner.HTMLTestRunner(output='C:/Users/Training/PycharmProjects/TestFireTesting/Report/')
runner.run(suite)
