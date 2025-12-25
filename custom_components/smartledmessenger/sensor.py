from homeassistant.components.sensor import SensorEntity
from .api import SmartLedAPI
from datetime import timedelta
import requests

SCAN_INTERVAL = timedelta(seconds=30)

async def async_setup_entry(hass, entry, async_add_entities):
    api = SmartLedAPI(entry.data["host"])
    async_add_entities([SmartLedStatus(api)])

class SmartLedStatus(SensorEntity):
    name = "Smart LED Status"

    def __init__(self, api):
        self.api = api
        self._attr_native_value = "unknown"

    async def async_update(self):
        try:
            requests.get(f"http://{self.api.host}", timeout=3)
            self._attr_native_value = "online"
        except Exception:
            self._attr_native_value = "offline"
