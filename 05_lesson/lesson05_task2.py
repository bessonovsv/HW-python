from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def press_button(local_driver, times=3):
    # Функция для нажатия на кнопку указанное количество раз.
    for _ in range(times):
        # Локализация кнопки по классу и тексту
        button = WebDriverWait(local_driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
        )
        button.click()


def verify_no_id_used(local_driver):
    # Проверка, что локализация кнопки не зависит от ID
    buttons = local_driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        id_attr = button.get_attribute("id")
        if id_attr and "dynamic" in id_attr.lower():
            print(f"Кнопка найдена с ID '{id_attr}',"
                  "зависящим от динамического значения")
        else:
            print("ID кнопки не зависит от динамических значений.")


# Создание экземпляра веб-драйвера


driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install())
)


driver.maximize_window()


# Переход на страницу
driver.get("http://uitestingplayground.com/dynamicid")

# Нажимаем кнопку три раза
press_button(driver)

# Проверяем, что идентификация кнопки не зависит от ID
verify_no_id_used(driver)

# Закрываем браузер
driver.quit()
