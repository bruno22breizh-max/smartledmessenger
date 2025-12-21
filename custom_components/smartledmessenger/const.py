from datetime import timedelta

DOMAIN = 'smartledmessenger'
CONF_IP = 'ip'
CONF_INTENSITY = 'intensity'
CONF_SPEED = 'speed'

INTENSITY_MIN = 0
INTENSITY_MAX = 15
SPEED_MIN = 10
SPEED_MAX = 50

DEFAULT_INTENSITY = 5
DEFAULT_SPEED = 20

SCAN_INTERVAL = timedelta(seconds=30)
