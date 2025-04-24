import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


def test_checkout_total(driver):
    # Создаем экземпляр страницы
    page = ShopPage(driver)

    # Открыть сайт
    driver.get("https://www.saucedemo.com/")

    # Авторизироваться как пользователь standard_user
    page.login("standard_user", "secret_sauce")

    # Ожидание загрузки элементов на странице с товарами
    page.wait_for_inventory()

    # Добавить в корзину товары с использованием точного XPATH
    page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-backpack"]')
    page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-onesie"]')

    # Перейти в корзину и нажать Checkout
    page.go_to_cart()
    page.checkout()

    # Заполнить форму своими данными и нажать Continue
    page.fill_checkout_form("Sergey", "Bessonov", "73009")

    # Прочитать со страницы итоговую стоимость (Total)
    total = page.get_total()

    # Проверить итоговую сумму
    assert total == "Total: $58.29", (f"Expected total to be '$58.29',"
                                      f" but got '{total}'")
