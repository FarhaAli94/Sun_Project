import allure
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.my_base_page import Base_Page



class HomePage(Base_Page):
    """
    Page Object class for Home Page.
    Contains Home Page related reusable methods.
    """

    EXPECTED_TITLE = "Agriculture Products Online | Buy Agricultural Products Online"
    CROP_NUTRITION_MENU=(By.XPATH,"//a[normalize-space()='Crop Nutrition']")
    MEGA_MENU=(By.XPATH,"//div[@data-headlessui-state='open']")
    MEGA_MENU_COLUMN_FERTILIZER=(By.XPATH,"(//a[@id='fertilizers'][1])")
    MEGA_MENU_COLUMN_GROWTH_PROMOTERS=(By.XPATH,"//a[@id='growth-promoters']")
    MEGA_MENU_COLUMN_PLANT_GROWTH_REGULATORS=(By.XPATH,"//a[@id='plant-growth-regulators']")
    MEGA_MENU_COLUMN_POPULAR=(By.XPATH,"//a[@id='popular']")


    @allure.step("Opening Home Page URL")
    def open_home_page(self, url):
        """
        Opens the application home page URL.
        """

        try:
            self.driver.get(url)
            self.logger.info(f"Home Page URL opened successfully: {url}")

        except Exception as e:
            self.logger.error(f"Failed to open Home Page URL: {url}. Error: {e}")
            raise

    @allure.step("Getting Home Page title")
    def get_home_page_title(self):
        """
        Gets the current home page title.
        """

        try:
            title = self.driver.title
            self.logger.info(f"Home Page title is: {title}")
            return title

        except Exception as e:
            self.logger.error(f"Failed to get Home Page title. Error: {e}")
            raise

    @allure.step("Verifying Home Page title")
    def verify_home_page_title(self):
        """
        Verifies the Home Page title.
        """

        try:
            actual_title = self.get_home_page_title()

            assert actual_title == self.EXPECTED_TITLE

            self.logger.info("Home Page title verified successfully")
            return True

        except AssertionError:
            self.logger.error("Home Page title verification failed")
            raise

    @allure.step("Hover on Crop Nutrition menu")
    def hover_crop_nutrition_menu(self):
        try:
            for attempt in range(3):
                try:
                    crop = self.wait.until(
                        EC.visibility_of_element_located(self.CROP_NUTRITION_MENU)
                    )

                    ActionChains(self.driver).move_to_element(crop).pause(1).perform()

                    self.logger.info("Hovered on Crop Nutrition menu successfully")
                    return

                except StaleElementReferenceException:
                    self.logger.warning("Crop Nutrition stale, retrying hover")

            raise StaleElementReferenceException("Crop Nutrition menu stale after retries")

        except TimeoutException:
            self.logger.error("Crop Nutrition menu not visible for hover")
            raise

        except TimeoutException:
            self.logger.error("Crop Nutrition menu not visible for hover")
            raise

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Crop Nutrition menu")
            raise

    @allure.step("Verify Mega Menu is visible")
    def verify_mega_menu(self):
        """
        Verify Mega Menu is displayed.
        """
        try:
            assert self.is_visible(self.MEGA_MENU)
            self.logger.info("Mega Menu is displayed")

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Mega Menu")
            raise

        except Exception as e:
            self.logger.error(f"Failed to verify Mega Menu: {e}")
            raise

    @allure.step("Verify Fertilizers Column")
    def verify_fertilizers_column(self):
        """
        Verify Fertilizers column is displayed in Mega Menu.
        """
        try:
            assert self.is_visible(self.MEGA_MENU_COLUMN_FERTILIZER)
            self.logger.info("Fertilizers column is displayed")

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Fertilizers column")
            raise

        except Exception as e:
            self.logger.error(f"Unable to verify Fertilizers column: {e}")
            raise

    @allure.step("Verify Growth Promoters Column")
    def verify_growth_promoters_column(self):
        """
        Verify Growth Promoters column is displayed in Mega Menu.
        """
        try:
            assert self.is_visible(self.MEGA_MENU_COLUMN_GROWTH_PROMOTERS)
            self.logger.info("Growth Promoters column is displayed")

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Growth Promoters column")
            raise

        except Exception as e:
            self.logger.error(f"Unable to verify Growth Promoters column: {e}")
            raise

    @allure.step("Verify Plant Growth Regulators Column")
    def verify_plant_growth_regulators_column(self):
        """
        Verify Plant Growth Regulators column is displayed in Mega Menu.
        """
        try:
            assert self.is_visible(self.MEGA_MENU_COLUMN_PLANT_GROWTH_REGULATORS)
            self.logger.info("Plant Growth Regulators column is displayed")

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Plant Growth Regulators column")
            raise

        except Exception as e:
            self.logger.error(f"Unable to verify Plant Growth Regulators column: {e}")
            raise

    @allure.step("Verify Popular Column")
    def verify_popular_column(self):
        """
        Verify Popular column is displayed in Mega Menu.
        """
        try:
            assert self.is_visible(self.MEGA_MENU_COLUMN_POPULAR)
            self.logger.info("Popular column is displayed")

        except StaleElementReferenceException:
            self.logger.error("Stale Element: Popular column")
            raise

        except Exception as e:
            self.logger.error(f"Unable to verify Popular column: {e}")
            raise

    @allure.step("Verify Total Mega Menu Columns")
    def verify_total_mega_menu_columns(self):
        """
        Verify total Mega Menu columns displayed.
        """
        try:
            count = 0

            if self.is_visible(self.MEGA_MENU_COLUMN_FERTILIZER):
                count += 1

            if self.is_visible(self.MEGA_MENU_COLUMN_GROWTH_PROMOTERS):
                count += 1

            if self.is_visible(self.MEGA_MENU_COLUMN_PLANT_GROWTH_REGULATORS):
                count += 1

            if self.is_visible(self.MEGA_MENU_COLUMN_POPULAR):
                count += 1

            self.logger.info(f"Total Mega Menu Columns : {count}")

            assert count == 4

        except StaleElementReferenceException:
            self.logger.error("Stale Element while counting Mega Menu columns")
            raise

        except Exception as e:
            self.logger.error(f"Failed to verify Mega Menu columns: {e}")
            raise

