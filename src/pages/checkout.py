import sys
sys.path.append('saltalk-auto-order\src')

from selenium.webdriver.common.by import By
from pages.base import BasePage
from data.locator import CheckoutPageLocators

class CheckoutPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/checkout'
  def __init__(self, driver, wait):
    super().__init__(driver, wait)
    self.locator = CheckoutPageLocators

  def open_checkout_page(self):
    self.driver.get(self.saltalk_url)

  def click_place_order_button(self):
    # FIXME: (Youn) non interactable element
    order_button = self.driver.find_element(*self.locator.PLACE_ORDER_BUTTON)
    order_button.click()

  def click_confirm_button(self):
    # FIXME: (Youn) non interactable element
    confirm_button = self.driver.find_element(*self.locator.CONFIRM_BUTTON)
    confirm_button.click()