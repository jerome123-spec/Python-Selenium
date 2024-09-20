from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from PageObjectModel.Locators.PageLocators import *
from constant import *
from selenium.common.exceptions import NoSuchElementException





class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.test_execute()
       

    #Normal Chat
    def homepage_send_text(self):
        self.driver.find_element(By.ID , Locators.homepage_text_field).send_keys("What is Salina?")
        self.driver.implicitly_wait(WAITINGTIME)
    def assert_send_icon(self):
        send_icon = self.driver.find_element(By.ID , Locators.homepage_send_button)
        send_icon.is_enabled()
    def homepage_click_send_icon(self):
        self.driver.find_element(By.ID , Locators.homepage_send_button).click()

    def test_normal_chat(self):
        self.homepage_send_text()
        self.assert_send_icon()
        self.homepage_click_send_icon()
        time.sleep(WAITINGNORMALRESPONSE)  
  
    #Web Search 
    def chatroom_select_ai_search_button(self):
        self.driver.find_element(By.ID, Locators.chatroom_select_ai_search).click()
    def select_search_option(self, value):
        self.driver.find_element(By.XPATH , f"//span[contains(text(),'{value}')]").click()
    def chatroom_send_text(self, text_send_keys):
        self.driver.find_element(By.ID ,Locators.chatroom_text_field).send_keys(text_send_keys)
    def chatroom_click_send_icon(self):
        self.driver.find_element(By.ID , Locators.chatroom_send_button).click()
        
    def test_web_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Web Search")
        self.chatroom_send_text("Could you provide a current (2024) definition of AI and suggest some relevant topics for research or discussion in this field?")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)
        
    #Arxiv 
    def test_arxiv_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Arxiv")
        self.chatroom_send_text("What is computer science? provide some topics for it in bullet form format.")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)

    #Reddit
    def test_reddit_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Reddit")
        self.chatroom_send_text("how ai being used in the world today?")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)

    #Youtube
    def test_youtube_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Youtube")
        self.chatroom_send_text("top 10 automation testing for 2024")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)
    
    #Wikipedia
    def test_wikipedia_search(self):
        self.chatroom_select_ai_search_button()
        self.select_search_option("Wikipedia")
        self.chatroom_send_text("In what ways is AI being used to address global challenges such as poverty, education, and climate change?")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)
    
    #Generatae Image
    def chatroom_click_select_menu(self):
        self.driver.find_element(By.ID , Locators.chatroom_select_menu_icon).click()
    def chatroom_generate_image(self):
        self.driver.find_element(By.ID , Locators.chatroom_generate_image).click()
    def chatroom_click_html(self):
        self.driver.find_element(By.XPATH, "//html[@lang='en']").click()
        

    def test_generate_image(self):
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_html()
        self.chatroom_send_text("Best AI Logo 2024")
        self.chatroom_click_send_icon()
        time.sleep(40)    

    #Suggested Replies (Disabled)
    def chatroom_click_off_suggested_replies(self):
        self.driver.find_element(By.ID , Locators.chatroom_suggested_replies).click()
    
    def test_off_suggested_replies(self):
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_off_suggested_replies()
        self.chatroom_click_html()
        self.chatroom_select_ai_search_button()
        self.select_search_option("Salina Assistant")
        self.chatroom_send_text("Can you please give me a top 5 ai tools? and what are the main features each of one.")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGNORMALRESPONSE)

    #File Document Upload
    def chatroom_click_select_attachment(self):
        attachment = self.driver.find_element(By.XPATH , "//button[@id='attachments-button-chatroom']")
        self.driver.execute_script("arguments[0].focus()",attachment)
        attachment.click()
    def chatroom_click_file_button(self):
        self.driver.find_element(By.ID , Locators.chatroom_select_file_document).click()
    def upload_process(self):
        fineinput = self.driver.find_element(By.NAME , Locators.chatroom_file_input)
        self.file_path = AI_SEARCH_DOCUMENTS_ATTACHMENT
        fineinput.send_keys(self.file_path)
    def click_upload_button(self):
        self.driver.find_element(By.ID , Locators.chatroom_upload_button).click()

    def test_file_upload(self):
        self.chatroom_click_select_attachment()
        self.chatroom_click_file_button()
        self.upload_process()
        self.click_upload_button()
        time.sleep(FILE_ATTACHMENT)
        self.chatroom_send_text("What is the uploaded file document about?")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)

    #Select Agent
    def click_agent_icon(self):
        self.driver.find_element(By.ID , Locators.chatroom_agent_icon).click()
    def chatroom_select_agent(self):
        self.driver.find_element(By.ID , Locators.chatbot_agent_selected).click()

    def test_select_agent(self):
        self.click_agent_icon()
        self.chatroom_select_agent()
        time.sleep(10)
        self.chatroom_send_text("give me more context about the uploaded file documents but in the format bullet form.")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)
 
    #Go to Homepage
    def test_go_to_homepage(self):
        self.driver.find_element(By.ID , Locators.click_homepage).click()
        time.sleep(5)

    #Test Execution
    def test_execute(self):
       self.test_normal_chat()
       self.test_web_search()
       self.test_arxiv_search()
       self.test_reddit_search()
       self.test_youtube_search()
       self.test_wikipedia_search()
       self.test_generate_image()
       self.test_off_suggested_replies()
       self.test_file_upload()
       self.test_select_agent()
       self.test_go_to_homepage()
    





    
    

