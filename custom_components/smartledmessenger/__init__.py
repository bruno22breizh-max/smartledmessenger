from .panel import async_register_smartled_panel
from .coordinator import SmartLedCoordinator

async def async_setup_entry(hass, entry):
    coordinator = SmartLedCoordinator(hass, entry.data["host"])
    hass.data.setdefault("smartledmessenger", {})[entry.entry_id] = coordinator

    await hass.config_entries.async_forward_entry_setups(
        entry,
        ["text", "number", "switch", "button", "select"]
    )

    if entry.options.get("sidebar", True):
        await async_register_smartled_panel(hass, entry.data["host"])

    return True
