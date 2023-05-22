class BasePage():
  def __init__(self, driver, wait) -> None:
    self.driver = driver
    self.wait = wait
