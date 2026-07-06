from time import sleep
import allure
from pages.base_page import BasePage


class Logout_Page(BasePage):

    account_logout=("xpath","(//a[text()='My Account'])[1]")
    logout_link=("xpath","//p[@class='logout-link']")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("logout")
    def logoutlink(self):
        self.click(self.account_logout)
        sleep(5)
        self.click(self.logout_link)
        sleep(5)
