from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest

@pytest.fixture()
def setup():
  service = Service("drivers/chromedriver_win32/chromedriver.exe")
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(service=service, options=options)
  driver.maximize_window()
  driver.implicitly_wait(10)
  return driver