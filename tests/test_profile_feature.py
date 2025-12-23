from base.base_test import BaseTest
import random
import allure
import pytest

@allure.feature("Profile Functionality")
class TestProfileFeature(BaseTest):
    
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_username(self):
        self.signin_page.open()
        self.signin_page.enter_signin(self.data.SIGNIN)
        self.signin_page.click_submit_button()
        self.signin_page.enter_password(self.data.PASSWORD)
        self.signin_page.click_submit_button()
        
        self.home_page.is_opened()
        self.home_page.click_my_account()
        
        self.personal_details.change_username(f"Test {random.randint(1,100)}")
        self.personal_details.save_changes()
        self.personal_details.is_changes_saved()
        self.personal_details.make_screenshot("Success")
        
        

        