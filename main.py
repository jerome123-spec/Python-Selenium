from selenium import webdriver
import time
from PageObjectModel.Pages.LoginPage import LoginPage
from PageObjectModel.Pages.HomePageVideosFiles import VideosFilesUpload
from PageObjectModel.Pages.AISearch import AISearch
from constant import *


driver = webdriver.Chrome()
driver.maximize_window()
# ActionChains(driver).send_keys(Keys.F12).perform()

#UserLogin
LoginPage(driver)

#Norml Chat and AI Search
AISearch(driver)

# VideosFilesUpload
# VideosFilesUpload(driver)


time.sleep(1000)
driver.close()
driver.quit()
print('Test Completed')

