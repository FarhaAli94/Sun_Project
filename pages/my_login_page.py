import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.my_base_page import Base_Page


class LoginPage(Base_Page):
    """
    Page Object class for Login Page.
    Contains login page related locators and reusable methods.
    """

    LOGIN_LINK = (By.LINK_TEXT, "Login")
    PHONE_NUMBER_TEXTBOX = (By.XPATH, "//input[@type='tel']")
    CONTINUE_BUTTON = (By.XPATH, "//button[normalize-space()='Continue']")
    OTP_TEXTBOX = (By.XPATH, "//input[@placeholder='Enter otp']")

    def __init__(self, driver):
        """
        Initializes LoginPage by calling the BasePage constructor.
        """
        super().__init__(driver)

    @allure.step("Clicking Login Link")
    def click_login_link(self):
        """
        Clicks on the Login link.
        """

        try:
            self.click(self.LOGIN_LINK)
            self.logger.info("Clicked on Login link successfully")

        except TimeoutException:
            self.logger.error("Login link is not clickable")
            raise

    @allure.step("Entering Phone Number: {phone_number}")
    def enter_phone_number(self, phone_number):
        """
        Enters phone number into the phone number textbox.
        """

        try:
            self.send_keys(self.PHONE_NUMBER_TEXTBOX, phone_number)
            self.logger.info(f"Entered phone number: {phone_number}")

        except TimeoutException:
            self.logger.error("Phone number textbox is not visible")
            raise

    @allure.step("Clicking Continue Button")
    def click_continue_button(self):
        """
        Clicks on the Continue button.
        """

        try:
            self.click(self.CONTINUE_BUTTON)
            self.logger.info("Clicked Continue button successfully")

        except TimeoutException:
            self.logger.error("Continue button is not clickable")
            raise

    @allure.step("Entering OTP")
    def enter_otp(self, otp):
        """
        Enters OTP into the OTP textbox.
        """

        try:
            self.enter_OTP(self.OTP_TEXTBOX, otp)
            self.logger.info("Entered OTP successfully")

        except TimeoutException:
            self.logger.error("OTP textbox is not visible")
            raise

    @allure.step("Perform Login")
    def login(self, phone_number):
        """
        Performs complete login flow until OTP page.
        """

        self.click_login_link()
        self.enter_phone_number(phone_number)
        self.click_continue_button()

    @allure.step("Checking OTP Textbox Visibility")
    def is_login_successful(self):
        """
        Checks whether OTP textbox is visible.
        """

        return self.is_visible(self.OTP_TEXTBOX, timeout=10)