import logging
import requests
_LOGGER = logging.getLogger(__name__)

class SmartLedAPI:
    def __init__(self, host):
        self.host = host
        self.supports_color = False

    def detect_capabilities(self):
        try:
            r = requests.get(f"http://{self.host}/", params={"color":"white"}, timeout=3)
            self.supports_color = r.status_code == 200
        except Exception:
            self.supports_color = False

    def send(self, params):
        try:
            requests.get(f"http://{self.host}/", params=params, timeout=3)
            return True
        except Exception as err:
            _LOGGER.warning("SmartLED unreachable: %s", err)
            return False
