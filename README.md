# DX‑Spot‑Bot mit Admin‑Webpanel

[![Deploy to Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https://github.com/Weyandp/dx-spot-bot)

## Einrichtung

1. **Forke oder klone** dieses Repository in dein GitHub‑Konto.
2. **Deploy per Klick** über den Button oben im README.
3. **Setze benötigte Umgebungsvariablen** im Railway‑Dashboard nach dem Deploy:
   - `ADMIN_USER`    (z. B. `admin`)
   - `ADMIN_PASS`    (z. B. `dxadmin2025`)
   - `DISCORD_WEBHOOK` (deine Webhook‑URL)
   - Optional:
     - `DX_CLUSTER_HOST` (Standard: `dxc.kb8zgl.net`)
     - `DX_CLUSTER_PORT` (Standard: `7373`)
     - `CALLSIGN`         (Default: `N0CALL`)
     - `FLASK_SECRET`     (für Session‑Sicherheit)

## Verwendung

- **Admin‑Login** unter `/login` (Standard: `admin` / `dxadmin2025`).
- **Dashboard** zeigt die letzten 50 DX‑Spots und ermöglicht Start/Stop des Bots.
- Bot läuft im Hintergrund und sendet DX‑Spots an deinen Discord‑Channel.

## Struktur
