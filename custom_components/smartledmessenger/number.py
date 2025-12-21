from homeassistant.components.number import NumberEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, CONF_INTENSITY, CONF_SPEED, INTENSITY_MIN, INTENSITY_MAX, SPEED_MIN, SPEED_MAX, DEFAULT_INTENSITY, DEFAULT_SPEED

async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([SmartLedIntensity(coordinator, entry), SmartLedSpeed(coordinator, entry)])

class SmartLedIntensity(CoordinatorEntity, NumberEntity):
    _attr_name = 'Smart Led Intensity'
    _attr_icon = 'mdi:brightness-6'
    _attr_native_min_value = INTENSITY_MIN
    _attr_native_max_value = INTENSITY_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._entry = entry
        self._attr_native_value = entry.data.get(CONF_INTENSITY, DEFAULT_INTENSITY)

    async def async_set_native_value(self, value: float) -> None:
        self._attr_native_value = int(value)
        self._entry.data[CONF_INTENSITY] = int(value)
        self.async_write_ha_state()

class SmartLedSpeed(CoordinatorEntity, NumberEntity):
    _attr_name = 'Smart Led Speed'
    _attr_icon = 'mdi:motion-play'
    _attr_native_min_value = SPEED_MIN
    _attr_native_max_value = SPEED_MAX
    _attr_native_step = 1

    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self._entry = entry
        self._attr_native_value = entry.data.get(CONF_SPEED, DEFAULT_SPEED)

    async def async_set_native_value(self, value: float) -> None:
        self._attr_native_value = int(value)
        self._entry.data[CONF_SPEED] = int(value)
        self.async_write_ha_state()
