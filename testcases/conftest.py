from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
  if browser == 'edge':
    from selenium.webdriver.edge.service import Service
    service_obj = Service("drivers/edgedriver_win64/msedgedriver.exe")
    options = webdriver.EdgeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Edge(service=service_obj,options=options)
  elif browser == 'firefox':
    from selenium.webdriver.firefox.service import Service
    service_obj = Service("drivers/geckodriver-v0.32.0-win32/geckodriver.exe")
    options = webdriver.FirefoxOptions()
    options.binary_location = 'C:\Program Files\Mozilla Firefox\\firefox.exe'
    driver = webdriver.Firefox(service=service_obj,options=options)
  else:
    from selenium.webdriver.chrome.service import Service
    service = Service("drivers/chromedriver_win32/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=service, options=options)
  driver.maximize_window()
  driver.implicitly_wait(10)
  return driver

# getting value from CLI
def pytest_addoption(parser):
  parser.addoption("--browser")

# returning --browser option to setup method
@pytest.fixture()
def browser(request):
  return request.config.getoption("--browser")