import time
import pytest
from pageobjects.login import Login
from pageobjects.add_customer import AddCustomer
from pageobjects.search_customer import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen

class Test_SearchCustomerByName_005:
  baseURL = ReadConfig.get_url()
  username = ReadConfig.get_username()
  password = ReadConfig.get_password()
  logger = LogGen.loggen()  

  def test_searchCustomerByName(self,setup):
    self.logger.info("************* SearchCustomerByName_005 **********")
    self.driver=setup
    self.driver.get(self.baseURL)

    self.lp = Login(self.driver)
    self.lp.set_username(self.username)
    self.lp.set_password(self.password)
    self.lp.click_login()
    self.logger.info("************* Login succesful **********")

    self.logger.info("******* Starting Search Customer By Name **********")

    self.addcust = AddCustomer(self.driver)
    self.addcust.clickOnCustomersMenu()
    self.addcust.clickOnCustomersMenuItem()

    self.logger.info("************* searching customer by name **********")
    searchcust = SearchCustomer(self.driver)
    searchcust.setFirstName("Victoria")
    searchcust.setLastName("Terces")
    searchcust.clickSearch()
    # time.sleep(5)
    status=searchcust.searchCustomerByName("Victoria Terces")
    self.driver.close()
    assert True==status
    self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")