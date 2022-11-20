import pytest
from selenium import webdriver
from pageobjects.login import Login
from utilities.read_properties import ReadConfig
from utilities.custom_logger import LogGen
from utilities import excel_utils

class Test_002_DDT_Login:
  baseURL = ReadConfig.get_url()
  path = ".\\testdata\\login_data.xlsx"

  logger = LogGen.loggen()

  @pytest.mark.regression
  def test_ddt_login(self, setup):
    self.logger.info("********** Test_002_DDT_Login **********")
    self.logger.info("********** Verifying Login Functionality **********")
    self.driver = setup
    self.driver.get(self.baseURL)
    self.login_page = Login(self.driver)

    self.rows = excel_utils.getRowCount(self.path, "Sheet1")
    self.logger.info("!!!!!!!!!!!!! NUMBER OF ROWS {} !!!!!!!!!!!!!".format(self.rows))

    test_status = []

    for row in range(2, self.rows+1):
      self.username = excel_utils.readData(self.path, "Sheet1", row, 1)
      self.password = excel_utils.readData(self.path, "Sheet1", row, 2)
      self.expected_result = excel_utils.readData(self.path, "Sheet1", row, 3)

      self.login_page.set_username(self.username)
      self.login_page.set_password(self.password)
      self.login_page.click_login()
      actual_title = self.driver.title

      if actual_title == "Dashboard / nopCommerce administration":
        if self.expected_result == "Pass":
          self.logger.info("********** test passed **********")
          self.login_page.click_logout()
          test_status.append('Pass')
        else:
          self.logger.info("********** test failed **********")
          self.login_page.click_logout()
          test_status.append('Fail')
      else:
        if self.expected_result == "Pass":
          self.logger.info("********** test failed **********")
          test_status.append('Fail')
        else:
          self.logger.info("********** test passed **********")
          test_status.append('Pass')


    if "Fail" not in test_status:
      self.logger.info("<<<<<<<<<< Test_002_DDT_Login pass >>>>>>>>>>")
      self.driver.close()
      assert True
    else:
      self.logger.info("<<<<<<<<<< Test_002_DDT_Login fail >>>>>>>>>>")
      self.driver.close()
      assert False

    self.logger.info("********** End of Test_002_DDT_Login **********")


