import requests
import threading
import time

class SmartLedAPI:
    def __init__(self, host):
        self.host = host

    def _send_raw(self, params):
        url = f"http://{self.host}/?{params}"
        requests.get(url, timeout=5)

    def send(
        self,
        message="",
        intensity=10,
        speed=40,
        static=0,
        local=0,
        return_clock_after=None,
    ):
        params = (
            f"message={message}"
            f"&intensity={intensity}"
            f"&speed={speed}"
            f"&static={static}"
            f"&local={local}"
        )

        self._send_raw(params)

        if return_clock_after:
            threading.Thread(
                target=self._delayed_clock,
                args=(return_clock_after,),
                daemon=True,
            ).start()

    def _delayed_clock(self, delay):
        time.sleep(delay)
        self._send_raw("message=&static=0")
