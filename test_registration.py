from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver

class TestRegistration:
    def test_registration(self, driver):
        driver.find_element(By.XPATH, "//div/header/nav/a").click()
        WebDriverWait(driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/div/p[1]/a")))
        driver.find_element(By.XPATH, "//div/main/div/div/p[1]/a").click()  # click ссылки Зарегистрироваться
        driver.find_element(By.NAME, "name").send_keys("Ivan")  # ввести имя
        driver.find_element(By.XPATH, "//div/main/div/form/fieldset[2]/div/div/input").send_keys(
            "IvanMakarov5512@mail.ru")  # ввести майл
        driver.find_element(By.NAME, "Пароль").send_keys("1q2w3e4r5t")  # ввести пароль
        driver.find_element(By.XPATH,
                            "//div/main/div/form/button").click()  # клик кнопки зарегисторироваться
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//div/main/div/form")))
        assert driver.find_element(By.XPATH, "//div/main/div/form").is_displayed() #
