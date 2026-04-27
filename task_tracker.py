class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        priority = input("Enter Priority (High/Medium/Low): ").capitalize()
        if priority not in ["High", "Medium", "Low"]:
            print("Invalid priority! Setting to Low.")
            priority = "Low"
        task = {
            "title": title,
            "description": description,
            "priority": priority
        }
        self.tasks.append(task)
        print("Task added successfully!")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!")
            return
        print("Your Tasks:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']} [{task['priority']} Priority]")
        print()
    def delete_task(self):
        if not self.tasks:
            print("No tasks to delete!")
            return
        self.view_tasks()
        try:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(self.tasks):
                del self.tasks[num - 1]
                print("Task deleted successfully!")
            else:
                print("Invalid number!")
        except:
            print("Please enter a valid number!")
    def update_priority(self):
        if not self.tasks:
            print("No tasks available!")
            return
        self.view_tasks()
        try:
            num = int(input("Enter task number to update priority: "))
            if 1 <= num <= len(self.tasks):
                new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()

                if new_priority in ["High", "Medium", "Low"]:
                    self.tasks[num - 1]["priority"] = new_priority
                    print("Task priority updated successfully!")
                else:
                    print("Invalid priority!")
            else:
                print("Invalid number!")
        except:
            print("Please enter a valid number!")
    def run(self):
        while True:
            print("===== Task Tracker =====")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Update Task Priority")
            print("5. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.update_priority()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
task_manager = TaskManager()
task_manager.run()