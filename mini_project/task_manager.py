tasks = []
while(True):
    print("====== TASK MANAGER ======")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    user = int(input("Enter your choice: "))
    if user == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif user == 2:
        print("\nYour Tasks:")
        if not tasks:
            print("There are no tasks.")
        else : 

            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
    elif user == 3:
        print("Delete your tasks")

        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")
        print("Task deleted successfully!")

        s = int(input("Enter task number to delete: "))

        print(f"Task deleted: {tasks[s - 1]}")

        tasks.pop(s - 1)
    

    elif user == 4 :
        print("Thank you for using Task Manager!")
        break
    else :
        print("choose right one")