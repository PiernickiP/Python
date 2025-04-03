import os

def load_tasks(filename = "tasks.txt"):
    if not os.path.exists(filename):
        return []
    
    tasks = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            parts = line.split('||')

            description = parts[0]

            if len(parts) > 1:
                status_str = parts[1].strip()
            else:
                status_str = 'False'
            
            status = True if status_str.lower() == 'true' else False

            tasks.append({
                'description': description,
                'status': status
            })
    
    return tasks

def save_task(tasks, filename = 'tasks.txt'):
    with open(filename, 'w', encoding= 'utf-8') as file:
        for task in tasks:
            description = task.get('description', '')
            status = task.get('status', False)
            
            status_str = "True" if status else "False"
            file.write(f"{description}||{status_str}\n")

def show_menu():
    print("1. Add task")
    print("2. Show list of tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def add_task(tasks):
    description = input("Enter task description: ")
    new_task = {
        'description': description,
        'status': False
    }

    tasks.append(new_task)
    save_task(tasks)

    print(f"Task '{description}' added.")

def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            status = "Done" if task['status'] else "Not done"
            print(f"{index + 1}. {task['description']} - {status}")

def mark_task_done(tasks):
    show_tasks(tasks)
    index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]['status'] = True
        save_task(tasks)
        print(f"Task '{tasks[index]['description']}' marked as done.")
    else:
        print("Invalid task number.")

def remove_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter the task number to remove: ")) - 1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_task(tasks)
        print(f"Task '{removed_task['description']}' removed.")
    else:
        print("Invalid task number.")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task(tasks)
    elif choice == '2':
        show_tasks(tasks)
    elif choice == '3':
        mark_task_done(tasks)
    elif choice == '4':
        remove_task(tasks)
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")