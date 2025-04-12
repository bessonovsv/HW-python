from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Функция для проверки видимости элемента и возврата элемента
def element_is_visible(driver, locator):
    try:
        element = (WebDriverWait(driver, 0.1)
                   .until(EC.visibility_of_element_located(locator)))
        return element  # Возвращаем элемент
    except Exception:
        return None  # Возвращаем None, если элемент не найден


# Создаем сервис с указанием пути к драйверу
service = Service(GeckoDriverManager().install())

# Инициализация драйвера Firefox
driver = webdriver.Firefox(service=service)

# Переходим на сайт
driver.get("https://bonigarcia.dev/"
           "selenium-webdriver-java/loading-images.html")

# Определяем локаторы для 3-й картинки
third_img_locator = (By.CSS_SELECTOR, 'img:nth-of-type(3)')

# Ожидаем загрузки 3-й картинки
try:
    element = WebDriverWait(driver, 60).until(
        lambda driver: element_is_visible(driver, third_img_locator))
except TimeoutException:
    print("Время ожидания истекло!")

# Проверяем наличие третьей картинки
if element:
    src = element.get_attribute('src')
    print(f"Ссылка на третье изображение: {src}")
else:
    print("Третья картинка не найдена!")

# Закрываем браузер
driver.quit()
