import pytest
from selenium import webdriver
from data import generate_unique_email, generate_password, generate_random_string
from locators import MainPage, LoginPage, RegisterPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():    
    options = webdriver.ChromeOptions()
    prefs = {"profile.password_manager_leak_detection": False}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options)
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def new_user():   
    name = generate_random_string(8)
    email = generate_unique_email()
    password = generate_password()
    return {"name": name, "email": email, "password": password}

@pytest.fixture
def test_user():   
    return {
        "name": "Евгений",
        "email": "eugene_popov_40_456@yandex.ru",
        "password": "123456789"
    }
