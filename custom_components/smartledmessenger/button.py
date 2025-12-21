import aiohttp
from urllib.parse import quote
from homeassistant.components.button import ButtonEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([
        SmartLedPresetButton(coordinator, entry, 'Urgent', 'mdi:alert', '🚨 URGENCE', 15, 45),
        SmartLedPresetButton(coordinator, entry, 'Info', 'mdi:information', 'ℹ️ Information', 8, 25),
        SmartLedPresetButton(coordinator, entry, 'Nuit', 'mdi:weather-night', '🌙 Bonne nuit', 2, 15),
    ])

class SmartLedPresetButton(CoordinatorEntity, ButtonEntity):
    def __init__(self, coordinator, entry, name, icon, message, intensity, speed):
        super().__init__(coordinator)
        self._entry = entry
        self._message = message
        self._intensity = intensity
        self._speed = speed
        self._attr_name = f'Smart Led {name}'
        self._attr_icon = icon

    async def async_press(self) -> None:
        data = self._entry.data
        message = quote(self._message)
        url = f'http://{data["ip"]}/?message={message}&intensity={self._intensity}&speed={self._speed}'
        async with aiohttp.ClientSession() as session:
            await session.get(url)
