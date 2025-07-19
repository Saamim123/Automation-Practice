from pageObjects.Homepage import Homepage
from pageObjects.AccountSignupPage import Account_Signup
from utilities import *
from utilities.customlogger import LogGen
from utilities.randomString import random_email
import pytest
import os
from utilities.readproperties import Readconfig


class Test_001_Registration:
    logger = LogGen.loggen()  # Initialize logger

    # Configuration values
    url = Readconfig.getAppUrl()
    name = Readconfig.getname()
    password = Readconfig.getpassword()
    setfirsnameinaddress = Readconfig.getFnameinaddress()
    setlastnameinaddress = Readconfig.getLnameinaddress()
    setaddress = Readconfig.getaddress()

    def test_account_reg(self, setup):
        self.logger.info("***** Test_001_Registration started *******")
        self.driver = setup
        try:
            self.logger.info(f"Navigating to URL: {self.url}")
            self.driver.get(self.url)
            self.driver.maximize_window()

            self.hp = Homepage(self.driver)
            self.logger.info("Clicking on signup button")
            self.hp.click_signup()

            self.accountsignup = Account_Signup(self.driver)
            self.logger.info("Providing customer details for registration")

            self.accountsignup.firstname(self.name)
            email = random_email()
            self.logger.info(f"Generated Email: {email}")

            self.accountsignup.setemail(email)
            self.accountsignup.click_signup()
            self.accountsignup.clickcheckbox()
            self.accountsignup.password(self.password)

            # Date of Birth selection
            day_select, month_select, year_select = self.accountsignup.DOB()
            day_select.select_by_visible_text('30')
            month_select.select_by_visible_text("July")
            year_select.select_by_visible_text('1994')

            # Address information
            self.accountsignup.setfirsnameinaddress(self.setfirsnameinaddress)
            self.accountsignup.setlastnameinaddress(self.setlastnameinaddress)
            self.accountsignup.setaddress(self.setaddress)

            # Country selection
            drp_country = self.accountsignup.setcountry()
            drp_country.select_by_visible_text("India")

            # Additional details
            self.accountsignup.setstate("Karnataka")
            self.accountsignup.setcity("BLR")
            self.accountsignup.setzipcode("12345")
            self.accountsignup.setmobile("3454323454")

            self.logger.info("Creating account")
            self.accountsignup.createaccount()

            msg = self.accountsignup.getconfirmationmsg()
            self.logger.info(f"Confirmation message received: {msg}")

            if msg == "ACCOUNT CREATED!":
                self.logger.info("***** Account registration passed *******")
                assert True
            else:
                self.logger.error("***** Account registration failed *******")
                screenshot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots",
                                               "test_account_reg.png")
                self.driver.save_screenshot(screenshot_path)
                assert False

        except Exception as e:
            self.logger.error(f"Exception occurred: {str(e)}", exc_info=True)
            raise e
        finally:
            self.driver.quit()
            self.logger.info("***** Test_001_Registration finished *******")