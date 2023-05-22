import os
import config

cfg = None

def load_config():
  global cfg
  if not cfg:
    config_filepath = os.path.join(
      os.path.dirname(__file__), '../..', 'config/favorite_orders.cfg')
    cfg = config.Config(config_filepath)
  return cfg