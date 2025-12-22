from homeassistant.components.button import ButtonEntity

class SmartLedPresetUrgent(ButtonEntity):
    _attr_name = "Smart LED Urgent"
    _attr_icon = "mdi:alert-circle"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_press(self):
        self.coordinator.send_message("Urgent")

class SmartLedPresetInfo(ButtonEntity):
    _attr_name = "Smart LED Info"
    _attr_icon = "mdi:information"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_press(self):
        self.coordinator.send_message("Info")

class SmartLedPresetNight(ButtonEntity):
    _attr_name = "Smart LED Night"
    _attr_icon = "mdi:weather-night"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_press(self):
        self.coordinator.send_message("Night")
