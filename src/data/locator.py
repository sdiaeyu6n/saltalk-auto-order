from selenium.webdriver.common.by import By

class LoginPageLocators:
  SIGN_IN_BUTTON = (By.LINK_TEXT, "Sign in")
  ID_INPUT = (By.ID, 'login-email')
  PW_INPUT = (By.ID, 'login-password')
  LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "Login")]')

class OrderPageLocators:
  ORDER_ITEMS = (By.CSS_SELECTOR, 'div.order-item')
  SHIPPING_TIME = (By.CSS_SELECTOR, 'span.shipping-time')
  ORDER_STATUS = (By.CSS_SELECTOR, 'div.order-status')


class MenuPageLocators:
  PRODUCT_ITEMS = (By.CLASS_NAME, "product-item")
  PRODUCT_TITLE = (By.CLASS_NAME, "product-title")
  ADD_BUTTON = (By.CSS_SELECTOR, "svg-icon[src='assets/svg/menu/add.svg']")

class CheckoutPageLocators:
  PLACE_ORDER_BUTTON = (By.XPATH, '//app-checkout/div/div/div[1]/div[5]/app-checkout-fee/div/div/button')
  CONFIRM_BUTTON = (By.XPATH, '/html/body/app-root/st-modal-box/div/div/div[2]/div[1]/button[2]')
