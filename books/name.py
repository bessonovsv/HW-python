from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.example.com")

print(f'Заголовок страницы: {driver.title}')

driver.quit()
