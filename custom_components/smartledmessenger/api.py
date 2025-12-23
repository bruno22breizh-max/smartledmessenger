import aiohttp

class SmartLedAPI:
    def __init__(self, host):
        self.host = host

    async def send(self, params):
        url = f"http://{self.host}/"
        async with aiohttp.ClientSession() as session:
            await session.get(url, params=params)

    async def show_message(self, message, intensity=10, speed=40, static=0):
        await self.send({
            "message": message,
            "intensity": intensity,
            "speed": speed,
            "static": static
        })

    async def show_clock(self):
        await self.send({"message": ""})
