from selenium.webdriver.common.by import By

class MainPage:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/..")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/..")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

class LoginPage:
    EMAIL_INPUT = (By.NAME, "name")
    PASSWORD_INPUT = (By.NAME, "Пароль")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")

class RegisterPage:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") 

class ForgotPasswordPage:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") 

class ProfilePage:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    