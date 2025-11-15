tasks = []

while True:
    print("\n--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
            try:
                task_num = int(input("Enter task number to remove: "))
                if 0 < task_num <= len(tasks):
                    tasks.pop(task_num - 1)
                    print("Task removed.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")


