from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestExitFromAccount:
    def test_exit_from_account(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email']/../input")))
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Войти']")))
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text() = 'Личный Кабинет']")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//button[text() = 'Выход']")))
        driver.find_element(*StellarburgersLocators.Button_exit).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text() = 'Вход']")))
        assert driver.find_element(*StellarburgersLocators.Vhod).is_displayed()