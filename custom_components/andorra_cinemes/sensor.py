"""Sensors per Andorra Cinemes."""
from __future__ import annotations
import logging
from typing import Any
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from .const import DOMAIN
from .coordinator import AndorraCinesCoordinator

_LOGGER = logging.getLogger(__name__)
MAX_FILM_SENSORS = 20


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: AndorraCinesCoordinator = hass.data[DOMAIN][entry.entry_id]

    entities: list[SensorEntity] = [
        AndorraCinesNowPlayingSensor(coordinator),
        AndorraCinesUpcomingSensor(coordinator),
    ]
    # Sensors individuals per film (fins a MAX_FILM_SENSORS)
    # Permet usar picture-glance cards natives de HA
    for i in range(MAX_FILM_SENSORS):
        entities.append(AndorraCinesFilmSensor(coordinator, i))

    async_add_entities(entities)


class AndorraCinesNowPlayingSensor(CoordinatorEntity, SensorEntity):
    """Sensor principal: llista de tots els films en cartell."""
    _attr_unique_id = "andorra_cinemes_now_playing"
    _attr_name = "Andorra Cinemes – En Cartell"
    _attr_icon = "mdi:movie-open"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name=self.coordinator.config_entry.title,
            manufacturer="Cinemes illa Carlemany",
            model="cinemesilla.com",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url="https://cinemesilla.com",
        )

    def __init__(self, coordinator: AndorraCinesCoordinator) -> None:
        super().__init__(coordinator)

    @property
    def native_value(self) -> int:
        return len((self.coordinator.data or {}).get("now_playing", []))

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        films = (self.coordinator.data or {}).get("now_playing", [])
        # Versió reduïda per evitar el límit de 16KB: sense sinopsis ni repartiment
        films_light = []
        for f in films:
            films_light.append({
                "id":              f.get("id"),
                "title":           f.get("title"),
                "poster_url":      f.get("poster_url"),
                "genre":           f.get("genre"),
                "rating":          f.get("rating"),
                "duration":        f.get("duration"),
                "release_date":    f.get("release_date", ""),
                "on_advance":      f.get("on_advance", False),
                "available_dates": f.get("available_dates", []),
                "showtimes_today": f.get("showtimes_today", []),
                "showtimes_today_full": f.get("showtimes_today_full", []),
                "film_page_url":   f.get("film_page_url"),
            })
        return {"films": films_light, "count": len(films)}

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success


class AndorraCinesFilmSensor(CoordinatorEntity, SensorEntity):
    """
    Sensor individual per a cada film (fins a MAX_FILM_SENSORS).
    Té entity_picture = URL del pòster → compatible amb picture-glance cards.
    state = horaris d'avui (string) o "No disponible"
    """
    def __init__(self, coordinator: AndorraCinesCoordinator, index: int) -> None:
        super().__init__(coordinator)
        self._index = index
        self._attr_unique_id = f"andorra_cinemes_film_{index + 1}"
        self._attr_name = f"Andorra Cinemes – Film {index + 1}"
        self._attr_icon = "mdi:movie"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name=self.coordinator.config_entry.title,
            manufacturer="Cinemes illa Carlemany",
            model="cinemesilla.com",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url="https://cinemesilla.com",
        )

    def _get_film(self) -> dict | None:
        films = (self.coordinator.data or {}).get("now_playing", [])
        if self._index < len(films):
            return films[self._index]
        return None

    @property
    def native_value(self) -> str:
        film = self._get_film()
        if not film:
            return "No disponible"
        times = film.get("showtimes_today", [])
        return " · ".join(times) if times else "Sense sessions avui"

    @property
    def entity_picture(self) -> str | None:
        """Retorna l'URL del pòster — HA l'utilitza com a imatge de l'entitat."""
        film = self._get_film()
        return film.get("poster_url") if film else None

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        film = self._get_film()
        if not film:
            return {"active": False}
        return {
            "active":          True,
            "title":           film.get("title"),
            "genre":           film.get("genre"),
            "rating":          film.get("rating"),
            "duration":        film.get("duration"),
            "synopsis":        film.get("synopsis", ""),
            "director":        film.get("director"),
            "available_dates": film.get("available_dates", []),
            "showtimes_today_full": film.get("showtimes_today_full", []),
            "showtimes_by_date":    film.get("showtimes_by_date", {}),
            "film_page_url":   film.get("film_page_url"),
            "trailer_url":     film.get("trailer_url"),
        }

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success


class AndorraCinesUpcomingSensor(CoordinatorEntity, SensorEntity):
    """Pròximes estrenes."""
    _attr_unique_id = "andorra_cinemes_upcoming"
    _attr_name = "Andorra Cinemes – Pròximes Estrenes"
    _attr_icon = "mdi:movie-star"

    @property
    def device_info(self) -> DeviceInfo:
        return DeviceInfo(
            identifiers={(DOMAIN, self.coordinator.config_entry.entry_id)},
            name=self.coordinator.config_entry.title,
            manufacturer="Cinemes illa Carlemany",
            model="cinemesilla.com",
            entry_type=DeviceEntryType.SERVICE,
            configuration_url="https://cinemesilla.com",
        )

    def __init__(self, coordinator: AndorraCinesCoordinator) -> None:
        super().__init__(coordinator)

    @property
    def native_value(self) -> int:
        return len((self.coordinator.data or {}).get("upcoming", []))

    @property
    def extra_state_attributes(self) -> dict[str, Any]:
        return {
            "upcoming_films": (self.coordinator.data or {}).get("upcoming", [])
        }

    @property
    def available(self) -> bool:
        return self.coordinator.last_update_success
        