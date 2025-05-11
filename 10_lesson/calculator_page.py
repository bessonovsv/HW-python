import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс, представляющий страницу калькулятора.

    :param driver: WebDriver для управления браузером (тип: WebDriver)
    """

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Установить задержку")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку в поле ввода.

        :param delay: Задержка, которую нужно установить (тип: str)
        :return: None
        """
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажать на кнопку {button_text}")
    def click_button(self, button_text: str) -> None:
        """
        Нажимает на кнопку с указанным текстом.

        :param button_text: Текст кнопки, на которую нужно нажать (тип: str)
        :return: None
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//span[text() = '{button_text}']")))
        button.click()

    @allure.step("Нажать на кнопку равно")
    def click_equal(self) -> None:
        """
        Нажимает на кнопку 'равно'.

        :return: None
        """
        equal_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = '=']"))
        )
        self.driver.execute_script("arguments[0].click();", equal_button)

    @allure.step("Получить результат")
    def get_result(self) -> str:
        """
        Получает результат вычисления из экрана калькулятора.

        :return: Результат вычисления (тип: str)
        """
        return self.driver.find_element(By.CLASS_NAME, 'screen').text
