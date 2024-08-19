from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys 
sys.path.append(r'C:\Users\Jerome\Desktop\Python-Selenium')
from PageObjectModel.Locators.PageLocators import *
from constant import *
class VideosFilesUpload():
    def __init__(self , driver):
        self.driver = driver
        self.UploadTest()
        
    
    def Navigate(self):
        self.driver.find_element(By.ID , Locators.homepage_attachment_id).click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID , Locators.select_attachment_id).click()
        time.sleep(2)
    def TranscoderPage(self):
        self.driver.find_element(By.ID , Locators.click_to_redirect_transcoder_id).click()
        time.sleep(2)
    def UploadProcess(self):
        fileinput = self.driver.find_element(By.NAME , Locators.file_input)
        self.driver.implicitly_wait(WAITINGTIME)
        self.file_path = AI_SEARCH_VIDEOS_FILES_ATTACHMENT
        time.sleep(2)
        fileinput.send_keys(self.file_path)
        time.sleep(2)
        self.driver.find_element(By.ID , Locators.Upload_button).click()

    def UploadTest(self):
        self.Navigate()
        self.TranscoderPage()
        self.UploadProcess()
