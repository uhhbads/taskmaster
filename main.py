from fastapi import FastAPI
from datetime import datetime
import os
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/create/{task}")
async def create_task(task: str):
    try:
        with open("data.json", "r+") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        datafile = []

    existing_ids = {x["id"] for x in datafile}
    new_id = 1
    while new_id in existing_ids:
        new_id += 1

    data = {
            "id": new_id,
            "description": task,
            "status": "todo",
            "createdAt": datetime.today(),
            "updatedAt": datetime.today()
            }

    datafile.append(data)

    with open("data.json", "w") as jsondata:
        json.dump(sorted(datafile, key=lambda x:x["id"]), jsondata, default=str, indent=4)

    return data

@app.put("/update/{id}/{new_task}")
async def update_task(id: int, new_task: str):
    try:
        with open("data.json", "r+") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        print("Create a task first!")

    task_to_update = None
    for task in datafile:
        if task["id"] == id:
            task_to_update = task
            break

    if task_to_update is None:
        return "No task found."

    task_to_update["description"] = new_task
    task_to_update["updatedAt"] = datetime.today()

    with open("data.json", "w") as jsondata:
        json.dump(sorted(datafile, key=lambda x: x["id"]), jsondata, default=str, indent=4)

    print(f"Task with ID:{id} Updated.")
    return f"Updated task #{id}"

@app.delete("/delete/{id}")
async def delete_task(id: int):
    try:
        with open("data.json", "r+") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        print("Create a task first!")

    original_length = len(datafile)
    updated_data = [task for task in datafile if task["id"] != id] 

    if len(updated_data) == original_length:
        return f"ID: {id} not found."

    with open("data.json", "w") as jsondata:
        json.dump(updated_data, jsondata, default=str, indent=4)

    print(f"Task with ID:{id} deleted.")
    return f"Deleted task #{id}"