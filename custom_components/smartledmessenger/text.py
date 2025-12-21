import aiohttp
from urllib.parse import quote
from homeassistant.components.text import TextEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SmartLedText(coordinator, entry)])

class SmartLedText(CoordinatorEntity, TextEntity):
    _attr_name = "Smart Led Messenger"
    _attr_icon = "mdi:led-on"

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._entry = entry
        self._attr_native_value = ""

    async def async_set_value(self, value: str) -> None:
        # 🔑 mémorisation du message
        self.coordinator.last_message = value

        data = self._entry.data
        message = quote(value)
        url = (
            f"http://{data['ip']}/"
            f"?message={message}"
            f"&intensity={data['intensity']}"
            f"&speed={data['speed']}"
        )

        async with aiohttp.ClientSession() as session:
            await session.get(url)

        self._attr_native_value = value
        self.async_write_ha_state()

