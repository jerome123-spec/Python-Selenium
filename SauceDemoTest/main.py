from selenium import webdriver
from saucedemotest import *
import time


driver = webdriver.Chrome()
driver.maximize_window()


SauceDemoTest(driver)

time.sleep(5000)