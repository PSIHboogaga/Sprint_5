from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver

class TestExit:
    def test_work_go_nachinki(self, driver):
        driver.find_element(By.XPATH, "//div/header/nav/a").click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/h2")))
        driver.find_element(By.XPATH, "//body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(By.XPATH, "//body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("1q2w3e4r5t")  # ввдод пароля
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//body/div/div/main/div/form/button")))
        driver.find_element(By.XPATH, "//body/div/div/main/div/form/button").click()  # Клик кнопки войти
        driver.find_element(By.XPATH, "//div/main/section[1]/div[1]/div[3]").click()  # Клик кнопки nachinki
        assert driver.find_element(By.XPATH, "//div/main/section[1]/div[2]/ul[3]/a[1]/img").is_displayed()  #