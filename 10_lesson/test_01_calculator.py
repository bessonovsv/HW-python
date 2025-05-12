import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculator_page import CalculatorPage


@pytest.fixture
def chrome_browser():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Проверка работы калькулятора с задержкой")
@allure.feature("Калькулятор")
@allure.severity("critical")
def test_calculator_form(chrome_browser):
    with allure.step("Открытие страницы калькулятора"):
        chrome_browser.get("https://bonigarcia.dev/"
                           "selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPage(chrome_browser)

    with allure.step("Установка задержки"):
        calculator.set_delay("45")

    with allure.step("Ввод чисел и операции"):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')

    with allure.step("Нажатие на кнопку равно"):
        calculator.click_equal()

    with allure.step("Ожидание появления результата"):
        WebDriverWait(chrome_browser, 46).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, 'screen'), '15')
        )

    with allure.step("Получение результата"):
        result_text = calculator.get_result()
        print("Результат", result_text)

    # Преобразуем результат в целое число для сравнения
    with allure.step("Проверка результата"):
        assert int(result_text) == 15
