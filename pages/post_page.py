from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By

class PostPage(BasePage):
    PAGE_URL = None
    SAVE_BUTTON = ("xpath", "//span[text()='Save']")

    @allure.step("Save post")
    def save_post(self,post_url):
        url = self.PAGE_URL or post_url
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()
        
        
            
    
    