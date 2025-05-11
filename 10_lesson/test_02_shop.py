import allure
import pytest
from selenium import webdriver
from shop_page import ShopPage


@pytest.fixture(scope="module")
def driver():
    """
    Фикстура для инициализации драйвера браузера.

    :return: WebDriver для управления браузером (тип: WebDriver)
    """
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.title("Проверка расчётов в интернет-магазине")
@allure.description("Проверить итоговую сумму при оформлении заказа")
@allure.feature("Интернет-магазин")
@allure.severity("critical")
def test_checkout_total(driver):
    """
    Тест для проверки итоговой суммы при оформлении заказа.

    :param driver: WebDriver для управления браузером (тип: WebDriver)
    :return: None
    """

    page = ShopPage(driver)

    with allure.step("Открыть сайт"):
        driver.get("https://www.saucedemo.com/")

    with allure.step(f'Авторизоваться как пользователь standard_user с паролём secret_sauce'):
        page.login("standard_user", "secret_sauce")


    with allure.step("Ожидание загрузки страницы с товарами"):
        page.wait_for_inventory()


    with allure.step("Добавить товары в корзину"):
        page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-backpack"]')
        page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
        page.add_item_to_cart('//*[@id="add-to-cart-sauce-labs-onesie"]')


    with allure.step("Перейти в корзину"):
        page.go_to_cart()

    with allure.step("Нажать на кнопку 'Checkout'"):
        page.checkout()




    with allure.step("Заполнить форму оформления заказа"):
        page.fill_checkout_form("Sergey", "Bessonov", "73009")


    with allure.step("Получить итоговую сумму"):
        total = page.get_total()


    with allure.step(f"Проверка итоговой суммы. Ожидаемая сумма '$58.29', фактическая '{total}'"):
        assert total == "Total: $58.29", (f"Expected total to be '$58.29',"
                                      f" but got '{total}'")
