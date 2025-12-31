# Taskmaster

CLI-only small project using Python and FastAPI for
https://roadmap.sh/projects/task-tracker

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

Install the package with:
```bash
pip install -e .
```

### Command Line Interface (CLI)

Run commands using the following format:
```bash
taskmaster  [arguments]
```

#### Add a New Task
```bash
taskmaster add "Buy groceries"
taskmaster add "Complete project documentation"
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
taskmaster update 1 "Buy groceries and cook dinner"
```

#### Mark Task as In Progress
```bash
taskmaster mark-in-progress 1
```

#### Mark Task as Done
```bash
taskmaster mark-done 1
```

#### Delete a Task
```bash
taskmaster delete 1
```

#### List All Tasks
```bash
taskmaster list
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
taskmaster list done

# List tasks in progress
taskmaster list in-progress

# List pending tasks
taskmaster list todo
```

### FastAPI
I was just practicing ok