from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BTN)
        basket_button.click()

    def check_book_names(self):
        added_book_name = self.browser.find_element(By.CSS_SELECTOR, "#messages .alertinner > strong")
        actual_book_name = self.browser.find_element(By.CSS_SELECTOR, ".breadcrumb .active")
        assert added_book_name.text == actual_book_name.text, "Added book name and actual book name are not the same"

    def check_book_prices(self):
        book_price = self.browser.find_element(By.CSS_SELECTOR, ".row p.price_color")
        cart_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner p strong")
        assert book_price.text == cart_price.text, "Added book price and actual book price are not the same"
