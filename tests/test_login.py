import pytest
from locators import MainPage, LoginPage, RegisterPage, ForgotPasswordPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import perform_login
class TestLogin:
    @pytest.mark.parametrize("login_method", [
        "main_button",
        "personal_account",
        "register_link",
        "forgot_password_link"
    ])
    def test_login(self, driver, test_user, login_method):
        user = test_user
       
        if login_method == "main_button":
            driver.find_element(*MainPage.LOGIN_BUTTON).click()
        elif login_method == "personal_account":
            driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        elif login_method == "register_link":
            driver.find_element(*MainPage.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPage.REGISTER_LINK)).click()
            driver.find_element(*RegisterPage.LOGIN_LINK).click()
        elif login_method == "forgot_password_link":
            driver.find_element(*MainPage.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPage.FORGOT_PASSWORD_LINK)).click()
            driver.find_element(*ForgotPasswordPage.LOGIN_LINK).click()
    
        perform_login(driver, user["email"], user["password"])

        order_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(MainPage.ORDER_BUTTON)
        )
        assert order_button.is_displayed()
        driver.quit()
        