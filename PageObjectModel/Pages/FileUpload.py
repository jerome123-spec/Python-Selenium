from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constant import *
import time
from PageObjectModel.Locators.PageLocators import Locators
from PageObjectModel.Pages.AISearch import AISearch

class FileDocumentUpload(AISearch):
    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, GLOBAL_TIME_WAIT)
        self.test_file_execution()
        
    def file_document_upload_process(self):
        fileinput = self.wait.until(EC.presence_of_element_located((By.ID, Locators.file_upload)))
        self.file_path = NORMAL_FILE_UPLOAD_ATTACHMENT
        fileinput.send_keys(self.file_path)

    def test_homepage_file_upload(self):
        self.file_document_upload_process()
        self.homepage_click_send_icon()
        time.sleep(WAITING_TIME_FOR_NORMAL_FILE_DOCUMENT_UPLOAD)

    def text_test_send_query_for_document(self):
        self.chatroom_send_text("What is the uploaded file document about?")
        self.chatroom_click_send_icon()
    
    # Generate Image   
    def test_file_generate_image(self):
       self.chatroom_click_select_menu()
       self.chatroom_generate_image()    
       self.chatroom_click_html()
       self.chatroom_send_text("Give me five big bike motorcycles")
       self.chatroom_click_send_icon()

    # No Suggested Replies
    def no_suggested_replies(self):
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_off_suggested_replies()
        self.chatroom_click_html()
        self.chatroom_send_text("What is Salina? Give me 5 features of Salina.")
        self.chatroom_click_send_icon()
        time.sleep(GENERATE_IMAGE_WAIT)

    def test_normal_file_upload_file_attachment(self):
        self.chatroom_click_select_attachment()
        self.chatroom_click_file_button()
        self.upload_process()
        self.click_upload_button()
        time.sleep(WAITING_TIME_FOR_FILE_ATTACHMENT)
        self.chatroom_send_text("What are the uploaded file document about?")
        self.chatroom_click_send_icon()

    def test_file_execution(self):
        self.test_homepage_file_upload()
        self.text_test_send_query_for_document()
        self.test_file_generate_image()
        self.no_suggested_replies()
        self.test_normal_file_upload_file_attachment()
        self.test_select_agent()
        self.test_go_to_homepage()