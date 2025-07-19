from selenium import webdriver
from selenium.webdriver.common.by import By


class Homepage:
    link_signup_xpath= "//a[normalize-space()='Signup / Login']"
    link_signin_linktext="Sign In"
    Btn_signup="//a[normalize-space()='Signup / Login']"

    def __init__(self,driver):
        self.driver=driver

    def click_signup(self):

        self.driver.find_element(By.XPATH,self.link_signup_xpath).click()
        #self.driver.find_element(By.LINK_TEXT,self.link_signin_linktext).click()
    def click_signup_btn(self):
        self.driver.find_element(By.XPATH,self.Btn_signup).click()

