from selenium.webdriver.common.by import By

class StellarburgersLocators:
    Button_self_akk = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # Кнопка личный кабинет БЕЗ АБСОЛЮТНОГО ПУТИ + можно заменить на //a[@href = '/account'] если и такой вариант с XPATH не будет устраивать
    Button_enter = (By.XPATH, ".//button[text() = 'Войти']")  #  кнопка войти БЕЗ АБСОЛЮТНОГО ПУТИ
    Button_enter_in_akk = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #  кнопка Войти в аккаунт БЕЗ АБСОЛЮТНОГО ПУТИ
    Button_exit = (By.XPATH, ".//button[text() = 'Выход']")  # Кнопка выйти БЕЗ АБСОЛЮТНОГО ПУТИ
    Button_registr = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")  # кнопка зарегисторироваться БЕЗ АБСОЛЮТНОГО ПУТИ
    Button_lego = (By.XPATH, ".//p[text() = 'Конструктор']")  # кнопка конструктор
    Logo = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип
    Button_boolki = (By.XPATH, ".//span[text() = 'Булки']")  # кнопка boolki
    Button_nachinki = (By.XPATH, ".//span[text() = 'Начинки']")  # кнопка nachinki
    Button_sous = (By.XPATH, ".//span[text() = 'Соусы']")  # кнопка sous

    Http_registr = (By.XPATH, ".//a[text() = 'Зарегистрироваться']")  # ссылка Зарегистрироваться БЕЗ АБСОЛЮТНОГО ПУТИ
    Http_recovery_pass = (By.XPATH, "//a[text() = 'Восстановить пароль']") #  ссылка Восстановить пароль
    Http_enter = (By.XPATH, "//a[@href = '/login']")  #  ссылка Войти

    Email = (By.XPATH, "//label[text()='Email']/../input")  # поле email БЕЗ АБСОЛЮТНОГО ПУТИ
    Password = (By.NAME, "Пароль")  # поле пароля
    Name = (By.NAME, "name")  # поле имя
    Profile = (By.XPATH, "//a[@href = '/account/profile']")
    Vhod = (By.XPATH, ".//h2[text() = 'Вход']")
    Sodery_burger = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    Select_button = (By.XPATH, ".//span[text() = 'Булки']")
    Nn_passwrd = (By.XPATH, ".//span[text() = 'Некорректный пароль']")

