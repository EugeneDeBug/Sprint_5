import pytest
from locators import RegisterPage, LoginPage, MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration:
    def test_successful_registration(self, driver, new_user):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPage.REGISTER_LINK)).click()

        
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys(new_user["name"])
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(new_user["password"])
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()


        login_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()
        driver.quit()
        

    def test_registration_fail_short_password(self, driver, new_user):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPage.REGISTER_LINK)).click()

        short_password = new_user["password"][:5]
        driver.find_element(*RegisterPage.NAME_INPUT).send_keys(new_user["name"])
        driver.find_element(*RegisterPage.EMAIL_INPUT).send_keys(new_user["email"])
        driver.find_element(*RegisterPage.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegisterPage.REGISTER_BUTTON).click()

    
        error = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(RegisterPage.PASSWORD_ERROR))
        assert error.is_displayed()
        driver.quit()
