from urllib.parse import quote
import aiohttp

from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    CONF_INTENSITY,
    CONF_SPEED,
    INTENSITY_MIN,
    INTENSITY_MAX,
    SPEED_MIN,
    SPEED_MAX,
    DEFAULT_INTENSITY,
    DEFAULT_SPEED,
)

TEXT_ENTITY_ID = "text.smart_led_messenger"


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        [
            SmartLedIntensity(coordinator, entry, hass),
            SmartLedSpeed(coordinator, entry, hass),
        ]
    )


class SmartLedIntensity(CoordinatorEntity, NumberEntity):
    _attr_name = "Smart Led Intensity"
    _attr_icon = "mdi:brightness-6"
    _attr_native_min_value = INTENSITY_MIN
    _attr_native_max_value = INTENSITY_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry, hass):
        super().__init__(coordinator)
        self._entry = entry
        self.hass = hass
        self._attr_native_value = entry.data.get(CONF_INTENSITY, DEFAULT_INTENSITY)

    async def async_set_native_value(self, value: float) -> None:
        value = int(value)
        self._attr_native_value = value
        self._entry.data[CONF_INTENSITY] = value
        await self._resend_message()
        self.async_write_ha_state()

    async def _resend_message(self):
        state = self.hass.states.get(TEXT_ENTITY_ID)
        if not state or not state.state:
            return

        data = self._entry.data
        message = quote(state.state)
        url = (
            f"http://{data['ip']}/"
            f"?message={message}"
            f"&intensity={data[CONF_INTENSITY]}"
            f"&speed={data[CONF_SPEED]}"
        )

        async with aiohttp.ClientSession() as session:
            await session.get(url)


class SmartLedSpeed(CoordinatorEntity, NumberEntity):
    _attr_name = "Smart Led Speed"
    _attr_icon = "mdi:motion-play"
    _attr_native_min_value = SPEED_MIN
    _attr_native_max_value = SPEED_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry, hass):
        super().__init__(coordinator)
        self._entry = entry
        self.hass = hass
        self._attr_native_value = entry.data.get(CONF_SPEED, DEFAULT_SPEED)

    async def async_set_native_value(self, value: float) -> None:
        value = int(value)
        self._attr_native_value = value
        self._entry.data[CONF_SPEED] = value
        await self._resend_message()
        self.async_write_ha_state()

    async def _resend_message(self):
        state = self.hass.states.get(TEXT_ENTITY_ID)
        if not state or not state.state:
            return

        data = self._entry.data
        message = quote(state.state)
        url = (
            f"http://{data['ip']}/"
            f"?message={message}"
            f"&intensity={data[CONF_INTENSITY]}"
            f"&speed={data[CONF_SPEED]}"
        )

        async with aiohttp.ClientSession() as session:
            await session.get(url)
