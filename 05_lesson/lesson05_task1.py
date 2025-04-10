from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


def perform_test(local_driver):
    # Переходим на страницу и ждём ее открытия
    driver.get("http://uitestingplayground.com/classattr")
    driver.execute_script("return document.readyState === 'complete'")

    # Ожидаем появления синей кнопки
    xpath_selector = ("//button[contains(concat"
                      "(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    search_button = WebDriverWait(local_driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath_selector))
    )

    # Нажатие на синюю кнопку
    search_button.click()

    # Обработка всплывающего окна
    try:
        alert = local_driver.switch_to.alert
        alert.accept()  # Подтверждаем всплывающее окно
    except NoAlertPresentException:
        print("Нет всплывающего окна.")  # Обработка исключения

    # Проверяем, можем ли мы найти кнопку через атрибут btn-primary
    found_buttons = local_driver.find_elements(By.XPATH, xpath_selector)
    if len(found_buttons) > 0:
        print(f"Было найдено {len(found_buttons)}"
              f" кнопка с классом 'btn-primary'.")
    else:
        print("Кнопки с классом 'btn-primary' не найдены.")


# Создаем экземпляр драйвера
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install())
)


driver.maximize_window()


# Выполняем тест три раза
perform_test(driver)
perform_test(driver)
perform_test(driver)

# Закрываем браузер
driver.quit()
