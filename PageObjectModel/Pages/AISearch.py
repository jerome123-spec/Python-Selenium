from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 
sys.path.append(r'C:\Users\Jerome\Desktop\Python-Selenium')
from PageObjectModel.Locators.PageLocators import *
from constant import *

class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.normal_chat()
        # self.ai_search()

    def normal_chat(self):
        self.driver.find_element(By.ID , Locators.homepage_text_field).send_keys("What is Salina?")
        self.driver.implicitly_wait(WAITINGTIME)
        self.driver.find_element(By.ID , Locators.homepage_send_button).is_enabled()
        print("The button is enabled")
        print("The test is completed")
        time.sleep(1)
        self.driver.find_element(By.ID , Locators.homepage_send_button).click()
        time.sleep(30)
        # self.driver.find_element(By.ID , Locators.chatroom_select_ai_search).click()
        self.driver.find_element(By.XPATH , "//button[@id='source-button-chatroom']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH , "//span[contains(text(),'Web Search')]").click()
        time.sleep(5)
        print("The Test completed")

    # def ai_search(self):
    #     time.sleep(60)
    #     self.driver.find_element(By.ID , Locators.chatroom_select_ai_search).click()
    #     self.driver.find_element(By.XPATH , "//button[contains(text(), 'Web Search')]").click()

