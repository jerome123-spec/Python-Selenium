from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



class SauceDemoTest():

    def __init__ (self , driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.test_execute()


    def enter_username(self):
        self.driver.find_element(By.ID , value="user-name").send_keys("standard_user")
    def enter_password(self):
        self.driver.find_element(By.ID , value="password").send_keys("secret_sauce")
    def click_login_button(self):
        self.driver.find_element(By.XPATH , value="//input[contains(@id,'login-button')]").click()
    def homepage_click_add_to_cart(self):
        self.driver.find_element(By.XPATH , value="//button[contains(@id,'add-to-cart-sauce-labs-backpack')]").click()
    def click_cart_icon(self):
        self.driver.find_element(By.CLASS_NAME , value="shopping_cart_link").click()
    def assert_cart_item(self):
        item_element = self.driver.find_element(By.XPATH , value="//div[contains(@class, 'inventory_item_name') and text()]")
        element_text = item_element.text
        expected_text = "Sauce Labs Backpack"
        assert element_text == expected_text , f"Expected text {element_text} but got {expected_text}"
    print("The test is succes")
    
    def click_check_out_button(self):
        self.driver.find_element(By.ID , value="checkout").click()



        

    def test_execute(self):
        self.enter_username()
        self.enter_password()
        self.click_login_button()
        self.homepage_click_add_to_cart()
        self.click_cart_icon()
        self.assert_cart_item()
        self.click_check_out_button()
        time.sleep(1)