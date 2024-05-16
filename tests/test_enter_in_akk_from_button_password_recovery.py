from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestLoginInAkkFromButtonPasswordRecovery:
    def test_enter_in_akk_from_button_password_recovery(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p[2]/a")))
        driver.find_element(*StellarburgersLocators.Http_recovery_pass).click()  # click ссылки Восстановить пароль   Http_recovery_pass
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p/a")))
        driver.find_element(*StellarburgersLocators.Http_enter).click()    # Http_enter
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov5555@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/header/nav/a/p")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div")))
        assert driver.find_element(By.XPATH, "//div/main/div").is_displayed()  #



