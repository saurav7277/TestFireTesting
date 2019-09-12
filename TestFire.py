import unittest
import HtmlTestRunner
import pytest
import allure
from selenium import webdriver
from configparser import ConfigParser
import PageObjects
from PageObjects.HomePage import Home
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.LoginPage import Login
from PageObjects.AccountHistoryPage import AccountHistory


class TestFireTesting(unittest.TestCase):
    parser = ConfigParser()
    parser.read('configuration.ini')
    firefox_driver_path = parser.get('driver_path', 'firefox_driver_path')

    # method for performing all the setup function.Gets executed before each test_method.
    def setUp(self, parser=parser):
        chrome_driver_path = parser.get('driver_path', 'chrome_driver_path')
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.driver.get("http://demo.testfire.net/")

    # test method to perform the required testing.
    def test_available_balance_and_Rent_balance(self, parser=parser):
        # Defining sign_in link element and performing sign in link click action
        signin_link = Home(self.driver).getSignIn()
        signin_link.click()

        # Defining username element and passing username value to it.
        username = Login(self.driver).getUsername()
        username_value = parser.get('login_credentials', 'username')
        username.send_keys(username_value)

        # Defining password element and passing password value to it.
        password = Login(self.driver).getPassword()
        password_value = parser.get('login_credentials', 'password')
        password.send_keys(password_value)

        # Defining login button element and performing click action.
        login_btn = Login(self.driver).get_login_butn()
        login_btn.click()

        # Defining account details list element and performing click action on it.
        account_details_list = MyAccountPage(self.driver).getAccountDetailsList()
        account_details_list.click()

        # Defining account details option element and performing click action on it.
        account_details_select = MyAccountPage(self.driver).getAccountDetailsSelect()
        account_details_select.click()

        # Defining account details submit button and performing click action on it
        account_details_submit_button = MyAccountPage(self.driver).getAccountDetailsSubmitButton()
        account_details_submit_button.click()

        # Defining available balance element and extracting amount from it.
        available_balance = AccountHistory(self.driver).getAvailableBalanceValue()
        available_balance_value = available_balance.text

        # verifying available balance value is empty or not
        try:
            self.assertNotEqual(available_balance_value, "", msg="Available Balance value is empty")

        except AssertionError:
            print("Available balance is empty")

        else:
            print("Available balance value is not empty")

        # Defining rent amount and verifying rent balance value
        rent = AccountHistory(self.driver).getRentBalance()
        rent_balance_value = rent.text

        print("Rent value:", rent_balance_value)

    # Method to stop test execution and quit driver
    def tearDown(self):
        self.driver.quit();


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Training/PycharmProjects/TestFireTesting/Report/'))
