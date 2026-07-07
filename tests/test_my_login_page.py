import allure
import pytest

from config.environment import Environment
from pages.my_login_page import LoginPage
from tests.base_test import BaseTest


@allure.feature("Authentication")
@allure.story("User Login")
class TestMyLogin(BaseTest):
    """
    Test class for Login functionality.
    """

    @allure.title("Verify Login with Valid Phone Number")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_valid_login(self):
        """
        Test case to verify login with valid phone number.
        """

        self.logger.info("************ VALID LOGIN TEST STARTED ************")

        login_page = LoginPage(self.driver)

        env = Environment("prod")
        base_url = env.get_base_url()
        phone_number ="7975813655"

        with allure.step("Open Application"):
            login_page.navigate_to(base_url)

        with allure.step("Perform Login"):
            login_page.login(phone_number)

        with allure.step("Verify OTP Page"):
            assert login_page.is_login_successful(), "OTP page is not displayed after entering valid phone number"

        self.logger.info("************ VALID LOGIN TEST PASSED ************")

    @allure.title("Verify Login with Less Than 10 Digit Phone Number")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_invalid_login_with_less_than_10_digits(self):
        """
        Test case to verify Continue button is disabled
        when phone number contains less than 10 digits.
        """

        self.logger.info("************ INVALID LOGIN TEST STARTED ************")

        login_page = LoginPage(self.driver)

        env = Environment("prod")
        base_url = env.get_base_url()

        with allure.step("Open Application"):
            login_page.navigate_to(base_url)

        with allure.step("Enter Invalid Phone Number"):
            login_page.click_login_link()
            login_page.enter_phone_number("12345")

        with allure.step("Verify Continue Button is Disabled"):
            assert login_page.is_continue_button_disabled()

        self.logger.info("************ INVALID LOGIN TEST PASSED ************")