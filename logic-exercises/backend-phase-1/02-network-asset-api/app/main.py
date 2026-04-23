import os
import json
from uuid import UUID
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from app.schemas import NetworkAsset

app = FastAPI()
path = "app/assets.json"



def load_data():
    if not os.path.exists(path):
        with open(path, "w") as file:
            json.dump([], file)
    try:
        with open(path, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []



def save_data(data):
    try:
        compatible_data = jsonable_encoder(data)
        with open(path, "w") as file:
            json.dump(compatible_data, file, indent=4)
    except json.decoder.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error saving: {e}")


# ------------ GET ------------
@app.get("/")
async def root():
    return {"message": "This sucks"}

@app.get("/assets")
def get_assets():
    data = load_data()
    return data

@app.get("/assets/{asset_id}")
def get_asset(asset_id: UUID):
    data = load_data()
    for asset in data:
        if str(asset["id"]) == str(asset_id):
            return asset
    raise HTTPException(status_code=404, detail="Asset not found")



# ------------ POST ------------
@app.post("/assets")
def add_asset(asset: NetworkAsset):
    data = load_data()
    new_dict = asset.model_dump()
    data.append(new_dict)
    save_data(data)
    return new_dict



# ------------ UPDATE ------------
@app.put("/assets/{asset_id}")
def update_asset(asset_id: UUID, update_data: NetworkAsset):
    data = load_data()
    for asset in data:
        if str(asset["id"]) == str(asset_id):
            new_data = update_data.model_dump()
            new_data["id"] = str(asset_id)
            asset.update(new_data)
            save_data(data)
            return asset
    raise HTTPException(status_code=404, detail="Asset not found")



# ------------ DELETE ------------
@app.delete("/assets/{asset_id}")
def delete_asset(asset_id: UUID):
    data = load_data()
    for asset in data:
        if str(asset["id"]) == str(asset_id):
            print(f"Asset {asset['hostname']} deleted")
            data.remove(asset)
            save_data(data)
            return {"message": "Success"}
    raise HTTPException(status_code=404, detail="Asset not found")