from tests.base_test import BaseTest
from pages.Sun_login_page import LoginPage
import pytest
from config.environment import Environment

class Test_LoginPage(BaseTest):

    def test_successful_login(self):
        env=Environment("Sun")
        login_page=LoginPage(self.driver)
        login_page.navigate_to(env.get_base_url())
        login_page.login(
            env.get_username(),
            env.get_password()
        )

