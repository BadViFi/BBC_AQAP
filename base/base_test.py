from pages.home_page import HomePage
from pages.personal_details import PersonalPage
from pages.signin_page import SigninPage
from pages.post_page import PostPage
from pages.saved_page import SavedPage
from config.data import Data
import pytest


class BaseTest():
    data: Data
    signin_page:SigninPage
    home_page: HomePage
    personal_details:PersonalPage
    post_page:PostPage
    saved_post:SavedPage

    @pytest.fixture(autouse= True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.signin_page = SigninPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.personal_details = PersonalPage(driver)
        request.cls.post_page = PostPage(driver)
        request.cls.saved_post = SavedPage(driver)
    
    @pytest.fixture
    def login_required(self):
        self.signin_page.open()
        self.signin_page.enter_signin(self.data.SIGNIN)
        self.signin_page.click_submit_button()
        self.signin_page.enter_password(self.data.PASSWORD)
        self.signin_page.click_submit_button()

