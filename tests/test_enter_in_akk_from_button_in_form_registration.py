from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators
from data import get_sign_up_data

class TestLoginInAkkFromButtonInFormRegistration:
    def test_enter_in_akk_from_button_in_form_registration(self, driver):
        email, password = get_sign_up_data()
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет Button_self_akk
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p[1]/a")))  # Http_registr
        driver.find_element(*StellarburgersLocators.Http_registr).click()  # click ссылки Зарегистрироваться Http_registr
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p/a")))  # Http_enter
        driver.find_element(*StellarburgersLocators.Http_enter).click()
        driver.find_element(*StellarburgersLocators.Email).send_keys(email)  # ввод email    Email
        driver.find_element(*StellarburgersLocators.Password).send_keys(password)  # ввдод пароля   Password
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти   Button_enter
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/header/nav/a/p")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click() # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div")))
        assert driver.find_element(By.XPATH, "//div/main/div").is_displayed() #