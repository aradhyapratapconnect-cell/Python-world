# import tkinter as tk
# from tkinter import mainloop, messagebox

# def add_task():
#     task = entry.get()
#     if task! = "":
#         listbox.insert(tk.END, task)
    

    
#     with open("to_do.txt", "a") as f:
#         f.write(task + "\n")
        
#     entry.delete(0, tk.END)

# def view_tasks():
#     try:
#         with open("to_do.txt", "r") as f:
#             tasks = f.readlines()
#             if not tasks:
#                 print("No tasks found 📭")
#             else:
#                 print("\n📝 Your To-Do List:")
#             for i, task in enumerate(tasks, start=1):
#                 print(f"{i}. {task.strip()}")
#     except FileNotFoundError:
#         print("No tasks found 📭")

# def delete_task():
#     view_tasks()
#     try:
#         task_no = int(input("Enter task number to delete: "))
#         with open("todo.txt", "r") as f:
#             tasks = f.readlines()

#             if 1 <= task_no <= len(tasks):
#                 tasks.pop(task_no - 1)
#                 with open("to_do.txt", "w") as f:
#                     f.writelines(tasks)
#                     print("Task deleted 🗑️")
#             else:
#                 print("Invalid task number ❌")
#     except:
#         print("Error deleting task ❌")

# add_task



# todo_window.mainloop()6
