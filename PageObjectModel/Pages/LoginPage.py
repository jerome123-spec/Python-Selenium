from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import sys 
sys.path.append(r'C:\Users\Jerome\Desktop\Python Selenium')
from constant import *
from PageObjectModel.Locators.PageLocators import *
import time

class LoginPage():


    def __init__ (self , driver):
        self.driver = driver
        self.driver.get(STAGING)
        self.TestLogin()

    def enter_username(self):
        self.driver.find_element(By.ID , Locators.username_textfield_id).send_keys(USERNAME)
        self.driver.implicitly_wait(WAITINGTIME)
    def enter_password(self):
        self.driver.find_element(By.ID, Locators.password_textfield_id).send_keys(PASSWORD)
        self.driver.implicitly_wait(WAITINGTIME)
    def click_login_button(self):
        self.driver.implicitly_wait(WAITINGTIME)
        self.driver.find_element(By. ID , Locators.login_button_id).click() 

    def TestLogin(self):
        self.enter_username()
        self.enter_password()
        self.click_login_button()