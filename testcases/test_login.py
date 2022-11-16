import pytest
from selenium import webdriver
from pageobjects.login import Login

class Test_001_Login:
  baseURL = "https://admin-demo.nopcommerce.com/login"
  username = "admin@yourstore.com"
  password = "admin"

  def test_homepage_title(self, setup):
    self.driver = setup
    self.driver.get(self.baseURL)
    actual_title = self.driver.title
    if actual_title == "Your store. Login":
      self.driver.close()
      assert True
    else:
      self.driver.save_screenshot(".\\screenshots\\test_homepage_title.png")
      self.driver.close()
      assert False

  def test_login(self, setup):
    self.driver = setup
    self.driver.get(self.baseURL)
    self.login_page = Login(self.driver)
    self.login_page.set_username(self.username)
    self.login_page.set_password(self.password)
    self.login_page.click_login()
    actual_title = self.driver.title
    if actual_title == "Dashboard / nopCommerce administration":
      self.driver.close()
      assert True
    else:
      self.driver.save_screenshot(".\\screenshots\\test_login.png")
      self.driver.close()
      assert False