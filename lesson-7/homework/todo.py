import json

class Task:
    def __init__(self, task_id, title, description, due_date, status):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status
        }

class ToDoManager:
    FILE_NAME = "tasks.json"

    @staticmethod
    def load_tasks():
        try:
            with open(ToDoManager.FILE_NAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @staticmethod
    def save_tasks(tasks):
        with open(ToDoManager.FILE_NAME, "w") as file:
            json.dump(tasks, file, indent=4)

    @staticmethod
    def add_task(task):
        tasks = ToDoManager.load_tasks()
        tasks.append(task.to_dict())
        ToDoManager.save_tasks(tasks)
        print("Task added successfully!")

    @staticmethod
    def view_tasks():
        tasks = ToDoManager.load_tasks()
        for task in tasks:
            print(task)

# Example Usage
task1 = Task(102, "Chores", "Wash the dishes", "2025-03-03", "Pending")
ToDoManager.add_task(task1)
ToDoManager.view_tasks()