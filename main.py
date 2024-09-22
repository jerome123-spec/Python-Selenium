from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PageObjectModel.Pages.LoginPage import LoginPage
from PageObjectModel.Pages.AISearch import AISearch
from PageObjectModel.Pages.FileUpload import FileDocumentUpload
from PageObjectModel.Pages.HomePageVideosFiles import VideosFilesUpload
from constant import *

# Initialize the WebDriver instance and maximize the window
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # User Login
    LoginPage(driver)

    # Normal Chat and AI Search
    AISearch(driver)

    # File Upload
    FileDocumentUpload(driver)

    # Videos Files Upload
    VideosFilesUpload(driver)

    time.sleep(10)
finally:
    driver.close()
    driver.quit()