from configparser import ConfigParser


class Home(object):
    def __init__(self, driver):
        self.driver = driver

        # Getting locator from configuration.ini file
        parser = ConfigParser()
        parser.read('configuration.ini')
        sign_in_locator = parser.get('locator', 'signin_locator')

        # defining sign_in element
        self.sign_in = self.driver.find_element_by_id(sign_in_locator)

    def getSignIn(self):
        return self.sign_in
