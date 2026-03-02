from locators import MainPage, LoginPage, ProfilePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import perform_login

class TestPersonalAccount:
    def test_go_to_personal_account_unauthorized(self, driver):
        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()

        login_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPage.LOGIN_BUTTON)
        )
        assert login_button.is_displayed()

    def test_go_to_personal_account_authorized(self, driver, test_user):
        driver.find_element(*MainPage.LOGIN_BUTTON).click()
        perform_login(driver, test_user["email"], test_user["password"])

        driver.find_element(*MainPage.PERSONAL_ACCOUNT_BUTTON).click()
        logout_button = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(ProfilePage.LOGOUT_BUTTON)
        )
        assert logout_button.is_displayed()
        