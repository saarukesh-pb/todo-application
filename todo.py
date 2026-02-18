# todo_app.py

tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("✅ Task added successfully!\n")


def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    
    print("\n📋 Your Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def delete_task():
    view_tasks()
    if tasks:
        try:
            choice = int(input("Enter task number to delete: "))
            removed = tasks.pop(choice - 1)
            print(f"❌ Task '{removed}' deleted successfully!\n")
        except:
            print("Invalid choice!\n")


def main():
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting To-Do App...")
            break
        else:
            print("Invalid option! Try again.\n")


if __name__ == "__main__":
    main()
