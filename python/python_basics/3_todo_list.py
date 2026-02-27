# ***************** Add a Task ***************** 
def addTask(tasks):
    task_name = input("Add a new task: ").strip().lower()
    time = input("Enter time (HH:MM): ").strip()

    for task in tasks:
        if task["task"] == task_name:
            print("\nTask already added.")
            return

    tasks.append({"task": task_name, "time": time})
    print("\nTask successfully added to your to-do-list.")


# ***************** Remove a Task(s) ***************** 
def removeTask(tasks):
    if len(tasks) == 0:
        print("To-Do-List is empty")
        return

    print(
        """Press
          1 ==> Remove one task
          2 ==> Remove all tasks"""
    )
    option = int(input("Option: "))

    if option == 1:
        task_name = input("Enter the task to be deleted: ").strip().lower()

        for task in tasks:
            if task["task"] == task_name:
                tasks.remove(task)
                print("\nTask successfully removed from to-do-list.")
                return

        print("\nTask does not exist so it cannot be deleted.")

    elif option == 2:
        tasks.clear()
        print("\nAll tasks successfully removed. The list is now empty.")
    else:
        print("Invalid option!!!\n")


# ***************** View all Task(s) ***************** 
def viewTask(tasks):
    if len(tasks) == 0:
        print("To-Do-List is empty")
        return
    else:
        print("Your Tasks are listed below:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}) {task["task"].capitalize()} at {task["time"]}")


print("********* Welcome to the ABC Task App *********")
tasks = []
while True:
    print(
        """Press
          1 ==> To add a task
          2 ==> To remove a task
          3 ==> To view all your tasks
          4 ==> Exit"""
    )
    option = int(input("Option: "))
    print()
    if option == 1:
        addTask(tasks)
        print()
    elif option == 2:
        removeTask(tasks)
        print()
    elif option == 3:
        viewTask(tasks)
        print()
    elif option == 4:
        print("Bye 👋🏻")
        break
    else:
        print("Invalid option!!!\n")
        continue
