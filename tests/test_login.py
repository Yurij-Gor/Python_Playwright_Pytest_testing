import allure
import pytest  # Импортируем pytest, фреймворк для написания и организации тестов.

# Импортируем sync_playwright, который предоставляет синхронный API для Playwright,
# позволяя управлять браузером без асинхронного кода.
from playwright.sync_api import sync_playwright

# Импортируем LoginPage из нашего модуля pages. Это класс, который мы определили для управления страницей логина.
from pages.login_page import LoginPage


# Создаем фикстуру pytest, которая настраивает объект страницы перед каждым тестом, где она используется.
@pytest.fixture(scope="function")
def page():
    # Запускаем Playwright в контекстном менеджере, чтобы он корректно закрывался после выполнения теста.
    with sync_playwright() as p:
        # Запускаем новый экземпляр браузера Chromium. headless=False означает, что браузер будет виден во время теста.
        browser = p.chromium.launch(headless=False)
        # Открываем новую страницу в браузере.
        page = browser.new_page()
        # "yield" возвращает объект страницы для использования в тесте.
        yield page
        # После теста закрываем браузер.
        browser.close()


# Декораторы Allure для детализации отчетности
@allure.feature("Login Feature")  # Основная функциональность, которую тестируем (Авторизация)
@allure.story("Successful authentication")  # Конкретный сценарий в рамках функциональности (Успешная аутентификация)
@allure.severity(allure.severity_level.CRITICAL)  # Уровень важности теста
@allure.issue("AUTH-1", "http://issue-tracker/AUTH-1")  # Ссылка на задачу в системе учета ошибок
@allure.testcase("TC-1", "http://test-case/TC-1")  # Ссылка на тест-кейс в тест-менеджмент системе
@allure.description("This test successfully authorizes a user by email and password")  # Описание теста
# Определяем наш тестовый сценарий, который использует фикстуру "page".
def test_login_success(page):
    # Создаем экземпляр LoginPage, передавая ему объект страницы.
    login_page = LoginPage(page)
    # Переходим на страницу логина.
    login_page.navigate()
    # Выполняем процесс логина с использованием предоставленных учетных данных.
    login_page.login("tomsmith", "SuperSecretPassword!")
    # Проверяем, что URL страницы изменился на URL защищенной зоны, что указывает на успешный вход.
    assert page.url == "https://the-internet.herokuapp.com/secure"
    # Ищем элемент h2 на странице, получаем его текстовое содержимое, обрезаем пробелы и проверяем, что текст
    # соответствует "Secure Area".
    assert page.text_content("h2").strip() == "Secure Area"
