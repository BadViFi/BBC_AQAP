from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure

class HomePage(BasePage):
    PAGE_URL = Links.HOST
    MY_ACCOUNT_BUTTON = ("css selector",".sc-ac7f3982-1")
    MY_SETTINGS_BUTTON = ("css selector","li.sc-8342e32-2:nth-child(2) > div:nth-child(1) > a:nth-child(1)")
    
    @allure.step("Click on my account")
    def click_my_account(self):
        self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(self.MY_SETTINGS_BUTTON)).click()