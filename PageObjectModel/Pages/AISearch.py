from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PageObjectModel.Locators.PageLocators import Locators
from constant import *

class AISearch():

    def __init__ (self , driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, GLOBAL_TIME_WAIT)
        self.test_execute()

    # Normal Chat
    def homepage_send_text(self):
        """Send a predefined text to the homepage text field."""
        self.wait.until(EC.presence_of_element_located((By.ID, Locators.homepage_text_field))).send_keys("What is Salina?")

    def assert_send_icon(self):
        """Verify that the send icon is enabled."""
        send_icon = self.wait.until(EC.presence_of_element_located((By.ID, Locators.homepage_send_button)))
        send_icon.is_enabled()

    def homepage_click_send_icon(self):
        """Click the send icon on the homepage."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.homepage_send_button))).click()

    def test_normal_chat(self):
        """Execute a normal chat test sequence."""
        self.homepage_send_text()
        self.assert_send_icon()
        self.homepage_click_send_icon()
       
    # Web Search 
    def chatroom_select_ai_search_button(self):
        """Click the AI search button in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_select_ai_search))).click()

    def select_search_option(self, value):
        """Select a specific search option by its text value."""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{value}')]"))).click()

    def chatroom_send_text(self, text_send_keys):
        """Send specified text to the chatroom text field."""
        self.wait.until(EC.presence_of_element_located((By.ID, Locators.chatroom_text_field))).send_keys(text_send_keys)

    def chatroom_click_send_icon(self):
        """Click the send icon in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_send_button))).click()

    def test_ai_search(self , search_option , input_text):
        """Execute an AI search test with specified search option and input text."""
        self.chatroom_select_ai_search_button()
        self.select_search_option(search_option)
        self.chatroom_send_text(input_text)
        self.chatroom_click_send_icon()
        
    # Generate Image
    def chatroom_click_select_menu(self):
        """Click the select menu icon in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_select_menu_icon))).click()

    def chatroom_generate_image(self):
        """Click the generate image button in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_generate_image))).click()

    def chatroom_click_html(self):
        """Click on the HTML element of the page."""
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//html[@lang='en']"))).click()
        
    def test_generate_image(self):
        """Execute an image generation test sequence."""
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_html()
        self.chatroom_send_text("Best AI Logo 2024")
        self.chatroom_click_send_icon()
        time.sleep(GENERATE_IMAGE_WAIT)

    # Suggested Replies (Disabled)
    def chatroom_click_off_suggested_replies(self):
        """Click to turn off suggested replies in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_suggested_replies))).click()
    
    def test_off_suggested_replies(self):
        """Execute a test sequence with suggested replies turned off."""
        self.chatroom_click_select_menu()
        self.chatroom_generate_image()
        self.chatroom_click_off_suggested_replies()
        self.chatroom_click_html()
        time.sleep(QUICK_WAIT)
        self.chatroom_select_ai_search_button()
        self.select_search_option("Salina Assistant")
        self.chatroom_send_text("Can you please give me a top 5 ai tools? and what are the main features each of one.")
        self.chatroom_click_send_icon()
      
    # File Document Upload
    def chatroom_click_select_attachment(self):
        """Click to select an attachment in the chatroom."""
        attachment = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@id='attachments-button-chatroom']")))
        self.driver.execute_script("arguments[0].focus()", attachment)
        attachment.click()

    def chatroom_click_file_button(self):
        """Click the file button to initiate file upload in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_select_file_document))).click()

    def upload_process(self):
        """Process the file upload by sending the file path."""
        fineinput = self.wait.until(EC.presence_of_element_located((By.NAME, Locators.chatroom_file_input)))
        self.file_path = AI_SEARCH_DOCUMENTS_ATTACHMENT
        fineinput.send_keys(self.file_path)

    def click_upload_button(self):
        """Click the upload button to complete the file upload process."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_upload_button))).click()

    def test_ai_page_file_attachment(self):
        """Execute a test sequence for uploading a file attachment in the AI page."""
        self.chatroom_click_select_attachment()
        self.chatroom_click_file_button()
        self.upload_process()
        self.click_upload_button()
        time.sleep(WAITING_TIME_FOR_FILE_ATTACHMENT)
        self.chatroom_send_text("What is the uploaded file document about?")
        self.chatroom_click_send_icon()
       
    # Select Agent
    def click_agent_icon(self):
        """Click the agent icon in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatroom_agent_icon))).click()

    def chatroom_select_agent(self):
        """Select a specific agent in the chatroom."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.chatbot_agent_selected))).click()

    def test_select_agent(self):
        """Execute a test sequence for selecting an agent and querying about uploaded documents."""
        self.click_agent_icon()
        self.chatroom_select_agent()
        time.sleep(QUICK_WAIT)
        self.chatroom_send_text("give me more context about the uploaded file documents but in the format bullet form.")
        self.chatroom_click_send_icon()
        time.sleep(SALINA_INQUIRY_WAITING_TIME_FOR_FILE_DOCUMENT)
    
    # Go to Homepage
    def test_go_to_homepage(self):
        """Navigate back to the homepage."""
        self.wait.until(EC.element_to_be_clickable((By.ID, Locators.click_homepage))).click()
        time.sleep(MIDDLE_WAIT)
       
    # Test Execution
    def test_execute(self):
        """Execute a comprehensive test sequence covering various functionalities."""
        self.test_normal_chat()
        self.test_ai_search("Web Search","ould you provide a current (2024) definition of AI and suggest some relevant topics for research or discussion in this field?")
        self.test_ai_search("Arxiv","What is computer science? provide some topics for it in bullet form format.")
        self.test_ai_search("Reddit","how ai being used in the world today?")
        self.test_ai_search("Youtube","top 10 automation testing for 2024")
        self.test_ai_search("Wikipedia","In what ways is AI being used to address global challenges such as poverty, education, and climate change?")
        self.test_generate_image()
        self.test_off_suggested_replies()
        self.test_ai_page_file_attachment()
        self.test_select_agent()
        self.test_go_to_homepage()