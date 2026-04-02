def findTask(tasks, name):
    for task in tasks:
        if task["task"] == name:
            return task
    return None


def addTask(tasks):
    taskName = input("Add a new task: ").strip().lower()
    time = input("Enter time (HH:MM): ").strip()

    if findTask(tasks, taskName):
        print("\nTask already added.")
        return

    tasks.append({"task": taskName, "time": time})
    print("\nTask successfully added.")


def removeSingleTask(tasks):
    taskName = input("Enter the task to be deleted: ").strip().lower()

    task = findTask(tasks, taskName)

    if task:
        tasks.remove(task)
        print("\nTask successfully removed.")
    else:
        print("\nTask does not exist.")


def removeTask(tasks):
    if not tasks:
        print("To-Do-List is empty")
        return
    if len(tasks) == 1:
        removeSingleTask(tasks)
        return

    print(
        """Press
1 ==> Remove one task
2 ==> Remove all tasks"""
    )

    option = int(input("Option: "))

    if option == 1:
        removeSingleTask(tasks)

    elif option == 2:
        tasks.clear()
        print("\nAll tasks removed.")

    else:
        print("Invalid option!!!\n")


def viewTask(tasks):
    if not tasks:
        print("To-Do-List is empty")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}) {task['task'].capitalize()} at {task['time']}")


def main():
    tasks = []

    print("********* Welcome to the ABC Task App *********")

    while True:
        print(
            """\nPress
1 ==> Add a task
2 ==> Remove a task
3 ==> View all tasks
4 ==> Exit"""
        )

        option = int(input("Option: "))

        if option == 1:
            addTask(tasks)

        elif option == 2:
            removeTask(tasks)

        elif option == 3:
            viewTask(tasks)

        elif option == 4:
            print("Bye 👋🏻")
            break

        else:
            print("Invalid option!!!\n")


main()