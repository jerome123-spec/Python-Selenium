from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PageObjectModel.Locators.PageLocators import *
from constant import *



class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.test_execute()
        print("COMPLETED")

    #Normal Chat
    def homepage_send_text(self):
        self.driver.find_element(By.ID , Locators.homepage_text_field).send_keys("What is Salina?")
        self.driver.implicitly_wait(WAITINGTIME)
    def assert_send_icon(self):
        self.driver.find_element(By.ID , Locators.homepage_send_button).is_enabled()
        print("The button is enabled")
        print("The test is completed")
        # time.sleep(1)
    def click_send_icon(self):
        self.driver.find_element(By.ID , Locators.homepage_send_button).click()

    def test_normal_chat(self):
        self.homepage_send_text()
        self.assert_send_icon()
        self.click_send_icon()
        time.sleep(30)  
  
    #Web Search 
    def chatroom_select_ai_search_button(self):
        # time.sleep(1)
        self.driver.find_element(By.ID , Locators.chatroom_select_ai_search).click()
    def select_search_option(self, value):
        self.driver.find_element(By.XPATH , f"//span[contains(text(),'{value}')]").click()
        # time.sleep(1)
    def chatroom_send_text(self, text):
        self.driver.find_element(By.ID ,Locators.chatroom_text_field).send_keys(text)
    def chatroom_click_send_icon(self):
        self.driver.find_element(By.ID , Locators.chatroom_send_button).click()
        
    def test_web_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Web Search")
        self.chatroom_send_text("Who is Hev Abi?")
        self.chatroom_click_send_icon()
        time.sleep(40)

    #Arxiv 
    def test_arxiv_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Arxiv")
        self.chatroom_send_text("What is computer science? provide some topics for it.")
        self.chatroom_click_send_icon()
        time.sleep(60)

    #Reddit
    def test_reddit_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Reddit")
        self.chatroom_send_text("What is the latest typhoon in the philippines?")
        self.chatroom_click_send_icon()
        time.sleep(60)

    #Youtube
    def test_youtube_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Youtube")
        self.chatroom_send_text("top 10 ai for 2024")
        self.chatroom_click_send_icon()
        time.sleep(60)
    
    #GenerataeImage
    def chatroom_click_select_menu(self):
        self.driver.find_element(By.ID , Locators.chatroom_select_menu_icon).click()
    def chatroom_generate_image(self):
        self.driver.find_element(By.ID , Locators.chatroom_generate_image).click()
    def chatroom_click_html(self):
        self.driver.find_element(By.XPATH, "//html[@lang='en']").click()

    def test_generate_image(self):
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        time.sleep(2)
        self.chatroom_click_html()
        time.sleep(2)
        self.chatroom_send_text("Best AI Logo 2024")
        self.chatroom_click_send_icon()
        time.sleep(40)


    #Final Execution
    def test_execute(self):
        self.test_normal_chat()
        self.test_web_search()
        self.test_arxiv_search()
        self.test_reddit_search()
        self.test_youtube_search()
        self.test_generate_image()


    
    

