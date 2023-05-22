from datetime import datetime, timedelta
from selenium.webdriver.common.by import By

from pages.base import BasePage

class OrderPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/order'  
  
  def __init__(self, driver, wait, n_days_later):
    super().__init__(driver, wait)
    self.n_days_later = n_days_later

  def open_order_page(self):
    self.driver.get(self.saltalk_url)

  def _get_n_days_later(self):
    return (datetime.today() + timedelta(days=self.n_days_later)).strftime('%a %m/%d')
    
  def check_order_status(self):
    # get next day in the same form w/ saltalk date(ex. Fri 05/14)
    next_day = self._get_n_days_later()

    # load order items
    order_items = self.driver.find_elements(by=By.CSS_SELECTOR, value='div.order-item')

    # check if (1) date is today's date +1 & (2) order status is 'Paid'
    for order_item in order_items:
      # (1) date is today's date +1
      shipping_time = order_item.find_element(By.CSS_SELECTOR, 'span.shipping-time').text
      if shipping_time == next_day:
        # (2) order status is 'Paid'
        order_status = order_item.find_element(By.CSS_SELECTOR, 'div.order-status').text
        if order_status == 'Paid':
          print(f'Found an order {self.n_days_later} day later')
          return True

    print(f'Not found an order {self.n_days_later} day later')
    return False