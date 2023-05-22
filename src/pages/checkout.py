from selenium.webdriver.common.by import By

from pages.base import BasePage

class CheckoutPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/checkout'
  def __init__(self, driver, wait):
    super().__init__(driver, wait)

  def open_checkout_page(self):
    self.driver.get(self.saltalk_url)

  def click_place_order_button(self):
    # FIXME: 
    order_button = self.driver.find_element(By.XPATH, '//app-checkout/div/div/div[1]/div[5]/app-checkout-fee/div/div/button')
    order_button.click()

  def click_confirm_button(self):
    confirm_button = self.driver.find_element(by=By.XPATH, value='/html/body/app-root/st-modal-box/div/div/div[2]/div[1]/button[2]')
    confirm_button.click()