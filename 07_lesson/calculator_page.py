from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, 'delay')
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//span[text() = '{button_text}']")))
        button.click()

    def click_equal(self):
        equal_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text() = '=']"))
        )
        self.driver.execute_script("arguments[0].click();", equal_button)

    def get_result(self):
        return self.driver.find_element(By.CLASS_NAME, 'screen').text
