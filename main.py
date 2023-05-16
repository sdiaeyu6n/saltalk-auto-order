import os
from load_config import load_config
import time
from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display

from fuzzysearch import find_near_matches

display = Display(visible=0, size=(800, 800))  
display.start()

id = os.getenv("SALTALK_ID")
pw = os.getenv("SALTALK_PASSWORD")

# load fav_order
fav_order = load_config()["order"]

if id is None or pw is None:
  print("ID or Password is not set")
  exit(1)

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
driver.get('https://www.saltalk.com/welcome')
wait = WebDriverWait(driver, 10)

# login
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")

sign_in_button.click()

time.sleep(1)

id_input = driver.find_element(By.ID, 'login-email')
id_input.send_keys(id)
pw_input = driver.find_element(By.ID, 'login-password')
pw_input.send_keys(pw)

login_button = driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
login_button.click()

time.sleep(1)

# open sidebar
sidebar_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a.sidebar-btn.fl')))
sidebar_button.click()

# driver.get('https://www.saltalk.com/order')

# click 'My Orders' button
orders_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.menu.st-flex-must[routerlink="/order"]')))
orders_button.click()

# get next day in the same form w/ saltalk date(ex. Fri 05/14)
next_day = (datetime.today() + timedelta(days=1)).strftime('%a %m/%d')

time.sleep(1)

# load order items
order_items = driver.find_elements(by=By.CSS_SELECTOR, value='div.order-item')

# check if (1) date is today's date +1 & (2) order status is 'Paid'
for order_item in order_items:
  # (1) date is today's date +1
  shipping_time = order_item.find_element(By.CSS_SELECTOR, 'span.shipping-time').text
  if shipping_time == next_day:
    # (2) order status is 'Paid'
    order_status = order_item.find_element(By.CSS_SELECTOR, 'div.order-status').text
    if order_status == 'Paid':
      print('Found an order with next day shipping and Paid status')
      exit(0)

print('No order with next day shipping and Paid status')

driver.get("https://www.saltalk.com") # back to menu

# wait for all the product-items to be clickable
time.sleep(10)

product_items = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-item")))

for product_item in product_items:
  title = product_item.find_element(by=By.CLASS_NAME, value="product-title")  
  if find_near_matches(fav_order["title"], title.text, max_l_dist=10):
    add_button = product_item.find_element(By.CSS_SELECTOR, "svg-icon[src='assets/svg/menu/add.svg']")    
    add_button.click()    
    break

# fast checkout
time.sleep(1)
fast_checkout_button = driver.find_element(by=By.CSS_SELECTOR, value="#menu-products-box > div.cart-items-root > app-b2b-cart-items > div > div.btn > div > button")
fast_checkout_button.click()    

# order confirm
time.sleep(1)
confirm_button = driver.find_element(by=By.CSS_SELECTOR, value="body > app-root > st-modal-box > div > div > div:nth-child(2) > div.btn-box.ng-star-inserted > button.ant-btn.btn.half.fr.ant-btn-primary")
confirm_button.click()