from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjectModel.Locators.PageLocators import Locators
from constant import *

class TranscriptPage():

    def __init__(self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver , GLOBAL_TIME_WAIT)
        self.test_transcript_execution()       

    def play_video_player(self):
        self.wait.until(EC.element_to_be_clickable((By.ID , Locators.play_video_player))).click()
        
    def show_waveform(self):
        self.wait.until(EC.element_to_be_clickable((By.ID , Locators.display_waveform))).click()
        time.sleep(30)
    
    def pause_video_player(self):
        self.play_video_player()
    
    def click_language_button(self):
        element = self.wait.until(EC.element_to_be_clickable((By.ID, Locators.translate_button)))
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(30)

    def select_language_to_translate(self):
        self.wait.until(EC.element_to_be_clickable((By.ID , Locators.translate_tagalog))).click()

    def test_transcript_execution(self):
        self.play_video_player()
        self.show_waveform()
        self.pause_video_player()
        self.click_language_button()
        time.sleep(30)
        self.select_language_to_translate()
       
