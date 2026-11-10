# Network Asset API

A small REST API built with FastAPI for managing network assets. Data is
validated with Pydantic and persisted to a local JSON file, so the project
runs without a database.

## Features

- Full CRUD for network assets
- UUID identifiers
- Pydantic validation for IP addresses and RAM values
- JSON file persistence (`app/assets.json`)
- Interactive docs at `/docs`

## Tech stack

- Python 3.13+
- FastAPI
- Pydantic
- Uvicorn

## Project structure

```text
02-network-asset-api/
├── app/
│   ├── __init__.py
│   ├── main.py       # routes and JSON storage helpers
│   └── schemas.py    # Pydantic model
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

Run these commands from the project directory:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`. Open
`http://127.0.0.1:8000/docs` for Swagger UI.

The first request creates `app/assets.json` if it does not exist. The file is
ignored by Git.

> Run `uvicorn` from this project directory. The storage path is relative
> (`app/assets.json`), so starting the server elsewhere creates the file in the
> wrong place.

## Data model

| Field | Type | Rules |
|---|---|---|
| `id` | UUID | Required |
| `hostname` | string | Required |
| `ip_address` | IPv4 or IPv6 address | Required |
| `ram_gb` | integer | Must be greater than 0 |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Basic service response |
| GET | `/assets` | List all assets |
| GET | `/assets/{asset_id}` | Get one asset by UUID |
| POST | `/assets` | Create an asset |
| PUT | `/assets/{asset_id}` | Replace an asset |
| DELETE | `/assets/{asset_id}` | Delete an asset |

### Create an asset

```bash
curl -X POST http://127.0.0.1:8000/assets \
  -H "Content-Type: application/json" \
  -d '{
    "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "hostname": "srv-app-01",
    "ip_address": "192.168.1.20",
    "ram_gb": 32
  }'
```

Response:

```json
{
  "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "hostname": "srv-app-01",
  "ip_address": "192.168.1.20",
  "ram_gb": 32
}
```

### Get one asset

```bash
curl http://127.0.0.1:8000/assets/3fa85f64-5717-4562-b3fc-2c963f66afa6
```

Returns `404` with `{"detail": "Asset not found"}` when the UUID does not
exist.

## What I practiced

- Building CRUD routes with FastAPI
- Separating routes from Pydantic schemas
- Validating IP addresses and numeric constraints
- Reading and writing JSON safely
- Returning proper `404` responses

## Next improvements

- Replace the JSON file with SQLite or PostgreSQL
- Return `201 Created` on `POST`
- Add `pytest` tests with `TestClient`
- Move the storage path to a `Path(__file__)`-based location
- Remove the unused debug `print()` from the delete route
