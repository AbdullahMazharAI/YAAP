# YAAP — Developer Setup (Minimal)

> Get the backend running in ~10 minutes. Read all the way through once before starting.

---

## Before You Start — File Sharing Rules

| What to share | How |
|---|---|
| **Source code** | Private GitHub repo (never commit `.env`) |
| **Supabase credentials** | Share via a **password manager** link (not Gmail/chat) |
| **Firebase credentials** | Share `firebase-credentials.json` via encrypted channel only |
| **`.env` file** | Never commit. Share via private message only. |

---

## 1. Prerequisites

| Tool | Version | Notes |
|---|---|---|
| **Python** | 3.11+ | Backend |
| **Java JDK** | 17 | Android build |
| **Android Studio** | Hedgehog 2023.1+ | Frontend |
| **Docker Desktop** | 24+ | All backend services |
| **ADB** | any | Comes with Android Studio |
| **RAM** | 8 GB min | 16 GB recommended |
| **GPU** | Optional | Only needed for XTTS / Whisper (voice calls) |

---

## 2. Credentials You Need (from project owner)

- [ ] Filled `.env` file → place in `backend/`
- [ ] `firebase-credentials.json` → place in `backend/`
- [ ] Supabase project URL + keys (already inside `.env`)
- [ ] DeepL API key (already inside `.env`) — required for chat translation

---

## 3. Backend Setup (One Command)

```bash
cd backend

# First time: copy and fill env file
copy .env.example .env

# Start core services (Django + Redis + Celery + Nginx)
docker compose up --build -d web celery_worker celery_beat redis nginx

# First time only: run migrations
docker compose exec web python manage.py migrate
```

Backend URL: http://localhost:8080

---

## 4. Services — What Is Mandatory?

| Service | Mandatory | Notes |
|---|---|---|
| Redis | YES | Channel layer + Celery broker |
| Django (web) | YES | Daphne ASGI on port 8000 |
| Celery Worker | YES | Runs translation & notification tasks |
| Celery Beat | YES | Scheduled cleanup tasks |
| Nginx | YES | Reverse proxy on port 8080 |
| Supabase (PostgreSQL) | YES | Cloud — no local setup needed |
| XTTS | NO | Voice cloning — needs GPU |
| Whisper | NO | Speech-to-text — needs GPU |
| Coturn | NO | WebRTC TURN relay — only for calls over mobile data |

**Chat testing only? Skip XTTS, Whisper, Coturn.**

---

## 5. Minimal .env Values for Chat

Copy `backend/.env.example` → `backend/.env` and fill these:

```env
DJANGO_SECRET_KEY=<any 50+ char random string>
DJANGO_DEBUG=True

SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=<anon key>
SUPABASE_SERVICE_ROLE_KEY=<service role key>
DATABASE_URL=postgresql://postgres:<pass>@db.<project>.supabase.co:5432/postgres

DEEPL_API_KEY=<deepl api key>

GOOGLE_CLIENT_ID=<client id>
GOOGLE_CLIENT_SECRET=<client secret>

FIREBASE_CREDENTIALS_PATH=/app/firebase-credentials.json
```

Redis/Celery URLs are set automatically by docker-compose — leave them blank in .env.

---

## 6. Android Setup

```bash
# 1. Open frontend/ in Android Studio
# 2. Connect phone via USB
# 3. Run ADB reverse (every time you reconnect the phone):
adb reverse tcp:8080 tcp:8080

# 4. Build & run from Android Studio
```

### Two Devices at the Same Time

```powershell
adb devices                               # get serial numbers
adb -s <SERIAL1> reverse tcp:8080 tcp:8080
adb -s <SERIAL2> reverse tcp:8080 tcp:8080
```

---

## 7. Database Schema

Run `backend/supabase_schema.sql` once in the Supabase SQL editor to create all tables.

---

## 8. Useful Docker Commands

```bash
docker compose logs -f web               # Django logs
docker compose logs -f celery_worker     # Translation/task logs
docker compose restart celery_worker     # Restart one service
docker compose down                      # Stop everything
docker compose down -v                   # Full reset (clears Redis)
```

---

## What You Do NOT Need to Set Up

- Local PostgreSQL — Supabase handles it
- XTTS / Whisper — only for voice calling feature
- Coturn — only for calls over mobile data
- Sentry — leave SENTRY_DSN blank for local dev
