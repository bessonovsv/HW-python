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
driver.get('http://uitestingplayground.com/ajax')

# Нажимаем кнопку после загрузки страницы с задержкой 5 секунд
search_button = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#ajaxButton'))
)

search_button.click()

# Ожидаем появления элемента с классом "bg-success" 16 секунд
success_message = WebDriverWait(driver, 16).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.bg-success'))
)

# Выводим текст с зеленой плашки в консоль
print(success_message.text)

# Закрываем браузер
driver.quit()
