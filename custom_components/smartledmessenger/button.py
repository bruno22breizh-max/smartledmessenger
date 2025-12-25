from homeassistant.components.button import ButtonEntity
from .api import SmartLedAPI

async def async_setup_entry(hass, entry, async_add_entities):
    api = SmartLedAPI(entry.data["host"])
    async_add_entities([SmartLedClock(api)])

class SmartLedClock(ButtonEntity):
    name = "Smart LED Show Clock"

    def __init__(self, api):
        self.api = api

    async def async_press(self):
        self.api.send(message="", static=0)
