import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.cart_page import CartPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.mark.ui
def test_add_product_to_cart(driver):
    page = CartPage(driver)
    page.open_homepage()
    page.add_first_product_to_cart()
    page.go_to_cart()

    assert page.is_product_in_cart(), "Товар не найден в корзине"


@pytest.mark.ui
def test_remove_product_from_cart(driver):
    page = CartPage(driver)
    page.open_homepage()
    page.add_first_product_to_cart()
    page.go_to_cart()
    page.remove_product_from_cart()

    assert page.is_cart_empty(), "Корзина не пуста после удаления товара"


@pytest.mark.ui
def test_increase_quantity_in_cart(driver):
    page = CartPage(driver)
    page.open_homepage()
    page.add_first_product_to_cart()
    page.go_to_cart()

    initial_qty, initial_price = page.get_cart_quantity_and_price()
    page.increase_quantity()
    updated_qty, updated_price = page.get_cart_quantity_and_price()

    assert updated_qty > initial_qty, "Количество товара не увеличилось"
    assert updated_price > initial_price, (
        "Цена не увеличилась после увеличения количества"
    )
