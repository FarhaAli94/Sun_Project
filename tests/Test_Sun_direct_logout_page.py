import allure
from config.environment import Environment
from time import sleep
import pytest
from tests.base_test import BaseTest
from pages.Sun_login_page import LoginPage
from pages.Sun_direct_logout_page import Direct_Logout

@allure.feature("logout page")
class Test_Sun_direct_logout_page(BaseTest):
    @allure.title("direct logout")

    def test_direct_logout(self):
        env=Environment("Sun")
        self.driver.get(env.get_base_url())
        login_page=LoginPage(self.driver)
        sleep(3)
        login_page.login(
            env.get_username(),
            env.get_password()
        )
        sleep(5)
        direct=Direct_Logout(self.driver)
        direct.directlogout()
        sleep(5)
