
import allure
from config.environment import Environment
from pages.Sun_login_page import LoginPage
from pages.Sun_search_page import Search_Bar
from pages.Sun_product_page import Product_Page
from tests.base_test import BaseTest


class Test_Sun_product_page(BaseTest):

    @allure.title("Login, search product and add to cart")
    def test_add_product_to_cart(self):

        env = Environment("Sun")

        self.driver.get(env.get_base_url())

        login_page = LoginPage(self.driver)

        login_page.login(
            env.get_username(),
            env.get_password()
        )

        search = Search_Bar(self.driver)
        search.search_product("Golf Maroon")

        product_page = Product_Page(self.driver)
        product_page.selectproduct()
