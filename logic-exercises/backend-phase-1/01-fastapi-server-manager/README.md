# Server Inventory API

A robust RESTful API built with **FastAPI** for managing server infrastructure. This project demonstrates a full CRUD implementation with data validation and a modular professional architecture.

## Tech Stack

* **FastAPI**: Modern, high-performance web framework.
* **Pydantic**: Data validation and settings management.
* **Python 3.9+**: Base programming language.
* **Uvicorn**: An ASGI web server for Python.

## Project Structure
```text
fastapi-server-manager/
├── app/
│   ├── __init__.py      # Makes 'app' a Python package
│   ├── main.py          # API entry point and routes
│   ├── schemas.py       # Pydantic models (Data Contracts)
│   └── database.py     # In-memory data storage
├── .gitignore          # Files and folders to be ignored by Git
└── requirements.txt    # Project dependencies
```

## Setup & Installation

Clone the repository:
```bash
git clone <your-repository-url>
cd fastapi-server-manager
```

Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.
Access the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/servers/` | Retrieve a list of all registered servers. |
| POST | `/servers/` | Register a new server in the inventory. |
| PUT | `/servers/{id}` | Replace all data for a specific server. |
| PATCH | `/servers/{id}` | Update specific fields of an existing server. |
| DELETE | `/servers/{id}` | Remove a server from the system. |
| GET | `/users/` | List all registered users. |
| POST | `/users/` | Create a new user profile. |