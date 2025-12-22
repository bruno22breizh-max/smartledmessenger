from datetime import datetime
import threading, asyncio
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .api import SmartLedAPI
import logging
_LOGGER = logging.getLogger(__name__)

class SmartLedCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, host, update_interval=30):
        self.api = SmartLedAPI(host)
        self.hass = hass
        super().__init__(hass, _LOGGER, name="Smart LED Coordinator", update_interval=asyncio.timedelta(seconds=update_interval))
        self.intensity = 10
        self.speed = 40
        self.static = 0
        self.local = 0
        self.auto_clock = True
        self.color = None
        self.duration = 0

    async def _async_update_data(self):
        success = await self.hass.async_add_executor_job(self.api.send, {"message": ""})
        if not success:
            raise UpdateFailed("Smart LED non joignable")
        return success

    def _is_day(self):
        hour = datetime.now().hour
        return 7 <= hour < 22

    def _apply_day_night(self):
        if self._is_day():
            self.intensity = 10
            self.speed = 40
        else:
            self.intensity = 2
            self.speed = 20

    def send_message(self, message):
        self._apply_day_night()
        params = {"message": message, "intensity": self.intensity, "speed": self.speed, "static": self.static, "local": self.local}
        if self.api.supports_color and self.color:
            params["color"] = self.color
        self.api.send(params)
        if self.duration > 0:
            threading.Timer(self.duration, self.restore_clock).start()

    def restore_clock(self):
        if not self.auto_clock:
            return
        self.api.send({"message": "", "intensity": self.intensity, "speed": self.speed, "static": 1})
