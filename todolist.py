class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task_id, task_name):
        self.tasks[task_id] = {'name': task_name, 'status': 'not started'}
        print(f"Task '{task_name}' added successfully")

    def view_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty")
        else:
            print("Your to-do list:")
            for task_id, task in self.tasks.items():
                print(f"Task ID: {task_id}, Task Name: {task['name']}, Status: {task['status']}")

    def update_task_status(self, task_id, status):
        if task_id in self.tasks:
            self.tasks[task_id]['status'] = status
            print(f"Task '{self.tasks[task_id]['name']}' status updated to '{status}'!")
        else:
            print("Task not found")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task with ID {task_id} deleted successfully")
        else:
            print("Task not found")


def main():
    todo = ToDoList()

    while True:
        print("\nWelcome to Your To-Do List")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task's status")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Choose what you do: ")

        if choice == '1':
            task_id = input("Enter a unique task ID: ")
            task_name = input("Enter the task name: ")
            todo.add_task(task_id, task_name)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            task_id = input("Enter the task ID: ")
            status = input("Enter the new status 'in progress', 'completed': ")
            todo.update_task_status(task_id, status)
        elif choice == '4':
            task_id = input("Enter the task ID: ")
            todo.delete_task(task_id)
        elif choice == '5':
            break
        else:
            print("Sorry, that's not a valid option. try again")


if __name__ == "__main__":
    main()