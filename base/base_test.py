from pages.home_page import HomePage
from pages.personal_details import PersonalPage
from pages.signin_page import SigninPage
from config.data import Data
import pytest


class BaseTest():
    data: Data
    signin_page:SigninPage
    home_page: HomePage
    personal_details:PersonalPage
    
    @pytest.fixture(autouse= True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.signin_page = SigninPage(driver)
        request.cls.home_page = HomePage(driver)
        request.cls.personal_details = PersonalPage(driver)