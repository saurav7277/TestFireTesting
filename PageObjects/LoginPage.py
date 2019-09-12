from selenium import webdriver
from configparser import ConfigParser


class Login(object):
    def __init__(self, driver):
        self.driver = driver

        # Getting locator from configuration.ini file
        parser = ConfigParser()
        parser.read('configuration.ini')
        username_locator = parser.get('locator', 'username_locator')
        password_locator = parser.get('locator', 'password_locator')
        login_btn_locator = parser.get('locator', 'login_btn_locator')

        # defining elements
        self.username = self.driver.find_element_by_id(username_locator)
        self.password = self.driver.find_element_by_name(password_locator)
        self.login_btn = self.driver.find_element_by_name(login_btn_locator)

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def get_login_butn(self):
        return self.login_btn
