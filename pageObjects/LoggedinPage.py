from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_Login_DDT:

    link_logout_linktext="logout"

    def __init__(self,driver):
        self.driver=driver


    def logout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()


