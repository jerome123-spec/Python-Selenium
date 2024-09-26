from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjectModel.Locators.PageLocators import Locators
from constant import *

class VideosFilesUpload():
    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, GLOBAL_TIME_WAIT)
        self.upload_test()
        
        
    def Navigate(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.homepage_attachment_id))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.select_attachment_id))).click()
        
    def TranscoderPage(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.click_to_redirect_transcoder_id))).click()
      
    def UploadProcess(self):
        fileinput = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.file_input)))
        self.file_path = VIDEOS_FILES_UPLOAD
        fileinput.send_keys(self.file_path)
        
    def click_upload_button(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.Upload_button))).click()


    def upload_test(self):
        self.Navigate()
        time.sleep(QUICK_WAIT)
        self.TranscoderPage()
        self.UploadProcess()
        self.click_upload_button()
       