from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjectModel.Locators.PageLocators import Locators  
from constant import USERNAME , PASSWORD , STAGING , GLOBALTIMEWAIT

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, GLOBALTIMEWAIT)
        self.driver.get(STAGING)
        self.perform_login()
        
    def enter_username(self , input_username):
        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, Locators.username_textfield_id)))
        username_field.send_keys(input_username)
        
    def enter_password(self , input_password):
        password_field = self.wait.until(EC.presence_of_element_located((By.ID, Locators.password_textfield_id)))
        password_field.send_keys(input_password)
        
    def click_login_button(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, Locators.login_button_id)))
        login_button.click()

    def perform_login(self):
        self.enter_username(USERNAME)
        self.enter_password(PASSWORD)
        self.click_login_button()