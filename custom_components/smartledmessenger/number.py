from homeassistant.components.number import NumberEntity
from .const import *
from .api import SmartLedAPI

async def async_setup_entry(hass, entry, async_add_entities):
    api = SmartLedAPI(entry.data["host"])
    async_add_entities([
        SmartLedIntensity(api),
        SmartLedSpeed(api),
    ])

class SmartLedIntensity(NumberEntity):
    name = "Smart LED Intensity"
    native_min_value = MIN_INTENSITY
    native_max_value = MAX_INTENSITY

    def __init__(self, api):
        self.api = api
        self._attr_native_value = DEFAULT_INTENSITY

    async def async_set_native_value(self, value):
        self._attr_native_value = value
        self.api.send(intensity=int(value))

class SmartLedSpeed(NumberEntity):
    name = "Smart LED Speed"
    native_min_value = MIN_SPEED
    native_max_value = MAX_SPEED

    def __init__(self, api):
        self.api = api
        self._attr_native_value = DEFAULT_SPEED

    async def async_set_native_value(self, value):
        self._attr_native_value = value
        self.api.send(speed=int(value))
