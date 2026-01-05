from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PostPage(BasePage):
    PAGE_URL = None
    SAVE_BUTTON = ("xpath", "//span[text()='Save']")
    SAVED_BUTTON = ("xpath", "//span[text()='Saved']")
    
    @allure.step("Save post")
    def save_post(self,post_url):
        url = self.PAGE_URL or post_url
        self.wait = WebDriverWait(self.driver, 3, poll_frequency=1)
        try:
            self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
            return True
        except:
            self.wait.until(EC.element_to_be_clickable(self.SAVED_BUTTON)).click()
            return False
        
        
    
        
        
            
    
    