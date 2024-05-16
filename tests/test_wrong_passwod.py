from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestRegistrationWithWrongPassword:
    def test_registration_with_wrong_password(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p[1]/a")))
        driver.find_element(*StellarburgersLocators.Http_registr).click()  # click ссылки Зарегистрироваться
        driver.find_element(*StellarburgersLocators.Name).send_keys("Ivan1")  # ввести имя
        driver.find_element(*StellarburgersLocators.Email).send_keys(
            "IvanMakarov45555@mail.ru")  # ввести майл
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2")  # ввести пароль
        driver.find_element(*StellarburgersLocators.Button_registr).click()  #  клик кнопки зарегисторироваться
        assert driver.find_element(By.XPATH, "//div/main/div/form/fieldset[3]/div/p").is_displayed  #
