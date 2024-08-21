from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PageObjectModel.Locators.PageLocators import *
from constant import *


class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.test_normal_chat()
        self.test_web_search()
        self.test_arxiv_search()

       
    #Normal Chat
    def homepage_send_text(self):
        self.driver.find_element(By.ID , Locators.homepage_text_field).send_keys("What is Salina?")
        self.driver.implicitly_wait(WAITINGTIME)
    def assert_send_icon(self):
        self.driver.find_element(By.ID , Locators.homepage_send_button).is_enabled()
        print("The button is enabled")
        print("The test is completed")
        time.sleep(1)
    def click_send_icon(self):
        self.driver.find_element(By.ID , Locators.homepage_send_button).click()
    def normal_wait_for_processing(self):
        time.sleep(30)

    def test_normal_chat(self):
        self.homepage_send_text()
        self.assert_send_icon()
        self.click_send_icon()
        self.normal_wait_for_processing()    
  
    #Web Search 
    def chatroom_select_ai_search_button(self):
        self.driver.find_element(By.ID , Locators.chatroom_select_ai_search).click()
        time.sleep(1)
    def select_web_search_option(self):
        self.driver.find_element(By.XPATH , "//span[contains(text(),'Web Search')]").click()
        time.sleep(1)
    def chatroom_send_text_web(self):
        self.driver.find_element(By.ID ,Locators.chatroom_text_field).send_keys("Who is Hev Abi?")
    def chatroom_web_click_send_icon(self):
        self.driver.find_element(By.ID , Locators.chatroom_send_button).click()
    def chatroom_web_wait_for_processing(self):
        time.sleep(30)

    def test_web_search(self):
        self.chatroom_select_ai_search_button()
        self.select_web_search_option()
        self.chatroom_send_text_web()
        self.chatroom_web_click_send_icon()
        self.chatroom_web_wait_for_processing()

    #Arxiv 
    def chatroom_select_ai_search_button1(self):
        self.driver.find_element(By.ID , Locators.chatroom_select_ai_search).click()
        time.sleep(1)
    def select_arxiv_search_option(self):
        self.driver.find_element(By.XPATH ,"//span[contains(text(),'Arxiv')]" ).click()
        time.sleep(1)
    def chatroom_send_text_arxiv(self):
        self.driver.find_element(By.ID , Locators.chatroom_text_field).send_keys("What is computer science? provide some topics for it.")
    def chatroom_arxiv_send_button(self):
        self.driver.find_element(By.ID , Locators.chatroom_send_button).click()
    def chatroom_arxiv_wait_for_processing(self):
        time.sleep(30)    


    def test_arxiv_search(self):
        self.chatroom_select_ai_search_button1()
        self.select_arxiv_search_option()
        self.chatroom_send_text_arxiv()
        self.chatroom_arxiv_send_button()
        self.chatroom_arxiv_wait_for_processing()
    
    

