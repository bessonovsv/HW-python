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


def test_calculator_form(chrome_browser):
    chrome_browser.get("https://bonigarcia.dev/"
                       "selenium-webdriver-java/slow-calculator.html")

    calculator = CalculatorPage(chrome_browser)

    calculator.set_delay("45")

    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')

    calculator.click_equal()

    # Ожидание результата
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15')
    )

    result_text = calculator.get_result()
    print("Результат", result_text)

    # Преобразуем результат в целое число для сравнения
    assert int(result_text) == 15
