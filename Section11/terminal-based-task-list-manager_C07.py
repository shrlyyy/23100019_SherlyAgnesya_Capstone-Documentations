'''
Challenge 07: Terminal-Based Task List Manager

Create a Python script that lets users manage a to-do list directly from the terminal.

Your program should:
1. Allow users to:
    - Add a task.
    - View all tasks.
    - Mark a task as completed.
    - Delete a task.
    - Exit the app.
2. Save all tasks in a text file named 'tasks.txt' so data persists between runs.
3. Display tasks with an index number and a ✅ if completed.

Example menu:
1. Add Task.
2. View Tasks.
3. Mark Task as Completed.
4. Delete Task.
5. Exit.

Example output:
Your Tasks:

Buy groceries || not_done
Finish Python project || done
Read a book || not_done

Bonus:
- Prevent empty tasks from being added.
- Validate task numbers before completing/deleting.
'''

import os # Operating System di-Python untuk cek file sudah ada atau belum.

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if(os.path.exists(TASK_FILE)): # Agar program tidak error kalau file belum ada.
        with open(TASK_FILE, 'r', encoding="utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1) # rsplit (1) untuk memecah string jadi 2 bagian (1 itu maksudnya pecahnya satu aja, jadinya dia ada 2 bagian). 
                tasks.append({"text": text, "done": status == "done"}) # Mengubah string "done" jadi nilai Boolean.
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, 'w', encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not_done"
            f.write(f"{task['text']} || {status}\n")

def display_tasks(tasks):
    if not tasks:
        print(f"No tasks found.")
    else:
        for i, task in enumerate(tasks, 1): # Membuat nomor dari list, ini dibikin dari nomor 1.
            checkbox = "✅" if task["done"] else " " # Kalau task done, tampilkan centang; kalau belum, tampilkan spasi kosong.
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n----------Task List Manager----------")
        print("1. Add Tasks")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        match choice:
            case "1": # Add Tasks
                text = input("Enter your task: ").strip()
                if text: # Agar tidak masukkan tugas kosong.
                    tasks.append({"text":text, "done": False}) # text (kiri) adalah key, text (kanan) adalah value dari hasil input. "done": False artinya setiap tugas baru statusnya belum selesai makanya dia False.
                    save_tasks(tasks)
                else:
                    print("Task cannot be empty.")

            case "2": # View Tasks
                display_tasks(tasks)
            
            case "3": # Mark Task as Complete
                display_tasks(tasks) # Dia tampilkan list task-nya dulu.
                try:
                    num = int(input("Enter task number: ")) # Pastikan dia pakai int.
                    if 1 <= num <= len(tasks): # Untuk hitung total tugas agar bisa di-cek user input-nya nomor yang ada tugasnya apa tidak.
                        tasks[num-1]["done"] = True # Kalau ada, langsung ubah statusnya jadi done.
                        save_tasks(tasks)
                        print("Task marked as DONE!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

            case "4": # Delete Tasks
                display_tasks(tasks)
                try:
                    num = int(input("Enter task number delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num-1) # Ingat, pop itu hapus.
                        save_tasks(tasks)
                        print(f"Task removed: {removed['text']}") # Removed ini tampilin yang tadi dihapus itu apa.
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a number.")

            case "5":
                print("Exiting Task Manager...")
                break

            case _:
                print("Please choose a valid option.")

task_manager()