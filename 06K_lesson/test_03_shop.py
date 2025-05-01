import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def driver():
    """Фикстура инициализации драйвера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_checkout_total(driver):
    # Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # Авторизироваться как пользователь standard_user
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ожидание загрузки элементов на странице с товарами
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # Добавить в корзину товары с использованием точного XPATH
    backpack_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="add-to-cart-sauce-labs-backpack"]'))
    )
    backpack_button.click()

    # Добавить другие товары аналогично (например, Sauce Labs Bolt T-Shirt)
    bolt_tshirt_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'))
    )
    bolt_tshirt_button.click()

    onesie_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    '//*[@id="add-to-cart-sauce-labs-onesie"]'))
    )
    onesie_button.click()

    # Перейти в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Нажать Checkout
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    # Заполнить форму своими данными
    driver.find_element(By.ID, "first-name").send_keys("Sergey")
    driver.find_element(By.ID, "last-name").send_keys("Bessonov")
    driver.find_element(By.ID, "postal-code").send_keys("73009")

    # Нажать кнопку Continue
    driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button").click()

    # Прочитать со страницы итоговую стоимость (Total)
    total = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME,
                                          "summary_total_label"))).text

    # Проверить итоговую сумму
    assert total == "Total: $58.29",\
        f"Expected total to be '$58.29', but got '{total}'"
