# Импортируем класс Page из синхронного API Playwright.
from playwright.sync_api import Page

# Определяем класс LoginPage, который будет взаимодействовать со страницей логина.
class LoginPage:
    # Конструктор класса принимает один аргумент - объект страницы Playwright.
    def __init__(self, page: Page):
        self.page = page  # Сохраняем объект страницы внутри экземпляра класса для последующего использования.
        # Сохраняем URL страницы логина в переменную, чтобы использовать его для навигации.
        self.login_url = "https://the-internet.herokuapp.com/login"
        # Сохраняем селекторы элементов страницы логина.
        self.username_input = "input[name='username']"  # Селектор для поля ввода имени пользователя.
        self.password_input = "input[name='password']"  # Селектор для поля ввода пароля.
        self.login_button = "text='Login'"  # Селектор для кнопки логина.

    # Метод navigate используется для перехода к странице логина.
    def navigate(self):
        self.page.goto(self.login_url)  # Используем метод goto объекта страницы для навигации по URL.

    # Метод login используется для ввода учетных данных и выполнения входа.
    def login(self, username: str, password: str):
        # Метод fill заполняет поле ввода имени пользователя переданным значением username.
        self.page.fill(self.username_input, username)
        # Метод fill заполняет поле ввода пароля переданным значением password.
        self.page.fill(self.password_input, password)
        # Метод click выполняет клик по кнопке логина, чтобы войти на сайт.
        self.page.click(self.login_button)
