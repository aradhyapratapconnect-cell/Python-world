import tkinter as tk
from u_to_do import add_task
from u_to_do import view_tasks
from u_to_do import delete_task

root = tk.Tk()
root.title("Yooo")
root.geometry("500x500")

def open_todo():
    import u_to_do   # file where you wrote the code

# buttons
todo_btn = tk.Button(root, text="To Do List", command=open_todo)
todo_btn.place(x=300, y=200, width=150, height=50,
        bg="#00C9A7",
        fg="#EAEAEA",
        activebackground="#00B894"
        ).pack(pady=12)

root.mainloop()