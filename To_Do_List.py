import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added!")

    def view_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task['description']} - Due: {task['due_date']} - Priority: {task['priority']} - Status: {task['status']}")

    def update_task(self, task_id, **updates):
        if 0 <= task_id < len(self.tasks):
            self.tasks[task_id].update(updates)
            print("Task updated!")
        else:
            print("Invalid Task ID")

    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):
            del self.tasks[task_id]
            print("Task deleted!")
        else:
            print("Invalid Task ID")

    def save_tasks(self, filename="tasks.json"):
        with open(filename, "w") as file:
            json.dump(self.tasks, file)
            print("Tasks saved to file.")

    def load_tasks(self, filename="tasks.json"):
        try:
            with open(filename, "r") as file:
                self.tasks = json.load(file)
                print("Tasks loaded from file.")
        except FileNotFoundError:
            print("No saved tasks found.")

if __name__ == "__main__":
    todo = ToDoList()
    todo.load_tasks()

    while True:
        command = input("Enter command (add, view, update, delete, save, exit): ").lower()
        if command == "add":
            description = input("Task description: ")
            due_date = input("Due date (YYYY-MM-DD): ")
            priority = input("Priority (low, medium, high): ")
            todo.add_task({"description": description, "due_date": due_date, "priority": priority, "status": "incomplete"})
        elif command == "view":
            todo.view_tasks()
        elif command == "update":
            task_id = int(input("Task ID to update: ")) - 1
            updates = {}
            description = input("New description (leave blank to keep current): ")
            if description:
                updates["description"] = description
            due_date = input("New due date (leave blank to keep current): ")
            if due_date:
                updates["due_date"] = due_date
            priority = input("New priority (leave blank to keep current): ")
            if priority:
                updates["priority"] = priority
            status = input("New status (leave blank to keep current): ")
            if status:
                updates["status"] = status
            todo.update_task(task_id, **updates)
        elif command == "delete":
            task_id = int(input("Task ID to delete: ")) - 1
            todo.delete_task(task_id)
        elif command == "save":
            todo.save_tasks()
        elif command == "exit":
            todo.save_tasks()
            break
