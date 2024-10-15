import os

# List to store tasks
todo_list = []


def add_task(task):
    """Add a new task to the to-do list."""
    todo_list.append(task)
    print(f"Added task: {task}")


def remove_task(index):
    """Remove a task by its index."""
    try:
        index = int(index) - 1  # Convert input to 0-based index
        if 0 <= index < len(todo_list):
            removed_task = todo_list.pop(index)
            print(f"Removed task: {removed_task}")
        else:
            print("Invalid index.")
    except ValueError:
        print("Please enter a valid number.")


def view_tasks():
    """View all tasks in the to-do list."""
    if todo_list:
        print("\nTo-Do List:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")
    else:
        print("\nYour to-do list is empty.")


def save_tasks_to_file():
    """Save tasks to a file."""
    with open("tasks.txt", "w") as file:
        for task in todo_list:
            file.write(task + "\n")
    print("Tasks saved to tasks.txt.")


def load_tasks_from_file():
    """Load tasks from a file at the start of the program."""
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                todo_list.append(line.strip())
        print("Tasks loaded from tasks.txt.")
    else:
        print("No previous tasks found.")


def main():
    """Main function to interact with the user."""
    load_tasks_from_file()

    while True:
        print("\nTo-Do List Manager")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task by index")
        print("4. Save and exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            task = input("Enter a task to add: ")
            add_task(task)
        elif choice == "3":
            view_tasks()  # Show the tasks so the user knows the index
            index = input("Enter the index of the task to remove: ")
            remove_task(index)
        elif choice == "4":
            save_tasks_to_file()
            print("Tasks saved. Exiting.")
            break
        else:
            print("Invalid choice, please try again.")


# this block to ensure the script only runs when executed directly
if __name__ == "__main__":
    main()
