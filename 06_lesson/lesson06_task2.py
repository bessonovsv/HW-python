from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Создаем сервис с указанием пути к драйверу
service = Service(GeckoDriverManager().install())

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=service)

# Переходим на страницу
driver.get('http://uitestingplayground.com/textinput')

# Находим поле ввода текста
input_field = driver.find_element(By.CSS_SELECTOR, '#newButtonName')

# Вводим текст "SkyPro" в поле
input_field.send_keys("SkyPro")

# Нажимаем на кнопку
search_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
search_button.click()

# Обновляем элемент search_button, чтобы получить новый текст
updated_search_button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')

# Выводим текст кнопки в консоль
print(updated_search_button.text)

# Закрываем браузер
driver.quit()
