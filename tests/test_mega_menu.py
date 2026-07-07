import allure
import pytest
from tests.base_test import BaseTest
from config.environment import Environment
from pages.my_home_page import HomePage

@allure.feature("Mega Menu")
@allure.story("Verify Crop Nutrition Mega Menu")
class Test_Mega_Menu(BaseTest):
    """"
    Test Class For Mega Menu
    """

    @pytest.fixture(autouse=True)
    def setup_page(self,setup_and_teardown):
        self.mega_menu = HomePage(self.driver)
        env = Environment("Bighath")
        base_url = env.get_base_url()
        self.mega_menu.open_home_page(base_url)
        self.mega_menu.hover_crop_nutrition_menu()

    @allure.title("Verify Mega Menu is displayed after hovering Crop Nutrition")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke

    def test_verify_crop_nutrition_mega_menu(self,setup_and_teardown):
        self.logger.info("************ MEGA MENU TEST STARTED ************")
        self.mega_menu.verify_mega_menu()
        self.logger.info("************ MEGA MENU VERIFIED ************")

    @allure.title("Verify fertilizers column")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_fertilizers_column(self):
        self.logger.info("************ VERIFYING FERTILIZERS COLUMN ************")
        self.mega_menu.verify_fertilizers_column()
        self.logger.info("************ FERTILIZERS COLUMN SUCCESSFULLY VERIFIED ************")

    @allure.title("Verify growth promoters column")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_growth_promoters_column(self):
        self.logger.info("************ VERIFYING GROWTH PROMOTERS COLUMN ************")
        self.mega_menu.verify_growth_promoters_column()
        self.logger.info("************ GROWTH PROMOTERS COLUMN SUCCESSFULLY VERIFIED ************")

    @allure.title("Verify plant growth regulators column")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_plant_growth_regulators_column(self):
        self.logger.info("************ VERIFYING PLANT GROWTH REGULATORS COLUMN ************")
        self.mega_menu.verify_plant_growth_regulators_column()
        self.logger.info("************ PLANT GROWTH REGULATORS COLUMN VERIFIED SUCCESSFULLY ************")

    @allure.title("Verify popular column")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_popular_column(self):
        self.logger.info("************ VERIFYING POPULAR COLUMN ************")
        self.mega_menu.verify_popular_column()
        self.logger.info("************ POPULAR COLUMN  VERIFIED SUCCESSFULLY ************")

    @allure.title("Verify total columns in mega menu")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_verify_total_mega_menu_columns(self):
        self.logger.info("************ VERIFYING TOTAL COLUMNS ************")
        self.mega_menu.verify_total_mega_menu_columns()
        self.logger.info("************ TOTAL COLUMNS VERIFIED SUCCESSFULLY ************")




















    