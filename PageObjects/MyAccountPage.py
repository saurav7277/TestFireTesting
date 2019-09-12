from configparser import ConfigParser


class MyAccountPage(object):
    def __init__(self, driver):
        self.driver = driver

        # getting locator from configuration.ini file
        parser = ConfigParser()
        parser.read('configuration.ini')
        account_details_list_locator = parser.get('locator', 'account_details_locator')
        account_details_select_locator = parser.get('locator', 'account_details_select_locator')
        account_details_submit_button_locator = parser.get('locator', 'go_btn_locator')

        # Defining elements
        self.account_details_list = self.driver.find_element_by_name(account_details_list_locator)
        self.account_details_select = self.driver.find_element_by_xpath(account_details_select_locator)
        self.account_details_submit_button = self.driver.find_element_by_id(account_details_submit_button_locator)

    def getAccountDetailsList(self):
        return self.account_details_list

    def getAccountDetailsSelect(self):
        return self.account_details_select

    def getAccountDetailsSubmitButton(self):
        return self.account_details_submit_button
