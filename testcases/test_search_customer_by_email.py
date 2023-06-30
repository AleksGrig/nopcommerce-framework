import time
import pytest
from pageobjects.login import Login
from pageobjects.add_customer import AddCustomer
from pageobjects.search_customer import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************* SearchCustomerByEmail_004 **********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        self.logger.info("************* Login succesful **********")

        self.logger.info(
            "******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.logger.info(
            "************* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        status = searchcust.searchCustomerByEmail(
            "victoria_victoria@nopCommerce.com")
        self.driver.close()
        assert True == status
        self.logger.info(
            "***************  TC_SearchCustomerByEmail_004 Finished  *********** ")
