from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestLoginInAkkFromButtonInFormRegistration:
    def test_enter_in_akk_from_button_in_form_registration(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//a[text() = 'Зарегистрироваться']")))  # подождали пока ссылка Зарегистрироваться станет кликабельной (важная тема для слабых ПК и медленного интернете)
        driver.find_element(*StellarburgersLocators.Http_registr).click()  # click ссылки Зарегистрироваться
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href = '/login']")))  # подождали пока ссылкf войти станет кликабельной (важная тема для слабых ПК и медленного интернете)
        driver.find_element(*StellarburgersLocators.Http_enter).click()  # нажали на кнопку входа
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov5555@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, ".//p[text() = 'Личный Кабинет']")))  # подождали пока личного кабинета станет кликабельной (важная тема для слабых ПК и медленного интернете)
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[@href = '/account/profile']")))  # подождали пока отобрахзится профиль (важная тема для слабых ПК и медленного интернете)
        assert driver.find_element(*StellarburgersLocators.Profile).is_displayed()  # Проверили что профиль отображается. ИЗУЗЕ! РАБОТАЕТ! Так же хорошо, как до лишней доработки!