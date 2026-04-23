from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from app.database import servers_db, users_db
from app.schemas import UserSchema, ServerCreate, ServerResponse, ServerUpdate

app = FastAPI()
print(servers_db)


# --- POST ---
@app.post("/servers/", response_model=ServerResponse)
def create_server(server: ServerCreate):
    updated_server_data = server.model_dump()
    updated_server_data["id"] = uuid4()
    servers_db.append(updated_server_data)
    return updated_server_data

@app.post("/users/")
def create_user(user: UserSchema):
    users_db.append(user)
    return {
        "mesagge": "User data received",
        "users_number": len(users_db),
        "last_user": user}



# --- GET ---
@app.get("/servers/")
def get_all_servers():
    return {"database": servers_db}

@app.get("/users/")
def get_all_users():
    return {"users": users_db}



# --- UPDATE ---
@app.put("/servers/{server_id}")
def update_server(server_id: UUID, server_update: ServerCreate):
    for index, server in enumerate(servers_db):
        if server["id"] == server_id:
            updated_server_data = server_update.model_dump()
            updated_server_data["id"] = server_id

            servers_db[index] = updated_server_data
            return updated_server_data

    raise HTTPException(status_code=404, detail="Server not found")

@app.patch("/servers/{server_id}", response_model=ServerResponse)
def patch_server(server_id: UUID, server_update: ServerUpdate):
    for index, server in enumerate(servers_db):
        if server["id"] == server_id:
            new_data = server_update.model_dump(exclude_unset=True)
            new_data = server | new_data
            servers_db[index] = new_data

            return new_data
    
    raise HTTPException(status_code=404, detail="Server not found")



# --- DELETE ---
@app.delete("/servers/{server_id}", response_model=ServerResponse)
def delete_server(server_id: UUID):
    for index, server in enumerate(servers_db):
        if server["id"] == server_id:
            delete_server = servers_db.pop(index)
            return delete_server
        
    raise HTTPException(status_code=404, detail="Server not found")