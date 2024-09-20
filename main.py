from selenium import webdriver
import time
from PageObjectModel.Pages.LoginPage import LoginPage
from PageObjectModel.Pages.AISearch import AISearch
from PageObjectModel.Pages.FileUpload import FileDocumentUpload
from PageObjectModel.Pages.HomePageVideosFiles import VideosFilesUpload
from constant import *


driver = webdriver.Chrome()
driver.maximize_window()
# ActionChains(driver).send_keys(Keys.F12).perform()

#UserLogin
LoginPage(driver)

#Normal Chat and AI Search
AISearch(driver)

#File Upload
FileDocumentUpload(driver)


# Videos Files Upload
# VideosFilesUpload(driver)


time.sleep(10)
driver.close()
driver.quit()
print('Test Completed')

