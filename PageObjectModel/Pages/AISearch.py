from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 
sys.path.append(r'C:\Users\Jerome\Desktop\Python Selenium')
from PageObjectModel.Locators.PageLocators import *
from constant import *

class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.normal_chat()

    def normal_chat(self):
        self.driver.find_element(By.ID , Locators.homepage_text_field).send_keys("What is Salina?")
        self.driver.implicitly_wait(WAITINGTIME)
        self.driver.find_element(By.ID , Locators.homepage_send_button).is_enabled()
        print("The button is enabled")
        print("The test is completed")
        self.driver.find_element(By.ID , Locators.homepage_send_button).click()


