import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPage, MainPage

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_unique_email():    
    rand_part = generate_random_string(8)
    return f"test_{rand_part}@yandex.ru"

def generate_password(lenght=6):    
    return generate_random_string(lenght)

def perform_login(driver, email, password):    
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located(LoginPage.EMAIL_INPUT))
    driver.find_element(*LoginPage.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPage.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LoginPage.LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(MainPage.ORDER_BUTTON))
    