from time import sleep
import allure
from pages.base_page import BasePage


class Direct_Logout(BasePage):

    direct_logout=("xpath","(//a[text()='My Account'])[1]")
    direct_logout_link=("xpath","//p[@class='logout-link']")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("logout")
    def directlogout(self):
        self.click(self.direct_logout)
        sleep(5)
        self.click(self.direct_logout_link)
        sleep(5)
