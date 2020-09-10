from selenium import webdriver
from utilities.utility import *
from utilities.readProperties import readConfig
from utilities.nopCommerceLogger import LogGeneration
import pytest

logger = LogGeneration.loggen()

@pytest.fixture
def setup(browser):
    if browser == "chrome":
        logger.info("Running test on Chrome browser")
        logger.info(readConfig.chrome_driver_path())
        driver = webdriver.Chrome("{0}".format(readConfig.chrome_driver_path()))
    elif browser == "firefox":
        logger.info("Running test on firefox browser")
        logger.info(readConfig.firefox_driver_path())
        driver = webdriver.Firefox(executable_path=r"{0}".format(readConfig.firefox_driver_path()))
    else:
        driver = webdriver.Firefox(executable_path=r"{0}".format(readConfig.firefox_driver_path()))
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    '''
    It is hook for adding environment info to the HTML report
    :param config: Configure the html report
    :return:
    '''
    config._metadata['Project Name'] = 'NOP COMMERCE'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'MandarK'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    '''
    Hook for delete/modify environment info to the HTML report
    :param metadata:
    :return:
    '''
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



