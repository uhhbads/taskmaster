# Taskmaster

CLI-only small project using Python and FastAPI

## Features

- ✅ Add new tasks
- ✅ Update task descriptions
- ✅ Delete tasks
- ✅ Mark tasks as in-progress or done
- ✅ List all tasks
- ✅ Filter tasks by status (todo, in-progress, done)
- ✅ REST API support via FastAPI

## Project Structure
```
taskmaster/
├── main.py          # FastAPI routes (API endpoints)
├── services.py      # Business logic
├── cli.py           # Command-line interface
├── data.json        # Task storage (auto-generated)
└── README.md        # This file
```

## Usage

### Command Line Interface (CLI)

Run commands using the following format:
```bash
python cli.py  [arguments]
```

#### Add a New Task
```bash
python cli.py add "Buy groceries"
python cli.py add "Complete project documentation"
```

**Output:**
```json
{
  "success": true,
  "message": "Task created successfully",
  "data": {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo",
    "createdAt": "2024-01-15#14:30",
    "updatedAt": "2024-01-15#14:30"
  }
}
```

#### Update a Task
```bash
python cli.py update 1 "Buy groceries and cook dinner"
```

#### Mark Task as In Progress
```bash
python cli.py mark-in-progress 1
```

#### Mark Task as Done
```bash
python cli.py mark-done 1
```

#### Delete a Task
```bash
python cli.py delete 1
```

#### List All Tasks
```bash
python cli.py list
```

**Output:**
```json
{
  "success": true,
  "data": [
    {"id": 1, "description": "Buy groceries"},
    {"id": 2, "description": "Complete documentation"}
  ]
}
```

#### List Tasks by Status
```bash
# List only completed tasks
python cli.py list done

# List tasks in progress
python cli.py list in-progress

# List pending tasks
python cli.py list todo
```

### FastAPI
I was just practicing ok