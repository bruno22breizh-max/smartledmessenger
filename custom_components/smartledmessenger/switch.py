from homeassistant.components.switch import SwitchEntity
from .api import SmartLedAPI

async def async_setup_entry(hass, entry, async_add_entities):
    api = SmartLedAPI(entry.data["host"])
    async_add_entities([SmartLedStatic(api)])

class SmartLedStatic(SwitchEntity):
    name = "Smart LED Static"

    def __init__(self, api):
        self.api = api
        self._attr_is_on = False

    async def async_turn_on(self):
        self._attr_is_on = True
        self.api.send(static=0)

    async def async_turn_off(self):
        self._attr_is_on = False
        self.api.send(static=1)
