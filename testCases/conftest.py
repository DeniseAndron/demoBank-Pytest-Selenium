from selenium import webdriver
import pytest
from Drivers.Drivers import executables
from utilities.readProperties import ReadConfig

# pytest -v -s testCases/test_login.py --browser chrome or firefox and to run them in parallel type -n= number of testcases

@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        driver = webdriver.Chrome(executables.CHROME_EXECUTABLE_PATH, options = chrome_options)
    elif browser == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(executable_path= executables.FIREFOX_EXECUTABLE_PATH, options= firefox_options)
    else:
        driver = webdriver.Edge(executable_path= executables.EDGE_EXECUTABLE_PATH)
    return driver



def pytest_addoption(parser): #This will get the value from the hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #this will return the browser value to the setup method
    return request.config.getoption("--browser")


############ PyTest HTML Report ##############

#pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome

# Hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'demo Bank'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Denisa'

# Hook to delete/modify Environment info to HTML Report
@pytest.mark.optonalhook
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME', None)
    metadata.pop('Plugins', None)


