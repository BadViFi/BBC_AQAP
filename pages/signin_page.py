from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class SigninPage(BasePage):
    PAGE_URL = Links.SIGNIN_PAGE
    
    USERNAME_FIELD = ("xpath",'//input[@id="username"]')
    SUBMIT_FIELD = ("css selector",'#submit-button')
    
    PASSWORD_FIELD = ("xpath",'//input[@id="password"]')


    @allure.step("Enter signin")
    def enter_signin(self, signin):
        button = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        button.click()
        button.send_keys(signin)
    
    @allure.step("Enter password")  
    def enter_password(self,password):
        button = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        button.click()
        button.send_keys(password)
        
        
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_FIELD)).click()