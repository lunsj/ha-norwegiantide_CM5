import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

class NorwegianTideFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Norwegian Tide", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("place"): str,
                vol.Required("latitude"): float,
                vol.Required("longitude"): float,
            }),
            errors=errors
        )
