from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Account_Signup():
    txt_firstname_name="name"

    txt_email_xpath="//input[@data-qa='signup-email']"
    btn_signup_xpath="//button[normalize-space()='Signup']"
    chkbox_title_ID="id_gender1"
    txt_password_ID = "password"
    drp_day_ID="days"
    drp_month_ID = "months"
    drp_year_ID="years"
    txt_add_Fname_ID="first_name"
    txt_add_Lname_ID = "last_name"
    txt_add_Add1_ID="address1"
    drp_country_ID="country"
    txt_state_ID="state"
    txt_city_ID = "city"
    txt_zip_ID = "zipcode"
    txt_mobile_xpath="//input[@id='mobile_number']"
    btn_createaccount_xpath="//button[normalize-space()='Create Account']"
    confirmationmsg_xpath="//b[normalize-space()='Account Created!']"


    def __init__(self,driver):
        self.driver=driver


    def firstname(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setemail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def click_signup(self):
        self.driver.find_element(By.XPATH, self.btn_signup_xpath).click()

    def clickcheckbox(self):
        self.driver.find_element(By.ID,self.chkbox_title_ID).click()

    def password(self,password):
        self.driver.find_element(By.ID,self.txt_password_ID).send_keys(password)
    def DOB(self):
        drp_day=Select(self.driver.find_element(By.ID,self.drp_day_ID))
        drp_month=Select(self.driver.find_element(By.ID, self.drp_month_ID))
        drp_year=Select(self.driver.find_element(By.ID, self.drp_year_ID))
        return drp_day,drp_month,drp_year


    def setfirsnameinaddress(self,firstname):
        self.driver.find_element(By.ID,self.txt_add_Fname_ID).send_keys(firstname)

    def setlastnameinaddress(self,lastname):
        self.driver.find_element(By.ID,self.txt_add_Lname_ID).send_keys(lastname)

    def setaddress(self,address):
        self.driver.find_element(By.ID,self.txt_add_Add1_ID).send_keys(address)

    def setcountry(self):
        country_list=Select(self.driver.find_element(By.ID,self.drp_country_ID))
        return country_list
    def setstate(self,state):
        self.driver.find_element(By.ID,self.txt_state_ID).send_keys(state)

    def setcity(self,city):
        self.driver.find_element(By.ID,self.txt_city_ID).send_keys(city)

    def setzipcode(self,zipcode):
        self.driver.find_element(By.ID,self.txt_zip_ID).send_keys(zipcode)

    def setmobile(self,mobile):
        self.driver.find_element(By.XPATH,self.txt_mobile_xpath).send_keys(mobile)

    #def setmobile(self):
        self.driver.find_element(By.XPATH,self.txt_mobile_xpath)

    def createaccount(self):
        element=self.driver.find_element(By.XPATH,self.btn_createaccount_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.btn_createaccount_xpath)))
        self.driver.execute_script("arguments[0].click();", element)

    def getconfirmationmsg(self):

        try:

            return self.driver.find_element(By.XPATH,self.confirmationmsg_xpath).text
        except:
            None







