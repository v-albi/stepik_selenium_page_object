from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_has_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), "Basket has items but should not have"

    def basket_has_no_items_message_shown(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), "Basket is not empty but should be"
