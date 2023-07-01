from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        from selenium.webdriver.edge.service import Service
        service_obj = Service("drivers/edgedriver_win64/msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Edge(service=service_obj, options=options)
    elif browser == 'firefox':
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(
            "drivers/geckodriver-v0.32.0-win32/geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.binary_location = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
        driver = webdriver.Firefox(service=service_obj, options=options)
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


# pytest html report

# it's a hook for adding environment info to html report
def pytest_configure(config):
    # config._metadata['Project Name'] = 'nop commerce'
    # config._metadata['Module Name'] = 'Customers'
    # config._metadata['Tester'] = 'Alex'
    config._metadata = {
        "Tester": "Alex",
        "Project Name": "nop commerce",
        "Module Name": "Customers",
    }


# it's a hook for delete/modify environment info in html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)
