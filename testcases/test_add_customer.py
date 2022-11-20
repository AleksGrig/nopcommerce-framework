import pytest
import time
from selenium.webdriver.common.by import By
from pageobjects.login import Login
from pageobjects.add_customer import AddCustomer
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
import string
import random

class Test_003_AddCustomer:
  baseURL = ReadConfig.get_url()
  username = ReadConfig.get_username()
  password = ReadConfig.get_password()
  logger = LogGen.loggen()  

  @pytest.mark.sanity
  def test_addCustomer(self,setup):
    self.logger.info("************* Test_003_AddCustomer **********")
    self.driver=setup
    self.driver.get(self.baseURL)

    self.lp = Login(self.driver)
    self.lp.set_username(self.username)
    self.lp.set_password(self.password)
    self.lp.click_login()

    self.logger.info("************* Login succesful **********")
    self.logger.info("******* Starting Add Customer Test **********")

    self.addcust = AddCustomer(self.driver)
    self.addcust.clickOnCustomersMenu()
    self.addcust.clickOnCustomersMenuItem()
    self.addcust.clickOnAddnew()

    self.logger.info("************* Providing customer info **********")

    self.email = random_generator() + "@gmail.com"
    self.addcust.setEmail(self.email)
    self.addcust.setPassword("test123")
    self.addcust.setCustomerRoles("Registered")
    self.addcust.setManagerOfVendor("Vendor 2")
    self.addcust.setGender("Male")
    self.addcust.setFirstName("Pavan")
    self.addcust.setLastName("Kumar")
    self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
    self.addcust.setCompanyName("busyQA")
    self.addcust.setAdminContent("This is for testing.........")
    self.addcust.clickOnSave()

    self.logger.info("************* Saving customer info **********")
    self.logger.info("********* Add customer validation started *****************")

    try:
      self.driver.find_element(By.CSS_SELECTOR, "div.alert-success")
      assert True
      self.logger.info("********* Add customer Test Passed *********")
    except:
      self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")  
      self.logger.error("********* Add customer Test Failed ************")
      self.driver.close()
      assert False

    self.driver.close()
    self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
  return ''.join(random.choice(chars) for x in range(size))