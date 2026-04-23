import json
import logging
from pathlib import Path
from typing import Optional, Literal
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from app.schemas import Asset



app = FastAPI()



# ------------ PATH CONFIG ------------
script_path = Path(__file__).resolve().parent
json_file = script_path / "assets.json"



# ------------ LOGGING CONFIG ------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)



# ------------ DATA HANDLING ------------
def load_data():
    if not json_file.exists():
        with open(json_file, "w") as file:
            json.dump([], file, indent=4)
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []
    
def save_data(assets):
    try:
        compatible_data = jsonable_encoder(assets)
        with open(json_file, "w") as file:
            json.dump(compatible_data, file, indent=4)
    except json.decoder.JSONDecodeError:
        return []
    except Exception as e:
        logger.error(f"Error saving data: {e}")



# ------------ GET ------------
@app.get("/")
def home():
    return {"message": "Here we go again"}

@app.get("/assets")
def get_assets(
    hostname: Optional[str] = None,
    status: Optional[Literal["Online", "Offline", "Maintenance"]] = None,
    min_cpu: Optional[float] = None,
    sort_by: Literal ["cpu_usage", "ram_usage"] = "cpu_usage",
    order_desc: bool = False,
    offset: int = 0,
    limit: int = 10,
):
    assets_list = load_data()
    results = assets_list

    if hostname:
        results = [asset for asset in results if hostname.lower() in asset["hostname"].lower()]
    if status:
        results = [asset for asset in results if asset["status"] == status]
        logger.info(f"User is searching for {status} assets")
    if min_cpu:
        results = [asset for asset in results if min_cpu <= asset["cpu_usage"]]
    
    results = sorted(results, key=lambda asset: asset[sort_by], reverse=order_desc)
    if limit <= 0:
        raise HTTPException(status_code=400, detail="Limit must be greater than 0")
    else:
        results = results[offset:offset + limit]
    return results