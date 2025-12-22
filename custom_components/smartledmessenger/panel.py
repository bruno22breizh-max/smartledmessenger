from homeassistant.components.panel_custom import async_register_panel

async def async_register_smartled_panel(hass, host):
    async_register_panel(
        hass,
        component_name="iframe",
        sidebar_title="Smart LED",
        sidebar_icon="mdi:led-on",
        frontend_url_path="smartled",
        config={
            "url": f"/local/smartled.html?host={host}",
            "title": "Smart LED Control"
        },
        require_admin=False
    )
