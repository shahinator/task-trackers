class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        task = {
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        print("Task added successfully!\n")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!\n")
            return
        print("\nTasks List:")
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{i}. {task['title']} - {task['description']} [{status}]")
        print()
    def delete_task(self):
        if not self.tasks:
            print("There is no task for deleting.\n")
            return
        self.view_tasks()
        try:
            num = int(input("Enter task number for deleting: "))
            if 1 <= num <= len(self.tasks):
                self.tasks.pop(num - 1)
                print("Task deleted successfully!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")
    def mark_completed(self):
        if not self.tasks:
            print("No tasks available to mark as completed.\n")
            return
        self.view_tasks()
        try:
            num = int(input("Enter task number to mark as completed: "))
            if 1 <= num <= len(self.tasks):
                self.tasks[num - 1]["completed"] = True
                print("Task marked as completed!\n")
            else:
                print("Invalid task number!\n")
        except ValueError:
            print("Please enter a valid number!\n")
    def run(self):
        while True:
            print("===== Task Tracker =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Mark Task as Completed")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.mark_completed()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!\n")
task_manager = TaskManager()
task_manager.run()