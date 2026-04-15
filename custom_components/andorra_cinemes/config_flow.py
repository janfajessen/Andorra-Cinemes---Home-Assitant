"""Config flow per Andorra Cinemes."""
from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult
from .const import DOMAIN


class AndorraCinesConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow - una sola instància possible."""
    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")
        if user_input is not None:
            return self.async_create_entry(title="Andorra Cinemes", data={})
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
