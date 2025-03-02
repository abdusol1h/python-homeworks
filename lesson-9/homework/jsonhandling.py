import json
import csv

# Load tasks from JSON
def load_tasks(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# Display tasks
def display_tasks(tasks):
    for task in tasks:
        print(f"ID: {task['id']}, Task: {task['task']}, Completed: {task['completed']}, Priority: {task['priority']}")

# Save tasks to JSON
def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

# Calculate task statistics
def task_statistics(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    avg_priority = sum(task["priority"] for task in tasks) / total if total else 0

    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Average priority: {avg_priority:.2f}")

# Convert JSON data to CSV
def json_to_csv(tasks, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Task", "Completed", "Priority"])
        for task in tasks:
            writer.writerow([task["id"], task["task"], task["completed"], task["priority"]])

# Execution
tasks = load_tasks('tasks.json')
display_tasks(tasks)
task_statistics(tasks)
json_to_csv(tasks, 'tasks.csv')
print("Tasks saved to 'tasks.csv'.")