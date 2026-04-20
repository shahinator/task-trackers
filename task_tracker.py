class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self):
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        task = {
            "title": title,
            "description": description
        }
        self.tasks.append(task)
        print("Added Task")
    def view_tasks(self):
        if not self.tasks:
            print("No tasks found!\n")
            return
        print("Tasks List:")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task['title']} - {task['description']}")
    def delete_task(self):
        if not self.tasks:
            print("There is no Task for Deleting")
            return
        self.view_tasks()
        try:
            num = int(input("Enter task number for deleting: "))
            if 1 <= num <= len(self.tasks):
                del self.tasks[num - 1]
                print("Delete successfully")
            else:
                print("Your Number Is Invalid")
        except:
            print("Please enter a valid number")
    def run(self):
        while True:
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice!\n")
task_manager = TaskManager()
task_manager.run()