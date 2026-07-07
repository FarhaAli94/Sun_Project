from time import sleep

import allure
from pages.base_page import BasePage


class Product_Page(BasePage):

    select_prod = ("xpath", "(//div[@class='filter_image_div'])[1]")
    add_cart = ("xpath", "//a[text()='Add to Cart']")
    click_ok = ("xpath", "//button[text()='OK']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Select product and add to cart")
    def selectproduct(self):
        self.click(self.select_prod)

        self.click(self.add_cart)

        self.click(self.click_ok)
