# Simple To-Do List (Task Manager)

tasks = []

while True:
    print("\n==============================")
    print("       TO-DO LIST MENU")
    print("==============================")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # View Tasks if user wants to view the tasks
    if choice == "1":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. [{status}] {task['name']}")

    # Add Task when user wants to add a task
    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")

    # Mark Task as Completed when user wants to mark a task as completed
    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. [{status}] {task['name']}")

            try:
                task_num = int(input("Enter task number to mark as completed: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Delete Task if user wants to delete a task
    elif choice == "4":
        if len(tasks) == 0:
            print("\nNo tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✔" if task["completed"] else "✘"
                print(f"{i}. [{status}] {task['name']}")

            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    deleted = tasks.pop(task_num - 1)
                    print(f"Deleted task: {deleted['name']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    # Exit
    elif choice == "5":
        print("\nThank you for using the To-Do List!")
        break
# invalid choice
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
        
