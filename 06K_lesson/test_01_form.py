import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.color import Color


@pytest.fixture(scope="module")
def driver():
    """Фикстура для инициализации драйвера"""
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_form_submission(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/"
               "selenium-webdriver-java/data-types.html")

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    # Заполнение полей
    for name, value in data.items():
        input_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            f"input[name='{name}']"))
        )
        input_field.clear()
        input_field.send_keys(value)

    # Нажимаем кнопку Submit после заполнения всех полей
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//button[@type='submit' and text()='Submit']"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    driver.execute_script("arguments[0].click();", submit_button)

    # Проверяем красное поле zip-code
    zip_alert = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        "#zip-code.alert-danger"))
    )
    bg_color_zip = zip_alert.value_of_css_property("background-color")
    hex_color_zip = Color.from_string(bg_color_zip).hex.lower()
    expected_red = '#f8d7da'

    assert hex_color_zip == expected_red,\
        (f"Поле Zip code не подсвечено красным: {hex_color_zip},"
         f" ожидалось {expected_red}")

    # Проверяем остальные поля на зелёную подсветку
    for name in data:
        if name == 'zip-code':
            continue
        alert_div = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            f"#{name}.alert-success"))
        )
        bg_color = alert_div.value_of_css_property("background-color")
        hex_color = Color.from_string(bg_color).hex.lower()
        expected_green = '#d1e7dd'

        assert hex_color == expected_green,\
            (f"Поле {name} не подсвечено зеленым: {hex_color}, "
             f"ожидалось {expected_green}")
