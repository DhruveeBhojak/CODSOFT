import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task["status"] == "complete" else "❌"
        print(f"{i}. {task['task']} (Due: {task['due_date']}) [{status}]")


def add_task(tasks):
    task = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"task": task, "due_date": due_date, "status": "pending"})
    print("Task added successfully!")


def mark_complete(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as complete: ")) - 1
        tasks[index]["status"] = "complete"
        print("Task marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number.")


def delete_task(tasks):
    display_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        deleted = tasks.pop(index)
        print(f"Deleted task: {deleted['task']}")
    except (IndexError, ValueError):
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
