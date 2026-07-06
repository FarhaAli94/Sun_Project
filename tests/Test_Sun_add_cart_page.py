import allure
from config.environment import Environment
from pages.Sun_search_page import Search_Bar
from pages.Sun_login_page import LoginPage
from pages.Sun_product_page import Product_Page
from pages.Sun_add_cart_page import Add_Cart_Page
from tests.base_test import BaseTest
from time import sleep

@allure.feature("remove product")
class Test_Sun_add_cart_page(BaseTest):
    @allure.title("add the product and remove then product from cart")
    def test_add_remove_cart(self):
        env=Environment("Sun")
        self.driver.get(env.get_base_url())
        login_page=LoginPage(self.driver)
        sleep(3)
        login_page.login(
            env.get_username(),
            env.get_password()
        )
        sleep(5)
        search = Search_Bar(self.driver)
        search.search_product("Golf Maroon")

        product_page = Product_Page(self.driver)
        product_page.selectproduct()
        sleep(5)

        addcart=Add_Cart_Page(self.driver)
        addcart.removeproduct()
        sleep(5)
