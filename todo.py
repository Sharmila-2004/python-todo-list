FILE_NAME = "tasks.txt"

def add_task():
    task = input("Enter new task: ")
    with open(FILE_NAME, "a") as file:
        file.write(task + "\n")
    print("✅ Task added successfully!\n")

def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("⚠ No tasks found.\n")
                return

            print("\n📋 Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
            print()
    except FileNotFoundError:
        print("⚠ No task file found.\n")

def delete_task():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("⚠ No tasks to delete.\n")
            return

        view_tasks()
        task_no = int(input("Enter task number to delete: "))

        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            with open(FILE_NAME, "w") as file:
                file.writelines(tasks)
            print(f"🗑 Removed: {removed.strip()}\n")
        else:
            print("❌ Invalid task number\n")

    except (FileNotFoundError, ValueError):
        print("❌ Error deleting task\n")

while True:
    print("---- TO-DO LIST ----")
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
        print("👋 Exiting To-Do List")
        break
    else:
        print("⚠ Invalid choice\n")