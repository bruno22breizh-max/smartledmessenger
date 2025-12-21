from homeassistant import config_entries
import voluptuous as vol
from .const import DOMAIN, CONF_IP, CONF_INTENSITY, CONF_SPEED, INTENSITY_MIN, INTENSITY_MAX, SPEED_MIN, SPEED_MAX, DEFAULT_INTENSITY, DEFAULT_SPEED

class SmartLedMessengerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input:
            return self.async_create_entry(title=f'SmartLed {user_input[CONF_IP]}', data=user_input)
        return self.async_show_form(
            step_id='user',
            data_schema=vol.Schema({
                vol.Required(CONF_IP): str,
                vol.Optional(CONF_INTENSITY, default=DEFAULT_INTENSITY): vol.All(int, vol.Range(INTENSITY_MIN, INTENSITY_MAX)),
                vol.Optional(CONF_SPEED, default=DEFAULT_SPEED): vol.All(int, vol.Range(SPEED_MIN, SPEED_MAX)),
            })
        )
