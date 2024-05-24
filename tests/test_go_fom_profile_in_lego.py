from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestGoFomProfileInLego:
    def test_go_fom_profile_in_lego(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(StellarburgersLocators.Email))  # подождали пока поле для ввода имейла станет доступным к использованию (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(StellarburgersLocators.Button_enter))  # подождали пока кнопка войти станет кликабельной (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable(StellarburgersLocators.Button_self_akk))  # подождали пока кнопка личный кабинет станет кликабельной (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarburgersLocators.Button_lego))  # подождали пока кнопка конструктор станет кликабельной (важная тема для слабых ПК и медленного интернета)
        driver.find_element(*StellarburgersLocators.Button_lego).click()  # Клик кнопки конструктор
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(StellarburgersLocators.Sodery_burger))  # подождали пока отобразится Соберите бургер на странице (важная тема для слабых ПК и медленного интернета)
        assert driver.find_element(*StellarburgersLocators.Sodery_burger).is_displayed() # Проверили что отображается. ИЗУЗЕ! РАБОТАЕТ! Так же хорошо, как до лишней доработки!