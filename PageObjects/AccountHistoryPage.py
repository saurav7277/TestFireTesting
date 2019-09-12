from configparser import ConfigParser


class AccountHistory(object):
    def __init__(self, driver):
        self.driver = driver

        # getting locator from configuration.ini file
        parser = ConfigParser()
        parser.read('configuration.ini')
        available_balance_locator = parser.get('locator', 'available_balance_locator')
        rent_balance_locator = parser.get('locator', 'rent_balance_locator')

        # defining elements
        self.available_balance = self.driver.find_element_by_xpath(available_balance_locator)
        self.rent = self.driver.find_element_by_xpath(rent_balance_locator)

    def getAvailableBalanceValue(self):
        return self.available_balance

    def getRentBalance(self):
        return self.rent
