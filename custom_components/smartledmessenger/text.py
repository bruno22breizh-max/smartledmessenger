from homeassistant.components.text import TextEntity

class SmartLedMessage(TextEntity):
    _attr_name = "Smart LED Message"
    _attr_icon = "mdi:message-text"

    def __init__(self, coordinator):
        self.coordinator = coordinator

    async def async_set_value(self, value):
        self.coordinator.send_message(value)
