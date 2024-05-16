from selenium.webdriver.common.by import By

class StellarburgersLocators:
    Button_self_akk = (By.XPATH, "//div/header/nav/a/p") # Кнопка личный кабинет
    Button_enter = (By.XPATH, "//div/main/div/form/button")  #  кнопка войти
    Button_enter_in_akk = (By.XPATH, "//div/main/section[2]/div/button") #  кнопка Войти в аккаунт
    Button_exit = (By.XPATH, "//div/main/div/nav/ul/li[3]/button")  # Кнопка выйти
    Button_registr = (By.XPATH, "//div/main/div/form/button")  # кнопка зарегисторироваться
    Button_lego = (By.XPATH, "//div/header/nav/ul/li[1]/a")  # кнопка конструктор
    Logo = (By.XPATH, "//div/header/nav/div")  # Логотип
    Button_boolki = (By.XPATH, "//div/main/section[1]/div[1]/div[1]")  # кнопка boolki
    Button_nachinki = (By.XPATH, "//div/main/section[1]/div[1]/div[3]")  # кнопка nachinki
    Button_sous = (By.XPATH, "//div/main/section[1]/div[1]/div[2]")  # кнопка sous

    Http_registr = (By.XPATH, "//div/main/div/div/p[1]/a")  # ссылка Зарегистрироваться
    Http_recovery_pass = (By.XPATH, "//div/main/div/div/p[2]/a") #  ссылка Восстановить пароль
    Http_enter = (By.XPATH, "//div/main/div/div/p/a")  #  ссылка Войти

    Email = (By.XPATH, "//div/main/div/form/fieldset[1]/div/div/input")  # поле email
    Password = (By.NAME, "Пароль")  # поле пароля
    Name = (By.NAME, "name")  # поле имя
