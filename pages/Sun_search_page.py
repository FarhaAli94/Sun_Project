from pages.Sun_login_page import LoginPage
from pages.base_page import BasePage
import allure


class Search_Bar(BasePage):

    def __init__(self, driver):
        # This calls the constructor of the BasePage to set up the driver, logger, etc.
        super().__init__(driver)

    search_input = ("xpath", "(//input[@type='text'])[2]")
    search_button = ("xpath", "(//button[@class='search_btn'])[2]")

    @allure.step("Searching Product:{product_name}")
    def search_product(self, product_name):
        self.send_keys(self.search_input, product_name)
        self.click(self.search_button)
