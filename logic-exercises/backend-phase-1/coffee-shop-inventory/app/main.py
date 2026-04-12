import json
from uuid import UUID
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from app.schemas import Product

app = FastAPI()

main_path = Path(__file__).resolve().parent
json_file = main_path / "inventory.json"

def load_data():
    if not json_file.exists():
        with open(json_file, "w") as file:
            json.dump([], file)
    try:
        with open(json_file, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        return []

def save_data(inventory):
    try:
        compatible_data = jsonable_encoder(inventory)
        with open(json_file, "w") as file:
            json.dump(compatible_data, file, indent=4)
    except json.decoder.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Error saving: {e}")



# ------------ GET ------------
@app.get("/")
def home():
    return {"message": "here we go again"}

@app.get("/inventory/")
def get_inventory(out_of_stock: Optional[bool] = None):
    inventory = load_data()
    if out_of_stock is True:
        return [item for item in inventory if item["stock"] == 0]
    return inventory

@app.get("/inventory/{item_id}")
def get_item(item_id: UUID):
    inventory = load_data()
    for item in inventory:
        if str(item["id"]) == str(item_id):
            return item
    raise HTTPException(status_code=404, detail="Item not found")



# ------------ POST ------------
@app.post("/inventory")
def add_item(item: Product):
    inventory = load_data()
    new_data = item.model_dump()
    inventory.append(new_data)
    save_data(inventory)
    return new_data

# ------------ UPDATE ------------
@app.put("/inventory/{item_id}")
def update_item(item_id: UUID, update_data: Product):
    inventory = load_data()
    for item in inventory:
        if str(item["id"]) == str(item_id):
            new_data = update_data.model_dump()
            new_data["id"] = str(item_id)
            item.update(new_data)
            save_data(inventory)
            return item
    raise HTTPException(status_code=404, detail="Item not found")



# ------------ DELETE ------------
@app.delete("/inventory/{item_id}")
def delete_item(item_id: UUID):
    inventory = load_data()
    for item in inventory:
        if str(item["id"]) == str(item_id):
            inventory.remove(item)
            save_data(inventory)
            return {"message": f"Item '{item["name"]}' deleted"}
    raise HTTPException(status_code=404, detail="Item not found")