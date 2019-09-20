import unittest
import HtmlTestRunner
import pytest
import allure
from selenium import webdriver
from configparser import ConfigParser
import PageObjects
import nose
from PageObjects.HomePage import Home
from PageObjects.MyAccountPage import MyAccountPage
from PageObjects.LoginPage import Login
from PageObjects.AccountHistoryPage import AccountHistory


class TestFireTesting(unittest.TestCase):
    parser = ConfigParser()
    parser.read('configuration.ini')

    # method for performing all the setup function.Get executed before each test_method.
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        with nose.allure.step('Launching http://demo.testfire.net/ '):
            self.driver.get("http://demo.testfire.net/")

    # test method to perform the required testing.
    def test_available_balance_and_Rent_balance(self):
        with nose.allure.step('Clicking on sign_in link'):
            # Defining sign_in link element and performing sign in link click action
            signin_link = Home(self.driver).getSignIn()
            signin_link.click()

        with nose.allure.step('Entering username'):
            # Defining username element and passing username value to it.
            username = Login(self.driver).getUsername()
            username_value = self.parser.get('login_credentials', 'username')
            username.send_keys(username_value)

        with nose.allure.step('Entering password'):
            # Defining password element and passing password value to it.
            password = Login(self.driver).getPassword()
            password_value = self.parser.get('login_credentials', 'password')
            password.send_keys(password_value)

        with nose.allure.step('Clicking on login button'):
            # Defining login button element and performing click action.
            login_btn = Login(self.driver).get_login_butn()
            login_btn.click()

        with nose.allure.step('Clicking on account details list box'):
            # Defining account details list element and performing click action on it.
            account_details_list = MyAccountPage(self.driver).getAccountDetailsList()
            account_details_list.click()

        with nose.allure.step('Selecting one account type'):
            # Defining account details option element and performing click action on it.
            account_details_select = MyAccountPage(self.driver).getAccountDetailsSelect()
            account_details_select.click()

        with nose.allure.step('Clicking on GO button'):
            # Defining account details submit button and performing click action on it
            account_details_submit_button = MyAccountPage(self.driver).getAccountDetailsSubmitButton()
            account_details_submit_button.click()

        with nose.allure.step('Getting available balance value'):
            # Defining available balance element and extracting amount from it.
            available_balance = AccountHistory(self.driver).getAvailableBalanceValue()
            available_balance_value = available_balance.text

        with nose.allure.step('Verifying available balance value'):
            # verifying available balance value is empty or not
            self.assertNotEqual(available_balance_value, "", msg="Available Balance value is empty")
            print(available_balance_value)

        with nose.allure.step('Verifying Rent balance'):
            # Defining rent amount and verifying rent balance value
            rent = AccountHistory(self.driver).getRentBalance()
            rent_balance_value = rent.text
            print("Rent value:", rent_balance_value)

    # Method to stop test execution and quit driver
    def tearDown(self):
        self.driver.quit();


if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Training/PycharmProjects/TestFireTesting/Report/'))
    unittest.main()