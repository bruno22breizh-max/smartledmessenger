import aiohttp
from urllib.parse import quote

from .const import DOMAIN, CONF_INTENSITY, CONF_SPEED

async def async_setup_entry(hass, entry):
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry

    async def handle_send(call):
        message = call.data["message"]
        intensity = call.data.get("intensity", entry.data[CONF_INTENSITY])
        speed = call.data.get("speed", entry.data[CONF_SPEED])

        msg = quote(message)
        url = (
            f"http://{entry.data['ip']}/"
            f"?message={msg}&intensity={intensity}&speed={speed}"
        )

        async with aiohttp.ClientSession() as session:
            await session.get(url)

    hass.services.async_register(
        DOMAIN,
        "send",
        handle_send,
    )

    await hass.config_entries.async_forward_entry_setups(
        entry, ["text", "number", "button"]
    )
    return True


async def async_unload_entry(hass, entry):
    hass.services.async_remove(DOMAIN, "send")
    return await hass.config_entries.async_unload_platforms(
        entry, ["text", "number", "button"]
    )
