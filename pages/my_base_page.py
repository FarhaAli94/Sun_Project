import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from config.environment import Environment
from utils.logger import get_logger


class Base_Page:
    """
    Base class containing common reusable methods for all page objects.
    This class follows the Page Object Model design pattern.
    """

    def __init__(self, driver):
        """
        Initializes WebDriver, Explicit Wait and Logger.
        """

        self.driver = driver
        self.act = ActionChains(driver)
        self.wait = WebDriverWait(driver, 20)
        self.logger = get_logger()

    @allure.step("Clicking Element: {locator}")
    def click(self, locator):
        """
        Waits until the element is clickable and performs click action.
        """

        try:
            element = self.wait.until(
                EC.element_to_be_clickable(locator)
            )
            element.click()

            self.logger.info(f"Successfully clicked on element: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Element not clickable: {locator}")
            raise

    @allure.step("Entering value '{value}' into Element: {locator}")
    def send_keys(self, locator, value, clear_first=True):
        """
        Waits until the element is visible and enters the given value.
        """

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            if clear_first:
                element.clear()

            element.send_keys(value)

            self.logger.info(f"Successfully entered value into element: {locator}")

        except TimeoutException:
            self.logger.error(f"Timeout: Element not visible: {locator}")
            raise

    @allure.step("Entering OTP into Element: {locator}")
    def enter_OTP(self, locator, otp):
        """
        Waits until the OTP field is visible and enters the OTP.
        """

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            element.send_keys(otp)

            self.logger.info("OTP entered successfully")

        except TimeoutException:
            self.logger.error(f"Timeout: OTP field not visible: {locator}")
            raise

    @allure.step("Checking visibility of Element: {locator}")
    def is_visible(self, locator, timeout=10):
        """
        Checks whether an element is visible or not.
        Returns True if visible, otherwise returns False.
        """

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

            self.logger.info(f"Element is visible: {locator}")
            return True

        except TimeoutException:
            self.logger.info(f"Element is not visible within {timeout} seconds: {locator}")
            return False

    @allure.step("Getting text from Element: {locator}")
    def get_text(self, locator):
        """
        Waits until the element is visible and returns its text.
        """

        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )

            text = element.text

            self.logger.info(f"Retrieved text '{text}' from element: {locator}")
            return text

        except TimeoutException:
            self.logger.error(f"Timeout: Could not get text from element: {locator}")
            raise

    @allure.step("Getting page title")
    def get_title(self):
        """
        Returns the current page title.
        """

        title = self.driver.title
        self.logger.info(f"Current page title: {title}")

        return title

    def get_prod_phone_number(self):
        """
        Gets production phone number from config.yaml.
        """

        env = Environment("Bighath")
        return env.current_env["phone_number"]

    @allure.step("Checking Continue Button Disabled")
    def is_continue_button_disabled(self):
        """
        Returns True if Continue button is disabled.
        """

        button = self.wait.until(
            EC.visibility_of_element_located(self.CONTINUE_BUTTON)
        )

        return not button.is_enabled()

    @allure.step("Navigating to URL: {url}")
    def navigate_to(self, url):
        """
        Navigates to the given application URL.
        """

        try:
            self.driver.get(url)
            self.logger.info(f"Successfully navigated to URL: {url}")

        except Exception as e:
            self.logger.error(f"Failed to navigate to URL: {url}. Error: {e}")
            raise

    @allure.step("Hovering to Crop Nutrition:{locator}")
    def hover_to(self,locator,timeout=10):
        """
        Hovering to Crop Protection by using action methods
        """

        try:
            element=WebDriverWait(self.driver,timeout).until(
                EC.visibility_of_element_located(locator)
            )
            self.act.move_to_element(element).perform()
            self.logger.info(f"Successfully hover to Corp Nutrition:{locator}")
        except TimeoutException:
            self.logger.info(f"Element is not visible within {timeout} seconds: {locator}")
            return False






