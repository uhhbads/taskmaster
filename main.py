from fastapi import FastAPI
from services import create_task_logic, _update_task, delete_task_logic, _list_task

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.post("/add/{task}")
async def create_task(task: str):
    return await create_task_logic(task)

@app.put("/update/{id}")
async def update_task_description(id: int, description: str):
    return await _update_task(id, new_task=description)

@app.put("/mark-in-progress/{id}")
async def mark_in_progress(id: int):
    return await _update_task(id, status="in-progress")

@app.put("/mark-done/{id}")
async def mark_done(id: int):
    return await _update_task(id, status="done")

@app.delete("/delete/{id}")
async def delete_task(id: int):
    return await delete_task_logic(id)

@app.get("/list")
async def list_task():
    return await _list_task(status=None)

@app.get("/list/{status}")
async def list_task_by_status(status: str):
    return await _list_task(status=status)