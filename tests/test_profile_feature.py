from base.base_test import BaseTest
import random
import allure
import pytest



@allure.feature("Sign in")
class TestSignin(BaseTest):
    @allure.title("Sign in account")
    @allure.severity("Critical")
    @pytest.mark.login
    def test_sign_in(self):
        self.signin_page.open()
        self.signin_page.enter_signin(self.data.SIGNIN)
        self.signin_page.click_submit_button()
        self.signin_page.enter_password(self.data.PASSWORD)
        self.signin_page.click_submit_button()


@allure.feature("Profile Functionality")
@pytest.mark.usefixtures("login_required")
class TestProfileFeature(BaseTest):
    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke

    def test_change_username(self):
        self.home_page.is_opened()
        self.home_page.click_my_account()
        self.home_page.click_settings()
        
        self.personal_details.change_username(f"Test {random.randint(1,100)}")
        self.personal_details.save_changes()
        self.personal_details.is_changes_saved()
        self.personal_details.make_screenshot("Success")     
        
        

@allure.feature("Save Post")
@pytest.mark.usefixtures("login_required")
class TestSavePost(BaseTest):
    @allure.title("Save post")
    @allure.severity("Critical")
    @pytest.mark.posts
    def test_save_post(self):
        self.home_page.is_opened()

        post_url = self.home_page.click_on_post()
        self.post_page.save_post(post_url)
        
        self.home_page.open()
        self.home_page.is_opened()
        self.home_page.click_my_account()
        self.home_page.click_on_saved()

        self.saved_post.check_for_post(post_url)
        
        