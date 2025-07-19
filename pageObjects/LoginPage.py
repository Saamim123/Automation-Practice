
from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:

    link_signin_xpath="//a[normalize-space()='Signup / Login']"
    txt_username_xpath="//input[@data-qa='login-email']"
    txt_password_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[normalize-space()='Login']"
    header_automation_xpath="//div[@class='item active']//h2[contains(text(),'Full-Fledged practice website for Automation Engin')]"


    def __init__(self,driver):
        self.driver=driver

    def clicklogin_signup(self):
        self.driver.find_element(By.XPATH, self.link_signin_xpath).click()

    def setusername(self,username):
        self.driver.find_element(By.XPATH, self.txt_username_xpath).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
        Title=self.driver.title

    def isAutomationheaderdisplay(self):
        try:
            login_text=self.driver.find_element(By.XPATH,self.header_automation_xpath).is_displayed()


        except:
            return False





