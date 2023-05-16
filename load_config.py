import os
import config

cfg = None

def load_config():
  global cfg
  if not cfg:
    cfg = config.Config('fav_order.cfg')
  return cfg