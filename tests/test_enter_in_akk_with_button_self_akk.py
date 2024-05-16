from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestLoginInAkkWithButtonSelfAkk:
    def test_enter_in_akk_with_button_self_akk(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")))
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov5555@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        driver.find_element(*StellarburgersLocators.Button_enter).click() # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/header/nav/a/p")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div")))
        assert driver.find_element(By.XPATH, "//div/main/div").is_displayed()  #
