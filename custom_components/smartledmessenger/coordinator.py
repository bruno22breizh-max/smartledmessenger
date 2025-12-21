import aiohttp
import asyncio
import logging
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

class SmartLedCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, ip):
        self.ip = ip
        super().__init__(hass, _LOGGER, name=DOMAIN, update_interval=SCAN_INTERVAL)

    async def _async_update_data(self):
        url = f'http://{self.ip}/'
        try:
            timeout = aiohttp.ClientTimeout(total=5)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as resp:
                    if resp.status != 200:
                        raise UpdateFailed('Device not reachable')
            return {'online': True}
        except (asyncio.TimeoutError, aiohttp.ClientError) as err:
            raise UpdateFailed('Device offline') from err
