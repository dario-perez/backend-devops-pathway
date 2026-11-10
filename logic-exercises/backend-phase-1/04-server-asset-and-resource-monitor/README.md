# Server Asset and Resource Monitor

A read-only FastAPI service for querying server assets stored in a JSON file.
It supports filtering by hostname, status, and CPU usage, plus sorting and
pagination.

## Features

- Filter by hostname substring
- Filter by operational status (`Online`, `Offline`, `Maintenance`)
- Filter by minimum CPU usage
- Sort by CPU or RAM usage, ascending or descending
- Offset/limit pagination
- Seed data in `app/assets.json`
- Swagger UI at `/docs`

## Tech stack

- Python 3.13+
- FastAPI
- Pydantic
- Uvicorn

## Project structure

```text
04-server-asset-and-resource-monitor/
├── app/
│   ├── __init__.py
│   ├── assets.json   # seed data
│   ├── main.py       # app and query logic
│   └── schemas.py    # Pydantic model
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API runs at `http://127.0.0.1:8000`; interactive docs are at
`http://127.0.0.1:8000/docs`.

The data path is built from `Path(__file__)`, so the server finds
`app/assets.json` regardless of the directory you start it from.

## Data model

| Field | Type | Rules |
|---|---|---|
| `id` | UUID | Required |
| `hostname` | string | Required |
| `ip_address` | IPv4 or IPv6 address | Required |
| `status` | `Online`, `Offline`, or `Maintenance` | Defaults to `Online` |
| `cpu_usage` | float | 0–100 |
| `ram_usage` | float | 0–100 |

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Basic service response |
| GET | `/assets` | List assets with optional filters |

### `GET /assets` query parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `hostname` | string | none | Case-insensitive substring match |
| `status` | string | none | `Online`, `Offline`, or `Maintenance` |
| `min_cpu` | float | none | Only assets with `cpu_usage >= min_cpu` |
| `sort_by` | string | `cpu_usage` | `cpu_usage` or `ram_usage` |
| `order_desc` | boolean | `false` | Descending order when `true` |
| `offset` | integer | `0` | Number of results to skip |
| `limit` | integer | `10` | Maximum results; must be greater than 0 |

### Example requests

List online servers using more than 40% CPU, highest first:

```bash
curl "http://127.0.0.1:8000/assets?status=Online&min_cpu=40&sort_by=cpu_usage&order_desc=true"
```

Search by hostname and return two results:

```bash
curl "http://127.0.0.1:8000/assets?hostname=srv&limit=2"
```

Paginate through all assets, 5 at a time:

```bash
curl "http://127.0.0.1:8000/assets?offset=0&limit=5"
curl "http://127.0.0.1:8000/assets?offset=5&limit=5"
```

Sample response:

```json
[
  {
    "id": "a1b2c3d4-e5f6-4321-8765-098765432109",
    "hostname": "backup-node-01",
    "ip_address": "10.0.2.100",
    "status": "Online",
    "cpu_usage": 92.1,
    "ram_usage": 40.5
  }
]
```

A `limit` of zero or less returns `400` with
`{"detail": "Limit must be greater than 0"}`.

## What I practiced

- Query parameters and optional filters in FastAPI
- Sorting and pagination over in-memory data
- Pydantic validation with `Literal` and numeric ranges
- Structured logging
- Reading JSON data with a path derived from `__file__`

## Next improvements

- Add `POST`, `PUT`, and `DELETE` to make it a full CRUD API
- Move from JSON to SQLite or PostgreSQL
- Add `pytest` tests for filters, sorting, and pagination
- Reject negative `offset` values
