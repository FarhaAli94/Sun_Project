import allure
import pytest
from tests.base_test import BaseTest
from config.environment import Environment
from pages.my_home_page import HomePage


class TestMyHomePage(BaseTest):
    """
    Test class for verifying Home Page functionality.
    """

    @allure.feature("Home Page")
    @allure.story("Verify Home Page Title")
    @allure.title("Verify Agriculture Home Page Title")
    def test_home_page_title(self):
        """
        Test case to verify Home Page title using prod environment URL.
        """

        self.logger.info("************ HOME PAGE TEST STARTED ************")

        home_page = HomePage(self.driver)

        """
        Get production URL from config.yaml.
        """
        env =Environment("prod")
        base_url = env.get_base_url()

        """
        Open Home Page.
        """
        home_page.open_home_page(base_url)

        """
        Verify Home Page title.
        """
        assert home_page.verify_home_page_title()

        self.logger.info("************ HOME PAGE TEST VERIFIED ************")

