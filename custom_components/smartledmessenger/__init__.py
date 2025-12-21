from .const import DOMAIN
from .coordinator import SmartLedCoordinator

async def async_setup_entry(hass, entry):
    coordinator = SmartLedCoordinator(hass, entry.data['ip'])
    await coordinator.async_config_entry_first_refresh()
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, ['text', 'number', 'button'])
    return True

async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_unload_platforms(entry, ['text', 'number', 'button'])
