from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators
from data import get_sign_up_data

class TestGoFromProfileInLogoSB:
    def test_go_from_profile_in_logo_sb(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email']/../input")))
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Войти']")))
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text() = 'Личный Кабинет']")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "AppHeader_header__logo__2D0X2")))
        driver.find_element(*StellarburgersLocators.Logo).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, ".//h1[text() = 'Соберите бургер']")))
        assert driver.find_element(By.XPATH, ".//h1[text() = 'Соберите бургер']").is_displayed()