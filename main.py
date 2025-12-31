from fastapi import FastAPI
from datetime import datetime
import os
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/add/{task}")
async def create_task(task: str):
    if not task or task.strip() == "":
        return {"success": False,
                "error": "Enter a proper task."
                }
    
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
            "createdAt": datetime.now().isoformat("#", "minutes"),
            "updatedAt": datetime.now().isoformat("#", "minutes")
            }

    datafile.append(data)

    with open("data.json", "w") as jsondata:
        json.dump(sorted(datafile, key=lambda x:x["id"]), jsondata, indent=4)

    return {
            "success": True,
            "message": "Task created successfully",
            "data": data
            }

@app.put("/update/{id}")
async def update_task_description(id: int, description: str):
    return await _update_task(id, new_task=description)

@app.put("/mark-in-progress/{id}")
async def mark_in_progress(id: int):
    return await _update_task(id, status="in-progress")

@app.put("/mark-done/{id}")
async def mark_done(id: int):
    return await _update_task(id, status="done")

async def _update_task(id: int, new_task: str = None, status: str = None):
    try:
        with open("data.json", "r") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        return {
                "success": False,
                "error": "Create a task first!"
                }

    task_to_update = None
    for task in datafile:
        if task["id"] == id:
            task_to_update = task
            break

    if task_to_update is None:
        return {
                "success": False,
                "error": "No task found."
                }

    # update only the fields that were provided
    if new_task is not None:
        if not new_task or new_task.strip() == "":
            return {
                    "success": False,
                    "error": "Enter a proper task."
                    }
        
        task_to_update["description"] = new_task
    
    if status is not None:
        valid_statuses = ["todo", "in-progress", "done"]
        if status not in valid_statuses:
            return {
                    "success": False,
                    "error": f"{status} is an invalid status."
                    }
        task_to_update["status"] = status

    task_to_update["updatedAt"] = datetime.now().isoformat("#", "minutes")

    with open("data.json", "w") as jsondata:
        json.dump(sorted(datafile, key=lambda x: x["id"]), jsondata, indent=4)

    return {
            "success": True,
            "message": f"Task {id} updated successfully", 
            "updated_task": task_to_update
            }

@app.delete("/delete/{id}")
async def delete_task(id: int):
    try:
        with open("data.json", "r+") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        return {
                "success": False,
                "error": "Create a task first!"
                }

    original_length = len(datafile)
    updated_data = [task for task in datafile if task["id"] != id] 

    if len(updated_data) == original_length:
        return {
                "success": False,
                "error": f"ID: {id} not found."
                }

    with open("data.json", "w") as jsondata:
        json.dump(updated_data, jsondata, indent=4)

    return {
            "success": True,
            "message": f"Deleted task #{id}"
            }

@app.get("/list")
async def list_task():
    return await _list_task(status=None)

@app.get("/list/{status}")
async def list_task_by_status(status: str):
    return await _list_task(status)

async def _list_task(status: str = None):
    try:
        with open("data.json", "r") as jsondata:
            datafile = json.load(jsondata)
    except FileNotFoundError:
        return {
                "success": False,
                "error": "Create a task first!"
                }

    if status is None:
        return {
                "success": True,
                "data": [{"id": task["id"], "description": task["description"]} for task in datafile]
                }
    
    valid_statuses = ["done", "todo", "in-progress"]
    if status not in valid_statuses:
        return {
                "success": False,
                "error": f"{status} is an invalid status."
                }    

    filtered = [{"id": task["id"], "description": task["description"]} for task in datafile if task["status"] == status]

    return {
            "success": True,
            "data": filtered
            }