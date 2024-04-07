import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks):
                status = " [x]" if task["completed"] else " [ ]"
                print(f"{i+1}. {task['task']}{status}")
        else:
            print("No tasks found.")

if __name__ == "__main__":
    task_manager = TaskManager()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            task = input("Enter task: ")
            task_manager.add_task(task)
        elif choice == '2':
            index = int(input("Enter index of task to mark as complete: ")) - 1
            task_manager.complete_task(index)
        elif choice == '3':
            index = int(input("Enter index of task to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == '4':
            task_manager.view_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
