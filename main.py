import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f"Added task: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = '✔' if task['completed'] else '✘'
        print(f"{idx}. [{status}] {task['task']}")

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}")
    else:
        print("Invalid task number.")

def mark_task_completed(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks(tasks)
        print(f"Marked task as completed: {tasks[task_number - 1]['task']}")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(task_number)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
