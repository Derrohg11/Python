#Create an empty list to store the tasks and their status
todo_list = []

#function to Add a New Task
def add_task():
    task = input("Enter a task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New task added successfully!\n")

#Function to view all tasks
def view_tasks():
    print("Your Todo list: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
            print("\n")

#Function to remoove a task
def remove_task():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter the task number you want to remove")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task}")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

#Function to mark a task as completed
def mark_done():
    if len(todo_list) == 0:
        print("List is empty!")
    else:
        try:
            search_index = int(input("Enter the task number you want to mark as completed: ")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]["Status"] = "completed"
                print(f"Task marked as completed: {todo_list[search_index]}")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

#Function to display a menu
def menu():
    while True:
        print("***Main Menu***")
        print("1. Add a new task.")
        print("2. View all tasks.")
        print("3. Remove a task.")
        print("4. mark a task as completed.")
        print("5. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
             remove_task()
        elif choice == "4":
             mark_done()
        elif choice == "5":
            print("exiting application...")
            exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
            