<div align="center">

# Andorra Cinemes <br> Home Assistant Integration

<img src="brands/icon@2x.png" width="250"/>

![Version](https://img.shields.io/badge/version-1.5.24-blue?style=for-the-badge)
![HA](https://img.shields.io/badge/Home%20Assistant-2024.1+-orange?style=for-the-badge&logo=home-assistant)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python)
![HACS](https://img.shields.io/badge/HACS-Custom-41BDF5?style=for-the-badge&logo=homeassistantcommunitystore&logoColor=white)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-Donate-yellow?style=for-the-badge&logo=buymeacoffee)](https://www.buymeacoffee.com/janfajessen)
[![Patreon](https://img.shields.io/badge/Patreon-Support-red?style=for-the-badge&logo=patreon)](https://www.patreon.com/janfajessen)
<!--[![Ko-Fi](https://img.shields.io/badge/Ko--Fi-Support-teal?style=for-the-badge&logo=ko-fi)](https://ko-fi.com/janfajessen)
[![GitHub Sponsors](https://img.shields.io/badge/GitHub%20Sponsors-Support-pink?style=for-the-badge&logo=githubsponsors)](https://github.com/sponsors/janfajessen)
[![PayPal](https://img.shields.io/badge/PayPal-Donate-blue?style=for-the-badge&logo=paypal)](https://paypal.me/janfajessen)-->


**Integració no oficial per als Cinemes Illa Carlemany d'Andorra**

Cartellera en temps real · Horaris · Pòsters · Sinopsis · Tràilers

[Instal·lació](#instal·lació) · [Sensors](#sensors) · [Lovelace](#lovelace) · [Automatitzacions](#automatitzacions)

---

</div>

<details>
<summary>🇪🇸 Español</summary>

## Andorra Cinemes para Home Assistant

Integración no oficial para los Cines Illa Carlemany de Andorra. Muestra la cartelera actual, horarios, pósters, sinopsis y tráilers directamente en Home Assistant.

### Instalación
1. Copia la carpeta `andorra_cinemes` a `/config/custom_components/`
2. Reinicia Home Assistant
3. Ve a **Configuración → Integraciones → Añadir integración**
4. Busca **"Andorra Cinemes"**
<img src="brands/icon@2x.png" width="100"/>

### Sensores creados
- `sensor.andorra_cinemes_en_cartell` — Cartelera actual
- `sensor.andorra_cinemes_film_1` ... `film_20` — Sensores individuales por película
- `sensor.andorra_cinemes_proximes_estrenes` — Próximos estrenos

### Configuración
Edita `const.py` para ajustar el intervalo de actualización:
```python
SCAN_INTERVAL_MINUTES = 1440  # 24 horas (recomendado)
```

</details>

<details>
<summary>🇫🇷 Français</summary>

## Andorra Cinemes pour Home Assistant

Intégration non officielle pour les Cinémas Illa Carlemany d'Andorre. Affiche la programmation actuelle, les horaires, les affiches, les synopsis et les bandes-annonces directement dans Home Assistant.

### Installation
1. Copiez le dossier `andorra_cinemes` dans `/config/custom_components/`
2. Redémarrez Home Assistant
3. Allez dans **Paramètres → Intégrations → Ajouter une intégration**
4. Recherchez **"Andorra Cinemes"**
<img src="brands/icon@2x.png" width="100"/>

### Capteurs créés
- `sensor.andorra_cinemes_en_cartell` — Programme actuel
- `sensor.andorra_cinemes_film_1` ... `film_20` — Capteurs individuels par film
- `sensor.andorra_cinemes_proximes_estrenes` — Prochaines sorties

### Configuration
Éditez `const.py` pour ajuster l'intervalle de mise à jour :
```python
SCAN_INTERVAL_MINUTES = 1440  # 24 heures (recommandé)
```

</details>

<details>
<summary>🇬🇧 English</summary>

## Andorra Cinemes for Home Assistant

Unofficial integration for the Cinemes Illa Carlemany cinema in Andorra. Displays the current billboard, showtimes, posters, synopses and trailers directly in Home Assistant.

### Installation
1. Copy the `andorra_cinemes` folder to `/config/custom_components/`
2. Restart Home Assistant
3. Go to **Settings → Integrations → Add Integration**
4. Search for **"Andorra Cinemes"**
<img src="brands/icon@2x.png" width="100"/>

### Created sensors
- `sensor.andorra_cinemes_en_cartell` — Current billboard
- `sensor.andorra_cinemes_film_1` ... `film_20` — Individual sensors per film
- `sensor.andorra_cinemes_proximes_estrenes` — Upcoming releases

### Configuration
Edit `const.py` to adjust the update interval:
```python
SCAN_INTERVAL_MINUTES = 1440  # 24 hours (recommended)
```

</details>

<details>
<summary>🇵🇹 Português</summary>

## Andorra Cinemes para Home Assistant

Integração não oficial para o Cinema Illa Carlemany de Andorra. Mostra a programação atual, horários, cartazes, sinopses e trailers diretamente no Home Assistant.

### Instalação
1. Copie a pasta `andorra_cinemes` para `/config/custom_components/`
2. Reinicie o Home Assistant
3. Vá a **Configurações → Integrações → Adicionar integração**
4. Pesquise **"Andorra Cinemes"**
<img src="brands/icon@2x.png" width="100"/>

### Sensores criados
- `sensor.andorra_cinemes_en_cartell` — Programação atual
- `sensor.andorra_cinemes_film_1` ... `film_20` — Sensores individuais por filme
- `sensor.andorra_cinemes_proximes_estrenes` — Próximas estreias

### Configuração
Edite `const.py` para ajustar o intervalo de atualização:
```python
SCAN_INTERVAL_MINUTES = 1440  # 24 horas (recomendado)
```

</details>
---

## ✨ Característiques

- 🎭 **Cartellera actual** amb totes les pel·lícules en cartell
- 🗓️ **Horaris per dia** amb format i link de compra d'entrades
- 🖼️ **Pòsters** carregats automàticament
- 📖 **Sinopsis, durada, director i repartiment**
- 🎥 **Tràilers de YouTube** amb miniatura
- 📅 **Pròximes estrenes** de tot l'any
- 🔄 **Actualització automàtica** configurable
- 🏠 **Compatible amb HA 2026.2+** sense dependències externes de HACS

---

## 📦 Instal·lació

### Requisits
- Home Assistant 2026.2 o superior
- `beautifulsoup4>=4.12.0` (s'instal·la automàticament)

### Manual

1. Copia la carpeta `andorra_cinemes` a `/config/custom_components/`
2. Reinicia Home Assistant
3. Ves a **Configuració → Integracions → Afegeix integració**
4. Cerca **"Andorra Cinemes"** i fes clic a **Configurar**
<img src="brands/icon@2x.png" width="100"/>

```
config/
└── custom_components/
    └── andorra_cinemes/
        ├── __init__.py
        ├── coordinator.py
        ├── sensor.py
        ├── config_flow.py
        ├── const.py
        ├── manifest.json
        └── strings.json
```

### Configuració opcional

Edita `const.py` per ajustar l'interval d'actualització:

```python
# Recomanat: 1440 minuts (24 hores) per a cartellera setmanal
SCAN_INTERVAL_MINUTES = 1440
```

---

## 📡 Sensors

La integració crea **22 sensors** agrupats en un dispositiu únic:

### `sensor.andorra_cinemes_en_cartell`
| Camp | Descripció |
|------|-----------|
| `state` | Nombre de pel·lícules en cartell |
| `films` | Llista completa de films amb horaris |
| `films[].title` | Títol de la pel·lícula |
| `films[].poster_url` | URL del pòster |
| `films[].genre` | Gènere |
| `films[].rating` | Classificació d'edat |
| `films[].duration` | Durada en minuts |
| `films[].release_date` | Data d'estrena |
| `films[].on_advance` | `true` si és venda anticipada (òpera, concert) |
| `films[].showtimes_today` | Horaris d'avui `["19:45", "22:00"]` |
| `films[].showtimes_by_date` | Horaris per data amb link de compra |
| `films[].film_page_url` | URL de la pàgina del film |

### `sensor.andorra_cinemes_film_1` ... `film_20`
Sensors individuals per a cada pel·lícula. Inclouen:
- `entity_picture` → URL del pòster (compatible amb cards de HA)
- `synopsis` → Sinopsis completa
- `trailer_url` → URL del tràiler de YouTube
- `director`, `cast` → Fitxa tècnica
- `showtimes_by_date` → Tots els horaris amb link de compra

### `sensor.andorra_cinemes_proximes_estrenes`
| Camp | Descripció |
|------|-----------|
| `state` | Nombre de pròximes estrenes |
| `upcoming_films[].title` | Títol |
| `upcoming_films[].poster_url` | URL del pòster |
| `upcoming_films[].release_date` | Data d'estrena prevista |
| `upcoming_films[].genre` | Gènere |

---

## 🃏 Lovelace

### Cartellera amb pòsters, horaris i sinopsis

```yaml
type: markdown
content: >
  {% set films = state_attr('sensor.andorra_cinemes_en_cartell', 'films') %}
  {% if films %}
  {% set films = films | selectattr('on_advance', 'eq', false) | list | sort(attribute='release_date', reverse=true) %}
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;padding:4px">
  {% for f in films %}
  {% set extra = namespace(synopsis='', trailer='') %}
  {% for i in range(1, 21) %}
    {% if state_attr('sensor.andorra_cinemes_film_' ~ i, 'title') == f.title %}
      {% set extra.synopsis = state_attr('sensor.andorra_cinemes_film_' ~ i, 'synopsis') %}
      {% set extra.trailer = state_attr('sensor.andorra_cinemes_film_' ~ i, 'trailer_url') %}
    {% endif %}
  {% endfor %}
  <div style="text-align:center">
  <a href="{{ f.film_page_url }}" target="_blank">
  <img src="{{ f.poster_url }}" style="width:100%;border-radius:6px;display:block">
  </a>
  <div style="font-size:11px;font-weight:bold;margin-top:4px"><b>{{ f.title }}</b></div>
  <div style="font-size:10px;color:var(--secondary-text-color)">{{ f.genre }} · {{ f.rating }} · {{ f.duration }}min</div>
  <div style="font-size:10px;color:var(--primary-color)"><b>{{ f.showtimes_today | join(' · ') }}</b></div>
  <div style="font-size:9px;color:var(--secondary-text-color);margin-top:4px;text-align:left"><small><small>{{ extra.synopsis }}</small></small></div>
  {% if extra.trailer and extra.trailer != '-' %}
  <a href="{{ extra.trailer | replace('embed/', 'watch?v=') }}" target="_blank" style="display:flex;align-items:center;gap:4px;margin-top:4px;text-decoration:none">
  <img src="https://img.youtube.com/vi/{{ extra.trailer.split('/')[-1] }}/mqdefault.jpg" style="width:60px;height:40px;object-fit:cover;border-radius:4px">
  <img src="/local/Youtube_logo.png" style="max-width:24px;max-height:16px;object-fit:contain">
  </a>
  {% endif %}
  </div>
  {% endfor %}
  </div>
  {% endif %}
```

### Pròximes estrenes (grid de 2 columnes)

```yaml
type: grid
columns: 2
square: false
cards:
  - type: markdown
    content: >
      {% set upcoming = state_attr('sensor.andorra_cinemes_proximes_estrenes', 'upcoming_films') %}
      {% for f in upcoming[0::2] %}
      <img src="{{ f.poster_url }}" style="width:100%;border-radius:4px">
      <div style="font-size:9px;font-weight:bold">{{ f.title }}</div>
      <div style="font-size:8px;color:var(--secondary-text-color)">{{ f.release_date }}</div>
      {% endfor %}
  - type: markdown
    content: >
      {% set upcoming = state_attr('sensor.andorra_cinemes_proximes_estrenes', 'upcoming_films') %}
      {% for f in upcoming[1::2] %}
      <img src="{{ f.poster_url }}" style="width:100%;border-radius:4px">
      <div style="font-size:9px;font-weight:bold">{{ f.title }}</div>
      <div style="font-size:8px;color:var(--secondary-text-color)">{{ f.release_date }}</div>
      {% endfor %}
```

---

## ⚡ Automatitzacions

### 🔔 Notificació de cartellera nova cada dilluns

```yaml
alias: "Cinema - Cartellera setmanal"
description: "Notifica la cartellera nova cada divendres al matí"
trigger:
  - platform: time
    at: "09:00:00"
condition:
  - condition: time
    weekday:
      - fri
action:
  - service: notify.telegram_jan
    data:
      message: >
        🎬 *Cartellera Cinemes Illa Carlemany*
        {% set films = state_attr('sensor.andorra_cinemes_en_cartell', 'films') %}
        {% set films = films | selectattr('on_advance', 'eq', false) | list | sort(attribute='release_date', reverse=true) %}
        {% for f in films %}
        🎭 *{{ f.title }}* ({{ f.genre }}, {{ f.duration }}min)
        🕐 Avui: {{ f.showtimes_today | join(' · ') if f.showtimes_today else 'Sense sessió avui' }}
        {% endfor %}
mode: single
```

### 🎬 Notificació quan s'estrena una pel·lícula nova

```yaml
alias: "Cinema - Estrena nova detectada"
description: "Notifica quan apareix una pel·lícula nova a la cartellera"
trigger:
  - platform: state
    entity_id: sensor.andorra_cinemes_en_cartell
action:
  - service: notify.telegram_jan
    data:
      message: >
        🎉 La cartellera ha canviat!
        Ara hi ha {{ states('sensor.andorra_cinemes_en_cartell') }} pel·lícules.
        Obre Home Assistant per veure la cartellera actualitzada.
mode: single
```

### ⏰ Recordatori de sessió del vespre

```yaml
alias: "Cinema - Recordatori sessió vespre"
description: "Recorda les sessions del vespre si hi ha pel·lícules"
trigger:
  - platform: time
    at: "17:00:00"
condition:
  - condition: template
    value_template: >
      {% set films = state_attr('sensor.andorra_cinemes_en_cartell', 'films') %}
      {% set films = films | selectattr('on_advance', 'eq', false) | list %}
      {{ films | selectattr('showtimes_today', 'ne', []) | list | length > 0 }}
action:
  - service: notify.telegram_jan
    data:
      message: >
        🍿 Sessions de cinema avui!
        {% set films = state_attr('sensor.andorra_cinemes_en_cartell', 'films') %}
        {% set films = films | selectattr('on_advance', 'eq', false) | list %}
        {% for f in films if f.showtimes_today %}
        🎬 {{ f.title }}: {{ f.showtimes_today | join(' · ') }}
        {% endfor %}
mode: single
```

---

## 🏗️ Arquitectura tècnica

La integració fa scraping de [cinemesilla.com](https://cinemesilla.com) que utilitza **Laravel + Vue 3**. Les dades estan disponibles directament a l'HTML estàtic com a props Vue del component `<Cinemaindexpage>`:

```
:fullsessionsinfo='[{
  "ID_Espectaculo": 11873,
  "Titulo": "SCREAM 7",
  "HoraReal": "2026-03-17 19:45:00.000",
  "Cartel": "scream-7.jpg",
  ...
}]'
```

No es fa cap crida a API externa — tot s'extreu d'una sola petició GET a la pàgina principal.

```
cinemesilla.com (1 petició GET)
        │
        ▼
    coordinator.py
    _extract_prop("fullsessionsinfo")
        │
        ├── _build_film() per cada ID_Espectaculo únic
        │       ├── Agrupa sessions per data
        │       └── Construeix showtimes_by_date
        │
        └── _extract_upcoming() (HTML estàtic)
```

---

## 🤝 Contribucions

Les contribucions són benvingudes! Obre un issue o pull request.

## 📄 Llicència

MIT © 2026

---

