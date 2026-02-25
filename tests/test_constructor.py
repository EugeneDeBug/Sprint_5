import pytest
from locators import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestConstructorTabs:
   
    def test_buns_tab(self, driver):
        
        sauces_tab = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(MainPage.SAUCES_TAB))
        sauces_tab.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(MainPage.ACTIVE_TAB_SAUCES)) 
        
        buns_tab = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPage.BUNS_TAB))
        buns_tab.click()

        active_tab = WebDriverWait(driver,5).until(EC.visibility_of_element_located(MainPage.ACTIVE_TAB_BUNS))
        assert "Булки" in active_tab.text

    def test_sauces_tab(self, driver):
        
        sauces_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.SAUCES_TAB))
        sauces_tab.click()

        active_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ACTIVE_TAB_SAUCES))
        assert "Соусы" in active_tab.text

    def test_fillings_tab(self, driver):
       
        fillings_tab = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MainPage.FILLINGS_TAB))
        fillings_tab.click()

        active_tab = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ACTIVE_TAB_FILLINGS))
        assert "Начинки" in active_tab.text
        