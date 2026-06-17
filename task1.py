def display_tasks(task_list):
    """
    VIEW: Handles the User Interface (UI).
    Iteration creates a temporary view of the system's state.
    """
    print("\n--- Current To-Do List ---")
    if not task_list:
        print("Memory empty. No tasks to display.")
    else:
        # Using enumerate() for professional polish instead of range(len())
        for index, task_data in enumerate(task_list):
            print(f"Index [{index}] | ID: {task_data['id']} | Task: {task_data['task']}")
    print("--------------------------\n")

def add_task(task_list, task_description, current_id):
    """
    MODEL/PROCESS: Handles the data logic and modification.
    Uses a dictionary to define a task, simulating a SQL table row.
    """
    # Dictionary -> Table Row
    new_task = {
        "id": current_id,
        "task": task_description
    }
    
    # Appending to the dynamic array (Amortized O(1) efficiency)
    task_list.append(new_task)
    print(f"[+] Success: '{task_description}' added to memory.")
    
    return current_id + 1

def main():
    """
    STORAGE/GATEKEEPER: The main execution environment.
    """
    # The Volatile Container (Data will be lost if process terminates)
    my_tasks = []
    task_id_counter = 1
    
    print("Initialization Complete: DecodeLabs Task Manager Running")
    
    while True:
        print("\nMain Menu:")
        print("1. View Tasks (Output)")
        print("2. Add Task (Input)")
        print("3. Terminate Process")
        
        choice = input("Enter command (1/2/3): ")
        
        if choice == '1':
            display_tasks(my_tasks)
            
        elif choice == '2':
            print("\n(Hint: Enter tasks like 'Finalize Collabin PR' or 'Check Khaam.essentials anti-hair fall shampoo inventory')")
            new_desc = input("Enter the task description: ")
            
            # Process the input and update the ID counter
            task_id_counter = add_task(my_tasks, new_desc, task_id_counter)
            
        elif choice == '3':
            print("Terminating process. Warning: RAM is volatile. All data lost.")
            break
            
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# PROJECT 1 GATEKEEPER
if __name__ == "__main__":
    main()