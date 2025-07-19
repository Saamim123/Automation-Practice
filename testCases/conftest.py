import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
from pageObjects.LoginPage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import LogGen

# ---------------- Browser Setup Fixture ----------------
@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser...")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching Edge browser...")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser...")
    else:
        driver = webdriver.Chrome()
        print("Launching Chrome browser (default)...")

    driver.maximize_window()
    yield driver
    driver.quit()

"""
# ---------------- Login Fixture ----------------
@pytest.fixture()
def login(setup):
    driver = setup
    baseURL = Readconfig.getAppUrl()
    username = Readconfig.getusername()
    password = Readconfig.getpwd()
    logger = LogGen.loggen()

    logger.info("----Login Fixture Started----")
    driver.get(baseURL)

    lp = Login(driver)
    logger.info("***** Performing Login *****")
    lp.clicklogin_signup()
    lp.setusername(username)
    lp.setpassword(password)
    lp.clicklogin()
    logger.info("***** Login Successful *****")

    return driver  # Important: return driver so other tests can use it
"""


# ---------------- Get Browser from CLI ----------------
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# ---------------- HTML Report Setup ----------------
def pytest_configure(config):
    reports_dir = os.path.join(os.path.abspath(os.curdir), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    config.option.htmlpath = os.path.join(reports_dir, f"report_{timestamp}.html")

    if not hasattr(config, '_metadata'):
        config._metadata = {}
    config._metadata['Project Name'] = 'Test Automation'
    config._metadata['Module Name'] = 'Customer Login'
    config._metadata['Tester'] = 'Saamim'

def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Packages", None)
