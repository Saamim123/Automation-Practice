
from pageObjects.LoginPage import Login
from utilities.customlogger import LogGen
from utilities.readproperties import Readconfig
import os
import pytest

class Test_Login:

    baseURL=Readconfig.getAppUrl()
    logger=LogGen.loggen()
    password = Readconfig.getpwd()
    username= Readconfig.getusername()

    @pytest.mark.regression
    def test_login_check(self,setup):

        self.logger.info("----test_002_login initiated----")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.logger.info("*****Login started*******")
        self.lp.clicklogin_signup()
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.targetpage=self.lp.isAutomationheaderdisplay()
        self.driver.quit()





