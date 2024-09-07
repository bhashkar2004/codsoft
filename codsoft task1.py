import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu options."""
    print("\nTo-Do List Application")
    print("======================")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Update a Task")
    print("4. Delete a Task")
    print("5. Exit")
    print("======================")

def view_tasks(tasks):
    """Displays all tasks in the to-do list."""
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Adds a new task to the to-do list."""
    task = input("\nEnter the task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")

def update_task(tasks):
    """Updates an existing task in the to-do list."""
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nEnter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_num - 1] = new_task
            print(f"Task {task_num} has been updated.")
        else:
            print("Invalid task number.")

def delete_task(tasks):
    """Deletes a task from the to-do list."""
    view_tasks(tasks)
    if tasks:
        task_num = int(input("\nEnter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")

def main():
    """Main function to run the To-Do List application."""
    tasks = []
    
    while True:
        clear_screen()
        display_menu()
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
