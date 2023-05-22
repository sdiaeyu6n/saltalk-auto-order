import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

from pages.login import LoginPage
from pages.order import OrderPage
from pages.menu import MenuPage
from pages.checkout import CheckoutPage

N_DAYS_LATER = 1
# TODO: (Sisi) 옵션 메뉴 선택 가능하게 하기
# TODO: (Youn) 주문 마감 시간 확인하기
# TODO: (Youn) Wait, find element 함수 공부하기

def main():
  # display = Display(visible=0, size=(800, 800))  
  # display.start()

  chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                        # and if it doesn't exist, download it automatically,
                                        # then add chromedriver to path

  chrome_options = webdriver.ChromeOptions()    
  # Add your options as needed    
  options = [
    # Define window size here
    "--window-size=1200,1200",
      "--ignore-certificate-errors"
  
      #"--headless",
      #"--disable-gpu",
      #"--window-size=1920,1200",
      #"--ignore-certificate-errors",
      #"--disable-extensions",
      #"--no-sandbox",
      #"--disable-dev-shm-usage",
      #'--remote-debugging-port=9222'
  ]

  for option in options:
      chrome_options.add_argument(option)

      
  driver = webdriver.Chrome(options = chrome_options)
  wait = WebDriverWait(driver, 20)

  # create login page
  login_page = LoginPage(driver, wait)

  if login_page.id is None or login_page.pw is None:
    print("ID or Password is not set")
    return
  
  # go to login page
  login_page.open_login_page()
  time.sleep(1)

  # input id & pw
  login_page.input_id_pw()

  # click login button
  login_page.click_login_button()
  time.sleep(1)

  order_page = OrderPage(driver, wait, N_DAYS_LATER)

  # go to order page
  order_page.open_order_page()
  time.sleep(1)

  is_order_placed = order_page.check_order_status() # check order 0 day after today

  if is_order_placed:
    print('Order already placed')
    return

  # go to menu page
  menu_page = MenuPage(driver, wait, N_DAYS_LATER)
  menu_page.open_menu_page()
  time.sleep(10) # wait for all the product-items to be clickable

  menu_page.add_favorite_orders_to_cart()
  time.sleep(1)

  # go to checkout page
  checkout_page = CheckoutPage(driver, wait)
  checkout_page.open_checkout_page()
  time.sleep(1)

  # click order confirm button
  checkout_page.click_place_order_button()
  time.sleep(1)

  # click confirm button
  checkout_page.click_confirm_button()

  # close the WebDriver
  driver.quit()

if __name__ == "__main__":
  main()