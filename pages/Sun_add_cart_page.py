from time import sleep
import allure
from pages.base_page import BasePage


class Add_Cart_Page(BasePage):

    add_cart=("xpath","(//a[text()=' Cart'])[2]")
    increment=("xpath","//button[@onclick='increment(9)']")
    remove=("xpath","//a[text()='Remove']")
    remove_ok=("xpath","//button[text()='OK']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("remove product added to cart")
    def removeproduct(self):
        self.click(self.add_cart)

        self.click(self.increment)

        self.click(self.remove)

        self.click(self.remove_ok)

