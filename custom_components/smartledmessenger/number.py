from homeassistant.components.number import NumberEntity

class SmartLedIntensity(NumberEntity):
    _attr_name = "Smart LED Intensity"
    _attr_icon = "mdi:brightness-6"
    _attr_min_value = 0
    _attr_max_value = 15
    _attr_step = 1

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_set_native_value(self, value):
        self.coordinator.intensity = int(value)

class SmartLedSpeed(NumberEntity):
    _attr_name = "Smart LED Speed"
    _attr_icon = "mdi:speedometer"
    _attr_min_value = 10
    _attr_max_value = 50
    _attr_step = 1

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_set_native_value(self, value):
        self.coordinator.speed = int(value)
