import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        """
        Инициализация страницы магазина.

        :param driver: WebDriver для управления браузером (тип: WebDriver)
        """
        self.driver = driver

    @allure.step("Вход в систему")
    def login(self, username: str, password: str) -> None:
        """
        Выполняет вход в систему.

        :param username: Имя пользователя (тип: str)
        :param password: Пароль (тип: str)
        :return: None
        """
        with allure.step("Указать имя"):
            self.driver.find_element(By.ID, "user-name").send_keys(username)
        with allure.step("Указать пароль"):
            self.driver.find_element(By.ID, "password").send_keys(password)
        with allure.step("Нажать на кнопку login-button"):
            self.driver.find_element(By.ID, "login-button").click()

    @allure.step("Ожидание появления новой страницы")
    def wait_for_inventory(self) -> None:
        """
        Ожидает появления страницы с инвентарем.

        :return: None
        """
        with allure.step("Подождать появления новой страницы"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "inventory_list"))
            )

    @allure.step("Добавление товара в корзину")
    def add_item_to_cart(self, item_xpath: str) -> None:
        """
        Добавляет товар в корзину.

        :param item_xpath: XPath элемента товара (тип: str)
        :return: None
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        button.click()

    @allure.step("Переход в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None
        """
        with allure.step("Нажать на кнопку shopping_cart_link"):
            self.driver.find_element(By.CLASS_NAME,
                                     "shopping_cart_link").click()

    @allure.step("Проверка наличия кнопки 'Checkout'")
    def checkout(self) -> None:
        """
        Переходит к оформлению заказа.

        :return: None
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    @allure.step("Заполнение формы оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str,
                           postal_code: str) -> None:
        """
        Заполняет форму оформления заказа.

        :param first_name: Имя (тип: str)
        :param last_name: Фамилия (тип: str)
        :param postal_code: Почтовый индекс (тип: str)
        :return: None
        """

        # Заполнение формы с шагами Allure
        with allure.step("Заполнить имя"):
            self.driver.find_element(By.ID, "first-name").send_keys(first_name)

        with allure.step("Заполнить фамилию"):
            self.driver.find_element(By.ID, "last-name").send_keys(last_name)

        with allure.step("Заполнить почтовый индекс"):
            self.driver.find_element(By.ID,
                                     "postal-code").send_keys(postal_code)

        with allure.step("Нажать на кнопку 'Продолжить'"):
            self.driver.find_element(By.CSS_SELECTOR,
                                     ".btn_primary.cart_button").click()

    @allure.step("Получение общей суммы")
    def get_total(self) -> str:
        """
         Получает общую сумму заказа.

         :return: Общая сумма (тип: str)
         """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                              "summary_total_label"))).text
