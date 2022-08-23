from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


# для корректного отображения кириллицы в параметризаторах
def pytest_make_parametrize_id(config, val): return repr(val)


# добавляем параметр запуска тестов в командной строке(чем запускать) По умолчанию хром
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or edge")
    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or edge")
    parser.addoption('--language', action='store', default=None, help="Choose language: ru, en ... etc.")


# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def driver(request):
    browser_name = request.config.getoption("browser_name")  # получаем параметр командной строки browser_name
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    if browser_name == "chrome":
        print("\nstart Сhrome browser for test..")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "edge":
        print("\nstart Edge browser for test..")
        driver = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser_name should be chrome or edge")
    yield driver
    print("\nquit browser..")
    driver.quit()
