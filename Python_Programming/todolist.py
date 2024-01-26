from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None):
        self.tasks.append({"TASK": task, "DUE_DATE": due_date, "COMPLETED": False})
        print(f'TASK "{task}" ADDED')

    def view_tasks(self):
        print("--- TASKS ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "DONE" if task["COMPLETED"] else "PENDING"
            due_date_info = f'DUE: {task["DUE_DATE"]}' if task["DUE_DATE"] else ''
            print(f"{index}. {task['TASK']} - {status} {due_date_info}")

    def mark_completed(self, task_index):
        try:
            task_index = int(task_index) - 1
            self.tasks[task_index]["COMPLETED"] = True
            self.tasks[task_index]["COMPLETION_DATE"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f'TASK "{self.tasks[task_index]["TASK"]}" marked as completed')
        except (ValueError, IndexError):
            print("INVALID TASK NUMBER")

    def remove_task(self, task_index):
        try:
            task_index = int(task_index) - 1
            removed_task = self.tasks.pop(task_index)
            print(f'TASK "{removed_task["TASK"]}" REMOVED')
        except (ValueError, IndexError):
            print("INVALID TASK NUMBER")

# Example usage with user input
todo_list = TodoList()

while True:
    print("\n==== TO-DO LIST ====")
    print("1) Add Task")
    print("2) View Tasks")
    print("3) Mark Task as Completed")
    print("4) Remove Task")
    print("5) Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("Enter the task: ")
        due_date_str = input("Enter the due date [ Format: YYYY-MM-DD HH:MM or Optional ]: ")
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d %H:%M") if due_date_str else None
        todo_list.add_task(task, due_date)
    elif choice == "2":
        todo_list.view_tasks()
    elif choice == "3":
        task_index = input("Enter the task number to mark as completed: ")
        todo_list.mark_completed(task_index)
    elif choice == "4":
        task_index = input("Enter the task number to remove: ")
        todo_list.remove_task(task_index)
    elif choice == "5":
        break
    else:
        print("Invalid Choice")
