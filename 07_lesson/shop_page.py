from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def wait_for_inventory(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

    def add_item_to_cart(self, item_xpath):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, item_xpath))
        )
        button.click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        (self.driver.find_element(By.CSS_SELECTOR, ".btn_primary.cart_button")
         .click())

    def get_total(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,
                                              "summary_total_label"))).text
