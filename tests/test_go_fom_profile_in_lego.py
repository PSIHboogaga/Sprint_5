from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators
from data import get_sign_up_data

class TestGoFomProfileInLego:
    def test_go_fom_profile_in_lego(self, driver):
        email, password = get_sign_up_data()
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p[1]/a")))
        driver.find_element(*StellarburgersLocators.Http_registr).click()  # click ссылки Зарегистрироваться
        driver.find_element(*StellarburgersLocators.Name).send_keys("Ivan")  # ввести имя
        driver.find_element(*StellarburgersLocators.Email).send_keys(
            email)  # ввести майл
        driver.find_element(*StellarburgersLocators.Password).send_keys(password)  # ввести пароль
        driver.find_element(*StellarburgersLocators.Button_registr).click()  #  клик кнопки зарегисторироваться
        driver.find_element(*StellarburgersLocators.Email).send_keys(
            email)  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys(password)  # ввдод пароля
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/header/nav/a/p")))
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()  # Клик кнопки личный кабинет
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div")))
        driver.find_element(*StellarburgersLocators.Button_lego).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/section[1]/h1")))
        assert driver.find_element(By.XPATH, "//div/main/section[1]/h1").is_displayed()  #









