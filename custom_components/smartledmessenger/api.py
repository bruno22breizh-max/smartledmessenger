import requests

class SmartLedAPI:
    def __init__(self, host):
        self.host = host

    def send(
        self,
        message="",
        intensity=10,
        speed=40,
        static=0,
        local=0,
    ):
        url = (
            f"http://{self.host}/"
            f"?message={message}"
            f"&intensity={intensity}"
            f"&speed={speed}"
            f"&static={static}"
            f"&local={local}"
        )
        requests.get(url, timeout=5)
