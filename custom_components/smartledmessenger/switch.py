from homeassistant.components.switch import SwitchEntity

class SmartLedStatic(SwitchEntity):
    _attr_name = "Smart LED Static"
    _attr_icon = "mdi:pause-circle"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_turn_on(self):
        self.coordinator.static = 1

    async def async_turn_off(self):
        self.coordinator.static = 0

class SmartLedAutoClock(SwitchEntity):
    _attr_name = "Smart LED Auto Clock"
    _attr_icon = "mdi:clock-outline"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_turn_on(self):
        self.coordinator.auto_clock = True

    async def async_turn_off(self):
        self.coordinator.auto_clock = False

class SmartLedWatchdog(SwitchEntity):
    _attr_name = "Smart LED Watchdog"
    _attr_icon = "mdi:dog"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_turn_on(self):
        pass  # géré par DataUpdateCoordinator

    async def async_turn_off(self):
        pass
