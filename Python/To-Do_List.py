# To Do List using Python

List = []

Exit = False
while not Exit:
    print("To-Do List")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task: ")
        List.append(task)
        print(f"Task '{task}' added to the list.")
    elif choice == '2':
        if List == []:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for i in range(len(List)):
                print(List[i])
    elif choice == '3':
        if not List:
            print("No tasks to remove.")
        else:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(List):
                removed_task = List.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
    elif choice == '4':
        Exit = True
        print("Exiting To-Do List.")
    else:
        print("Invalid choice. Please try again.")