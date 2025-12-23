from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
from config.links import Links
from selenium.webdriver.common.by import By
import time
class SavedPage(BasePage):
    PAGE_URL = Links.SAVED
    
    @allure.step("Check for saved post")
    def check_for_post(self,post_url):
        saved_post = ("xpath", f"//a[contains(@href, '{post_url}')]")

        try:
            post = self.wait.until(EC.visibility_of_element_located(saved_post))
        except:
            raise ValueError("Saved post is not in the page")
        