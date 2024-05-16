from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from fixture import driver
from locators import StellarburgersLocators

class TestWorkGoBulki:
    def test_work_go_bulki(self, driver):
        driver.find_element(*StellarburgersLocators.Button_self_akk).click()
        WebDriverWait(driver, 20).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/main/div/h2")))
        driver.find_element(*StellarburgersLocators.Email).send_keys("IvanMakarov1000@mail.ru")  # ввод email
        driver.find_element(*StellarburgersLocators.Password).send_keys("1q2w3e4r5t")  # ввдод пароля
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((*StellarburgersLocators.Button_enter)))
        driver.find_element(*StellarburgersLocators.Button_enter).click()  # Клик кнопки войти
        driver.find_element(*StellarburgersLocators.Button_boolki).click()  # Клик кнопки boolki
        assert driver.find_element(By.CLASS_NAME, "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect").is_displayed()  #<div class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"><span class="text text_type_main-default">Булки</span></div>