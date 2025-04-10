from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Создаем сервис с указанием пути к драйверу
service = Service(GeckoDriverManager().install())

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=service)

# Переходим на страницу
driver.get('http://the-internet.herokuapp.com/login')

# Находим поле ввода username
input_field = driver.find_element(By.CSS_SELECTOR, '#username')

# Вводим текст в поле
input_field.send_keys("tomsmith")

# Находим поле ввода password
input_field = driver.find_element(By.CSS_SELECTOR, '#password')

# Вводим текст в поле
input_field.send_keys("SuperSecretPassword!")

# Нажимаем кнопку Login после загрузки страницы с задержкой
search_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.fa-2x'))
)

search_button.click()

# Ожидаем появления элемента с классом "flash success"
success_message = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.flash.success'))
)

# Выводим текст с зеленой плашки в консоль
print(success_message.text)

# Закрываем браузер
driver.quit()
