from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    PAGE_URL = Links.HOST
    MY_ACCOUNT_BUTTON = ("css selector",".sc-ac7f3982-1")
    MY_SETTINGS_BUTTON = ("link text","Settings")
    POSTS = ("css selector","div[data-testid$='-card']")
    SAVED_BUTTON = ("link text",'Saved')
    
    @allure.step("Click on my account")
    def click_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_BUTTON)).click()
        
    @allure.step("Click settings")
    def click_settings(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_SETTINGS_BUTTON)).click()
        
        
    @allure.step("Click on post")
    def click_on_post(self):
        self.open()
        posts = self.driver.find_elements(*self.POSTS)
        post = posts[0]
        link_element = post.find_element(By.TAG_NAME, "a")
        relative_link = link_element.get_attribute("href").replace("https://www.bbc.com", "")
        post.click()
        return relative_link
    
    @allure.step("Click on saved")
    def click_on_saved(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVED_BUTTON)).click()