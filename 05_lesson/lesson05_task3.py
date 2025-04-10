from time import sleep
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

# Создаем сервис с указанием пути к драйверу
service = Service(GeckoDriverManager().install())

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=service)

# Переходим на страницу
driver.get('http://the-internet.herokuapp.com/inputs')

# Находим поле ввода текста
input_field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

# Вводим текст "Sky" в поле
input_field.send_keys("Sky")
sleep(3)
# Очищаем поле методом clear()
input_field.clear()

# Вводим текст "Pro" в поле
input_field.send_keys("Pro")
sleep(3)
# Закрываем браузер
driver.quit()
