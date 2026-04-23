# Coffee Shop Inventory API

A robust FastAPI-based backend service designed to manage a coffee shop's inventory with professional-grade features like dynamic filtering, pagination, and structured logging.

## Features

- **Full CRUD Operations**: Create, Read, Update, and Delete inventory items.
- **Advanced Filtering**: 
  - Search by product name (partial match).
  - Filter by category (`Coffee`, `Food`, `Equipment`).
  - Filter by stock status (out of stock).
  - Filter by maximum price.
- **Dynamic Sorting**: Order results by `name` or `price` in both ascending and descending order.
- **Pagination**: Efficiently handle large datasets using `limit` and `offset` parameters.
- **Professional Logging**: Integrated Python `logging` module to track system events and errors.
- **Data Validation**: Powered by Pydantic for strict type checking and error handling.

## Tech Stack

- **Language**: Python 3.x
- **Framework**: FastAPI
- **Data Serialization**: Pydantic & JSON
- **Tooling**: Pathlib for cross-platform path management.

## API Usage (Endpoints)

### GET `/inventory/`
Fetches the inventory list with the following optional query parameters:

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | Search items by name (case-insensitive). |
| `category` | `string` | Filter by `Coffee`, `Food`, or `Equipment`. |
| `max_price` | `float` | Filter items below a specific price point. |
| `out_of_stock`| `boolean`| If `true`, returns only items with 0 stock. |
| `sort_by` | `string` | Field to sort by: `name` (default) or `price`. |
| `order_desc` | `boolean`| Set to `true` for descending order. |
| `limit` | `integer`| Max results to return (default: 10). Must be > 0. |
| `offset` | `integer`| Number of items to skip (default: 0). |

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/your-username/backend-devops-pathway.git](https://github.com/your-username/backend-devops-pathway.git)
   cd coffee-shop-inventory
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

The API will be available at `http://127.0.0.1:8000`.
Access the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.