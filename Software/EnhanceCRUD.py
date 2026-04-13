import json
import os
from datetime import datetime

FILENAME = "EnhanceCRUD.json"


# ------------------ Task Class ------------------

class Task:
    def __init__(self, task_id, title, description, priority, due_date, status="Pending"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.status = status

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "status": self.status
        }


# ------------------ File Handling ------------------

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ------------------ Utility ------------------

def generate_task_id(tasks):
    if not tasks:
        return 1
    return max(task["task_id"] for task in tasks) + 1


def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n----- Task List -----")
    for task in tasks:
        print(f"""
ID: {task['task_id']}
Title: {task['title']}
Description: {task['description']}
Priority: {task['priority']}
Due Date: {task['due_date']}
Status: {task['status']}
---------------------------""")


# ------------------ CRUD Operations ------------------

def add_task(tasks):
    task_id = generate_task_id(tasks)
    title = input("Enter task title: ")
    description = input("Enter description: ")
    priority = input("Enter priority (High/Medium/Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    new_task = Task(task_id, title, description, priority, due_date)
    tasks.append(new_task.to_dict())
    save_tasks(tasks)

    print("Task added successfully!")


def update_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter Task ID to update: "))

    for task in tasks:
        if task["task_id"] == task_id:
            task["title"] = input("Enter new title: ")
            task["description"] = input("Enter new description: ")
            task["priority"] = input("Enter new priority: ")
            task["due_date"] = input("Enter new due date: ")
            task["status"] = input("Enter new status: ")
            save_tasks(tasks)
            print("Task updated successfully!")
            return

    print("Task not found.")


def delete_task(tasks):
    display_tasks(tasks)
    task_id = int(input("Enter Task ID to delete: "))

    for task in tasks:
        if task["task_id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted successfully!")
            return

    print("Task not found.")


def search_task(tasks):
    keyword = input("Enter keyword to search: ").lower()
    results = [task for task in tasks if keyword in task["title"].lower()]

    if results:
        display_tasks(results)
    else:
        print("No matching tasks found.")


def filter_by_status(tasks):
    status = input("Enter status to filter (Pending/Completed): ")
    filtered = [task for task in tasks if task["status"] == status]

    if filtered:
        display_tasks(filtered)
    else:
        print("No tasks with that status.")


# ------------------ Main Program ------------------

def main():
    tasks = load_tasks()

    while True:
        print("""
======== Smart Task & Productivity Manager ========
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Search Task
6. Filter by Status
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            search_task(tasks)
        elif choice == "6":
            filter_by_status(tasks)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
