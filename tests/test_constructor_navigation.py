import pytest
from locators import MainPage, LoginPage, ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import perform_login

class TestConstructorNavigation:
    def test_go_to_constructor_by_link(self, driver, test_user):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        perform_login(driver, test_user["email"], test_user["password"])

        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePage.LOGOUT_BUTTON))

        driver.find_element(*ProfilePage.CONSTRUCTOR_LINK).click()
        
        order_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )
        assert order_button.is_displayed()

    def test_go_to_constructor_by_logo(self, driver, test_user):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        perform_login(driver, test_user["email"], test_user["password"])

        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ProfilePage.LOGOUT_BUTTON))

        driver.find_element(*ProfilePage.LOGO).click()
        order_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        