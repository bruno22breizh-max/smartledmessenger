from homeassistant.components.select import SelectEntity

class SmartLedColor(SelectEntity):
    _attr_name = "Smart LED Color"
    _attr_icon = "mdi:palette"
    _attr_options = ["white", "red", "green", "blue"]

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_select_option(self, option):
        self.coordinator.color = option
