from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def open_homepage(self):
        self.driver.get("https://www.sibdar-spb.ru/")

    def add_first_product_to_cart(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

        add_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.btn-default.js-order")
        ))
        add_button.click()

        self.wait.until(
            lambda driver: int(driver.find_element
                               (By.CSS_SELECTOR,
                                "span.count_bask_right").text) > 0
        )

    def go_to_cart(self):
        cart_icon = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.bask_icon")
        ))
        cart_icon.click()

    def is_product_in_cart(self):
        count = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "span.count_bask_right")
        ))
        return int(count.text) > 0

    def remove_product_from_cart(self):
        delete_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.delet_pr_bas")
        ))
        delete_button.click()

    def is_cart_empty(self):
        empty_message = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Корзина пуста')]")
        ))
        return empty_message.is_displayed()

    def increase_quantity(self):
        plus_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "span.plus_prod")
        ))
        plus_button.click()

        self.wait.until(
            lambda driver: "2" in driver.find_element
            (By.CSS_SELECTOR, "input.rasOb").get_attribute("value")
        )

    def get_cart_quantity_and_price(self):
        quantity_value = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "input.rasOb")
        )).get_attribute("value").replace(" шт", "")

        price_value = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "span.price_ti")
        )).text

        return int(quantity_value), int(price_value)
