class SmartLedCoordinator:
    def __init__(self, hass, entry):
        self.hass = hass
        self.entry = entry
        self.last_message = None
