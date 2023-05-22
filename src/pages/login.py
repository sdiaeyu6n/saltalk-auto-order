import os
from selenium.webdriver.common.by import By

from pages.base import BasePage

class LoginPage(BasePage):
  saltalk_url = 'https://www.saltalk.com/welcome'
  def __init__(self, driver, wait):
    super().__init__(driver, wait)
    self.id = os.getenv("SALTALK_ID")
    self.pw = os.getenv("SALTALK_PASSWORD")

  def open_login_page(self):
    self.driver.get(self.saltalk_url)
    sign_in_button = self.driver.find_element(by=By.LINK_TEXT, value="Sign in")
    sign_in_button.click()

  def input_id_pw(self):
    id_input = self.driver.find_element(By.ID, 'login-email')
    id_input.send_keys(self.id)
    pw_input = self.driver.find_element(By.ID, 'login-password')
    pw_input.send_keys(self.pw)

  def click_login_button(self):
    login_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Login")]')
    login_button.click()
