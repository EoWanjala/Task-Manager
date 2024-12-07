import json

<<<<<<< HEAD
TASKS_FILE = "tasks.json"
=======
TASKS_FILE = "tasks.json"
>>>>>>> feature/delete-tasks

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(name, description):
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"name": name, "description": description})
    save_tasks(tasks)
    print(f"Task '{name}' added.")

if __name__ == "__main__":
    task_name = input("Enter task name: ")
    task_description = input("Enter task description: ")
    add_task(task_name, task_description)

