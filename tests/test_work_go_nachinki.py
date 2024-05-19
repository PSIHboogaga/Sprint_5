from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestWorkGoNachinki:
    def test_work_go_nachinki(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//label[text()='Email']/../input")))  # подождали пока поле для ввода имейла станет доступным к использованию (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//span[text() = 'Начинки']"))) # подождали пока будут кликабельны начинки (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Button_nachinki).click()  # Клик кнопки nachinki
        assert driver.find_element(*StellarburgersLocators.Select_button).text == 'Начинки'  # проверили что начинки выбраны