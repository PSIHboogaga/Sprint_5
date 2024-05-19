from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators
from data import get_sign_up_data

class TestRegistration:
    def test_registration(self, driver):
        email, password = get_sign_up_data()  #  фейковые имейлы и пароль создаем
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//a[text() = 'Зарегистрироваться']")))  # подождали пока ссылка Зарегистрироваться станет кликабельной (важная тема для слабых ПК и медленного интернете)
        driver.find_element(*StellarburgersLocators.Http_registr).click()  # click ссылки Зарегистрироваться
        driver.find_element(*StellarburgersLocators.Name).send_keys("Ivan")  # ввести имя
        driver.find_element(*StellarburgersLocators.Email).send_keys(
            email)  # ввести майл
        driver.find_element(*StellarburgersLocators.Password).send_keys(password)  # ввести пароль
        driver.find_element(*StellarburgersLocators.Button_registr).click()  # клик кнопки зарегисторироваться
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//h2[text() = 'Вход']")))  # подождали пока кнопка станет кликабельной (важная тема для слабых ПК и медленного интернета)
        assert driver.find_element(*StellarburgersLocators.Vhod).is_displayed()  # Проверили что отображается. ИЗУЗЕ! РАБОТАЕТ! Так же хорошо, как до лишней доработки!