from datetime import datetime, timedelta
from utils.load_config import load_config

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base import BasePage

class MenuPage(BasePage):

  def __init__(self, driver, wait, n_days_later):
    super().__init__(driver, wait)
    self.n_days_later = n_days_later
  
  def _get_n_days_later(self):
    return (datetime.today() + timedelta(days=self.n_days_later)).strftime("%Y-%m-%d")

  def _get_saltalk_url(self):
    return f'https://www.saltalk.com/?date={self._get_n_days_later()}&shippingTime=Lunch'
  
  def _get_favorite_orders(self):
    return load_config()["orders"]

  def open_menu_page(self):
    self.saltalk_url = self._get_saltalk_url()
    self.driver.get(self.saltalk_url)

  def add_favorite_orders_to_cart(self):
    product_items = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))
    favorite_orders = self._get_favorite_orders()
    
    order_count = 0
    for product_item in product_items:

      # FIXME: (Youn) StaleElementReferenceException - wait for element to be ready
      product_title = product_item.find_element(by=By.CLASS_NAME, value="product-title").text
                                                                                            
      for favorite_order in favorite_orders[order_count:]:
        if favorite_order["title"] == product_title:
          add_button = product_item.find_element(By.CSS_SELECTOR, "svg-icon[src='assets/svg/menu/add.svg']")    
          add_button.click()

          # TODO: (Sisi) select options


          order_count += 1
        
      if order_count == len(favorite_orders):
        return