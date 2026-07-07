import allure
from config.environment import Environment
from pages.Sun_search_page import Search_Bar
from pages.Sun_login_page import LoginPage
from tests.base_test import BaseTest
from time import sleep

@allure.feature("Product Search")
class Test_Sun_search_page(BaseTest):
    @allure.title("verify user can login and search for a product")
    def test_login_and_search(self):
        env=Environment("Sun")
        self.driver.get(env.get_base_url())
        login_page=LoginPage(self.driver)
        login_page.login(
            env.get_username(),
            env.get_password()
        )
        search=Search_Bar(self.driver)
        search.search_product("Golf Maroon")
