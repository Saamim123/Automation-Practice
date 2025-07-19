import time

from pageObjects.LoggedinPage import Test_Login_DDT
from pageObjects.LoginPage import Login
from pageObjects.Homepage import Homepage
from pageObjects.AccountSignupPage import Account_Signup

import os

from utilities.customlogger import LogGen
from utilities.readproperties import Readconfig
from utilities import xlutilities

class Test_login_DDT:

    baseURL=Readconfig.getAppUrl()
    logger = LogGen.loggen()
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "testdata", "Credentials.xlsx")
    password = Readconfig.getpwd()
    username = Readconfig.getusername()

    def test_login_DDT(self,setup):
        self.logger.info("----test_002_login initiated----")

        self.rows=xlutilities.getRowCount(self.file_path,'Sheet1')
        lst_status=[]
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp=Homepage(self.driver)
        self.lp=Login(self.driver)
        self.loginddt=Test_Login_DDT(self.driver)
        for r in range(2,self.rows+1):
            self.loginddt.logout()
            self.lp.clicklogin_signup()

            self.email=xlutilities.readData(self.file_path,"Sheet1",r,1)
            self.password = xlutilities.readData(self.file_path, "Sheet1", r, 2)
            self.exp = xlutilities.readData(self.file_path, "Sheet1", r, 3)
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(3)
            self.targetpage = self.lp.isAutomationheaderdisplay()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=='Invalid':
                if self.targetpage == True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("******* End of test_003_login_Datadriven **********")
























