from selenium.webdriver.common.service import logger
import logging
import os
from datetime import datetime
from pageObjects.Homepage import Homepage
from pageObjects.AccountSignupPage import Account_Signup
from utilities import *
from utilities.customlogger import LogGen
from utilities.randomString import random_email
import pytest

from utilities.readproperties import Readconfig


class Test_001_Registration():
    logger= LogGen.loggen()  #for logging
    url=Readconfig.getAppUrl()
    name =Readconfig.getname()
    password= Readconfig.getpassword()
    setfirsnameinaddress=Readconfig.getFnameinaddress()
    setlastnameinaddress=Readconfig.getLnameinaddress()
    setaddress=Readconfig.getaddress()

    @pytest.mark.sanity
    def test_account_reg(self,setup):
        self.logger.info("*****Test_001_Registration started *******")
        self.driver=setup
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.hp=Homepage(self.driver)
        self.logger.info("*****signup started*******")

        self.hp.click_signup()
        self.accountsignup=Account_Signup(self.driver)
        self.logger.info("***** providing cx details for registration *******")

        self.accountsignup.firstname(self.name)
        email=random_email()
        print(f"Generated Email:{email}")

        self.accountsignup.setemail(email)
        self.accountsignup.click_signup()
        self.accountsignup.clickcheckbox()
        self.accountsignup.password(self.password)
        day_select, month_select, year_select=self.accountsignup.DOB()
        day_select.select_by_visible_text('30')
        month_select.select_by_visible_text("July")
        year_select.select_by_visible_text('1994')
        self.accountsignup.setfirsnameinaddress(self.setfirsnameinaddress)
        self.accountsignup.setlastnameinaddress(self.setlastnameinaddress)
        self.accountsignup.setaddress(self.setaddress)
        drp_country=self.accountsignup.setcountry()
        drp_country.select_by_visible_text("India")
        self.accountsignup.setstate("Karnataka")
        self.accountsignup.setcity("BLR")
        self.accountsignup.setzipcode("12345")
        self.accountsignup.setmobile("3454323454")
        self.accountsignup.createaccount()
        msg=self.accountsignup.getconfirmationmsg()
        print(msg)

        if msg== "ACCOUNT CREATED!":
            assert True
            self.driver.close()
            self.logger.info("***** account registration is passed *******")


        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"//screenshots//"+"test_account_reg.png")
            assert False
            self.logger.info("***** account registration is passed *******")
            self.driver.quit()
            self.logger.info("*****Test_001_Registration finished *******")
















