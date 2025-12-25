from homeassistant.components.text import TextEntity
from .const import DOMAIN
from .api import SmartLedAPI

async def async_setup_entry(hass, entry, async_add_entities):
    api = SmartLedAPI(entry.data["host"])
    async_add_entities([SmartLedText(api)])

class SmartLedText(TextEntity):
    name = "Smart LED Message"

    def __init__(self, api):
        self.api = api
        self._attr_native_value = ""

    async def async_set_value(self, value: str):
        self._attr_native_value = value
        self.api.send(message=value)
