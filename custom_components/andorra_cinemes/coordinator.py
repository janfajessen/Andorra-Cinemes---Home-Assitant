"""DataUpdateCoordinator per Andorra Cinemes (cinemesilla.com).

Arquitectura definitiva confirmada via view-source:
- Pàgina principal conté <Cinemaindexpage> amb la prop:
  :fullsessionsinfo='[{Titulo, Cartel, NombreGenero, ID_Espectaculo,
                       HoraReal, Hora, diacompleto, Duracion, ...}]'
  Cada entrada = una sessió. No cal visitar cap altra pàgina.
- Properes estrenes: HTML estàtic a la secció PROPERES ESTRENES.
"""
from __future__ import annotations

import html as html_module
import json
import logging
import re
from collections import defaultdict
from datetime import datetime, timedelta

import aiohttp
from bs4 import BeautifulSoup

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    DOMAIN,
    BASE_URL,
    MAIN_PAGE_URL,
    THEATER_ID,
    THEATER_NAME,
    SCAN_INTERVAL_MINUTES,
)

_LOGGER = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/123.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*;q=0.8",
    "Accept-Language": "ca,es;q=0.9,en;q=0.8",
}


class AndorraCinesCoordinator(DataUpdateCoordinator):

    def __init__(self, hass: HomeAssistant) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(minutes=SCAN_INTERVAL_MINUTES),
        )

    async def _async_update_data(self) -> dict:
        try:
            async with aiohttp.ClientSession(headers=HEADERS) as session:
                async with session.get(MAIN_PAGE_URL) as resp:
                    resp.raise_for_status()
                    html = await resp.text()
            _LOGGER.debug("HTML principal: %d bytes", len(html))
            return self._parse_main_page(html)
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error connectant: {err}") from err

    def _parse_main_page(self, html: str) -> dict:
        now_playing = self._extract_now_playing(html)
        upcoming = self._extract_upcoming(html)
        _LOGGER.info("Cartellera: %d pel·lícules, %d pròximes estrenes",
                     len(now_playing), len(upcoming))
        return {"now_playing": now_playing, "upcoming": upcoming}

    def _extract_now_playing(self, html: str) -> list[dict]:
        raw = self._extract_prop(html, "fullsessionsinfo")
        if not raw:
            _LOGGER.warning(
                "No s'ha trobat :fullsessionsinfo a la pàgina. "
                "HTML: %d bytes", len(html)
            )
            return []
        try:
            sessions: list[dict] = json.loads(html_module.unescape(raw))
        except Exception as ex:
            _LOGGER.error("Error parsejant fullsessionsinfo: %s", ex)
            return []
        if not isinstance(sessions, list) or not sessions:
            return []
        _LOGGER.debug("fullsessionsinfo: %d sessions", len(sessions))

        films_sessions: dict[str, list[dict]] = defaultdict(list)
        for sess in sessions:
            fid = str(sess.get("ID_Espectaculo", ""))
            if fid:
                films_sessions[fid].append(sess)

        now_playing = []
        for film_id, film_sessions in films_sessions.items():
            film = self._build_film(film_id, film_sessions)
            if film:
                now_playing.append(film)

        now_playing.sort(key=lambda f: f.get("title", ""))
        return now_playing

    def _extract_prop(self, html: str, prop_name: str) -> str | None:
        """Extreu el valor d'una prop Vue :prop_name='[...]' de l'HTML.
        Usa [^']+ per evitar que ] dins el JSON aturi el match massa aviat.
        El contingut usa &quot; per les cometes, mai cometes simples literals.
        """
        # Cometes simples: tot el que no sigui cometa simple
        m = re.search(
            r":" + re.escape(prop_name) + r"\s*='([^']+)'",
            html, re.IGNORECASE
        )
        if m:
            return m.group(1)
        # Cometes dobles: tot el que no sigui cometa doble
        m = re.search(
            r':' + re.escape(prop_name) + r'\s*="([^"]+)"',
            html, re.IGNORECASE
        )
        if m:
            return m.group(1)
        return None

    def _build_film(self, film_id: str, sessions: list[dict]) -> dict | None:
        if not sessions:
            return None
        first = sessions[0]
        title = (first.get("Titulo") or first.get("NombreEspectaculo") or "").strip()
        if not title:
            return None

        poster_filename = (first.get("Cartel") or first.get("ImagenPase") or "").strip()
        poster_url = (
            f"{BASE_URL}/Posters/{poster_filename}"
            if poster_filename and not poster_filename.startswith("http")
            else poster_filename
        )

        from urllib.parse import quote
        film_page_url = (
            f"{BASE_URL}/FilmTheaterPage/{film_id}/"
            f"{quote(title)}/{THEATER_ID}/{quote(THEATER_NAME)}"
        )

        showtimes_by_date: dict[str, list[dict]] = defaultdict(list)
        for sess in sessions:
            hora_real = sess.get("HoraReal") or ""
            hora_simple = sess.get("Hora") or ""
            diacompleto = sess.get("diacompleto") or ""
            if hora_real:
                try:
                    dt = datetime.strptime(hora_real[:16], "%Y-%m-%d %H:%M")
                    date_key = dt.strftime("%d/%m/%Y")
                    time_str = dt.strftime("%H:%M")
                except ValueError:
                    date_key = diacompleto
                    time_str = hora_simple
            else:
                date_key = diacompleto
                time_str = hora_simple
            if not date_key or not time_str:
                continue
            session_id = str(sess.get("ID_Pase") or "")
            formato = sess.get("NombreFormato") or ""
            buy_url = (
                f"{BASE_URL}/Session/{THEATER_ID}/"
                f"{quote(THEATER_NAME)}/{film_id}/{quote(title)}/{session_id}"
            ) if session_id else ""
            entry = {"time": time_str, "format": formato,
                     "session_id": session_id, "buy_url": buy_url}
            if entry not in showtimes_by_date[date_key]:
                showtimes_by_date[date_key].append(entry)

        for dk in showtimes_by_date:
            showtimes_by_date[dk].sort(key=lambda s: s["time"])

        available_dates = sorted(showtimes_by_date.keys())
        today = datetime.now().strftime("%d/%m/%Y")
        showtimes_today = (
            showtimes_by_date.get(today)
            or (showtimes_by_date.get(available_dates[0]) if available_dates else [])
        )

        return {
            "id": film_id,
            "title": title,
            "poster_url": poster_url,
            "genre": first.get("NombreGenero") or "",
            "rating": first.get("AbreviaturaCalificacion") or "",
            "duration": str(first.get("Duracion") or ""),
            "director": first.get("Director") or "",
            "cast": first.get("Interpretes") or "",
            "synopsis": first.get("Sinopsis") or "",
            "release_date": first.get("FechaEstreno") or "",
            "trailer_url": first.get("Video") or "",
            "on_advance": bool(first.get("on_advance", 0)),
            "available_dates": available_dates,
            "showtimes_today": [s["time"] for s in showtimes_today],
            "showtimes_today_full": showtimes_today,
            "showtimes_by_date": dict(showtimes_by_date),
            "film_page_url": film_page_url,
        }

    def _extract_upcoming(self, html: str) -> list[dict]:
        soup = BeautifulSoup(html, "html.parser")
        upcoming = []
        seen: set[str] = set()
        for img in soup.find_all("img", src=re.compile(r"/Posters/", re.IGNORECASE)):
            src = img.get("src", "")
            alt = img.get("alt", "").strip()
            if not src:
                continue
            poster_url = src if src.startswith("http") else f"{BASE_URL}{src}"
            parent = img.parent
            title = alt
            for ancestor in ([parent] + list(parent.parents))[:4]:
                if not hasattr(ancestor, "find"):
                    continue
                h = ancestor.find(["h2", "h3", "h4"])
                if h:
                    t = h.get_text(strip=True)
                    if t:
                        title = t
                        break
            if not title or title in seen:
                continue
            seen.add(title)
            date_text = ""
            if parent:
                m = re.search(r"\d{2}/\d{2}/\d{2,4}", parent.get_text(" "))
                if m:
                    date_text = m.group(0)
            genre = ""
            if parent:
                for t in parent.stripped_strings:
                    t = t.strip()
                    if t and t != title and not re.match(r"\d", t) and "/" not in t:
                        genre = t
                        break
            upcoming.append({
                "title": title,
                "poster_url": poster_url,
                "release_date": date_text,
                "genre": genre,
            })
        return upcoming
        