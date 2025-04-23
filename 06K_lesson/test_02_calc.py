import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_browser():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome()
    yield driver  # Возвращаем драйвер для использования в тестах
    driver.quit()  # Закрываем браузер после завершения теста


def test_calculator_form(chrome_browser):
    chrome_browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = chrome_browser.find_element(By.ID, 'delay')
    delay_input.clear()
    delay_input.send_keys("45")

    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '7']"))
    ).click()

    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '+']"))
    ).click()

    WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '8']"))
    ).click()

    equal_button = WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text() = '=']"))
    )

    # Кликаем через JavaScript
    chrome_browser.execute_script("arguments[0].click();", equal_button)

    # Ожидание результата
    WebDriverWait(chrome_browser, 46).until(EC.text_to_be_present_in_element(
        (By.CLASS_NAME, 'screen'), '15')
    )


    result_text = chrome_browser.find_element(By.CLASS_NAME, 'screen').text
    print("Результат", result_text)
    # Преобразуем результат в целое число для сравнения
    assert int(result_text) == 15
