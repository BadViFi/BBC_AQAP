from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

class PersonalPage(BasePage):
    PAGE_URL = Links.PROFILE_PAGE
    EDIT_DISPLAY_NAME_BUTTON = ("css selector", "a[aria-label='Edit Display name']")

    DISPLAY_NAME = ("css selector","#display-name-field > div:nth-child(1) > div:nth-child(1)")
    EDIT_DISPLAY_NAME = ("xpath",'//input[@id="displayName-input"]')
    SUBMIT_BUTTON = ("css selector","button.button")
    



    def change_username(self, new_name):
        with allure.step(f"Change username on '{new_name}'"):
            self.wait_invisibility_of_spiner()
            edit_button = self.wait.until(EC.element_to_be_clickable(self.EDIT_DISPLAY_NAME_BUTTON))
            edit_button.click()
            
            self.wait_invisibility_of_spiner()
            change_field = self.wait.until(EC.element_to_be_clickable(self.EDIT_DISPLAY_NAME))
            change_field.click()
            change_field.clear()
            change_field.send_keys(new_name)
            self.name = new_name


    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_BUTTON)).click()

    @allure.step("Changes has been saved successfully")
    def is_changes_saved(self):
        self.wait_invisibility_of_spiner()
        display_name_elem = self.wait.until(EC.visibility_of_element_located(self.DISPLAY_NAME))
        actual_name = display_name_elem.text.strip()
        assert actual_name == self.name, f"Expected name '{self.name}', but got '{actual_name}'"

        
        