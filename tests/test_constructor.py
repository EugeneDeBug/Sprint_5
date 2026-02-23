import pytest
from selenium.webdriver.common.by import By
from locators import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorTabs:
    @pytest.mark.parametrize("tab_locator, expected_text", [
        (MainPage.BUNS_TAB, "Булки"),
        (MainPage.SAUCES_TAB, "Соусы"),
        (MainPage.FILLINGS_TAB, "Начинки")])
    
    def test_switch_tabs(self, driver, tab_locator, expected_text):
   
        current_active = driver.find_element(*MainPage.ACTIVE_TAB)
        active_text = current_active.find_element(By.XPATH, ".//span").text
        if active_text == expected_text:
            assert active_text == expected_text
            driver.quit()
            return
    
        tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(tab_locator))
        tab.click()    
        active_tab = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located(MainPage.ACTIVE_TAB)
        )
        assert expected_text in active_tab.text
        driver.quit()
        