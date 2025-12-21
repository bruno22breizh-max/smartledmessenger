import asyncio
import aiohttp
from urllib.parse import quote

from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    CONF_INTENSITY,
    CONF_SPEED,
    INTENSITY_MIN,
    INTENSITY_MAX,
    SPEED_MIN,
    SPEED_MAX,
    DEFAULT_INTENSITY,
    DEFAULT_SPEED,
)

DEBOUNCE_DELAY = 0.3


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data["smartledmessenger"][entry.entry_id]
    sender = SmartLedSender(entry, coordinator)
    async_add_entities(
        [
            SmartLedIntensity(coordinator, entry, sender),
            SmartLedSpeed(coordinator, entry, sender),
        ]
    )


class SmartLedSender:
    def __init__(self, entry, coordinator):
        self.entry = entry
        self.coordinator = coordinator
        self._task = None

    async def schedule_send(self):
        if self._task:
            self._task.cancel()
        self._task = asyncio.create_task(self._delayed_send())

    async def _delayed_send(self):
        try:
            await asyncio.sleep(DEBOUNCE_DELAY)
            await self._send()
        except asyncio.CancelledError:
            pass

    async def _send(self):
        message = self.coordinator.last_message
        if not message:
            return

        data = self.entry.data
        url = (
            f"http://{data['ip']}/"
            f"?message={quote(message)}"
            f"&intensity={data[CONF_INTENSITY]}"
            f"&speed={data[CONF_SPEED]}"
        )

        async with aiohttp.ClientSession() as session:
            await session.get(url)


class SmartLedIntensity(CoordinatorEntity, NumberEntity):
    _attr_name = "Smart Led Intensity"
    _attr_icon = "mdi:brightness-6"
    _attr_native_min_value = INTENSITY_MIN
    _attr_native_max_value = INTENSITY_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry, sender):
        super().__init__(coordinator)
        self._entry = entry
        self._sender = sender
        self._attr_native_value = entry.data.get(CONF_INTENSITY, DEFAULT_INTENSITY)

    async def async_set_native_value(self, value: float):
        value = int(value)
        self._entry.data[CONF_INTENSITY] = value
        self._attr_native_value = value
        await self._sender.schedule_send()
        self.async_write_ha_state()


class SmartLedSpeed(CoordinatorEntity, NumberEntity):
    _attr_name = "Smart Led Speed"
    _attr_icon = "mdi:motion-play"
    _attr_native_min_value = SPEED_MIN
    _attr_native_max_value = SPEED_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry, sender):
        super().__init__(coordinator)
        self._entry = entry
        self._sender = sender
        self._attr_native_value = entry.data.get(CONF_SPEED, DEFAULT_SPEED)

    async def async_set_native_value(self, value: float):
        value = int(value)
        self._entry.data[CONF_SPEED] = value
        self._attr_native_value = value
        await self._sender.schedule_send()
        self.async_write_ha_state()
