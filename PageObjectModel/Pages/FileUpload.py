from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from constant import *
from PageObjectModel.Locators.PageLocators import *
from PageObjectModel.Pages.AISearch import AISearch


class FileDocumentUpload(AISearch):
    def __init__(self , driver):
        self.driver = driver
        self.test_file_execution()
        
       
    def file_document_upload_process(self):
        time.sleep(WAITINGTIME)
        fileinput = self.driver.find_element(By.ID , Locators.file_upload)
        self.file_path = AI_SEARCH_DOCUMENTS_ATTACHMENT
        time.sleep(WAITINGTIME)
        fileinput.send_keys(self.file_path)

    def test_homepage_file_upload(self):
        self.file_document_upload_process()
        self.homepage_click_send_icon()
        time.sleep(FILE_ATTACHMENT)

    def text_test_send_query_for_document(self):
        self.chatroom_send_text("What is the uploaded file document about?")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGRESPONSE)

    #Generate Image   
    def test_file_generate_image(self):
       self.chatroom_click_select_menu()
       self.chatroom_generate_image()    
       self.chatroom_click_html()
       self.chatroom_send_text("Give me five big bike motorcycles")
       self.chatroom_click_send_icon()
       time.sleep(40)

    #No Suggested Replies
    def no_suggested_repies(self):
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_off_suggested_replies()
        self.chatroom_click_html()
        self.chatroom_send_text("What is salina? give me 5 features of salina.")
        self.chatroom_click_send_icon()
        time.sleep(WAITINGNORMALRESPONSE)



    def test_file_execution(self):
        self.test_homepage_file_upload()
        self.text_test_send_query_for_document()
        self.test_file_generate_image()
        self.no_suggested_repies()
        # self.test_file_upload()
        # self.test_select_agent()
        # self.test_go_to_homepage()
 
 
        

