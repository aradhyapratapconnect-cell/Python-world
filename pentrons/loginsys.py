import tkinter as tk
from tkinter import mainloop, messagebox
import datetime


# Backend Function 
def Signup():
    username = entry_username.get()
    password= entry_password.get()

    if username == "" or password == "":
        messagebox.showerror("Error","\nPlease Fill the required properly")
        return
    with open("user_info.txt", "a") as f:
        f.write(username + "," + password + "\n")

    with open("user_info.txt", "r") as f:
        for lines in f:
            stored_username = lines.strip().split(",")[0]
            if username == stored_username:
                messagebox.showerror("Error", "\nUsername already exists. Please choose a different username.")
                entry_username.delete(0, tk.END)           
                entry_password.delete(0, tk.END)
                return
            
    messagebox.showinfo("Success", "\nAccount was Successfully created")
    entry_username.delete(0, tk.END)           
    entry_password.delete(0, tk.END)
    root.withdraw()
    home_screen(username)
    return

def Login():
    username = entry_username.get()
    password = entry_password.get()

    # ✅ First check empty fields
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill all fields properly")
        return

    try:
        with open("user_info.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")

                if username == stored_username and password == stored_password:
                    messagebox.showinfo("Success", "Login Successful!")
                    entry_username.delete(0, tk.END)           
                    entry_password.delete(0, tk.END)
                    root.withdraw()   # hide login window
                    home_screen(username)
                    return

        # If loop finishes and no match found
        messagebox.showerror("Error", "Invalid Username or Password")

    except FileNotFoundError:
        messagebox.showerror("Error", "No users registered yet!")

# GUI Setup 

# Window setup
root = tk.Tk()
root.title("Login To Clocke")
root.geometry("500x500")
root.configure(bg="#0F2027")

# Username Label and Entry
tk.Label(root, text="Login To Clocke", font=("Segoe UI", 18, "bold")).pack(padx=10, pady=5)
tk.Label(root,text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Label and Entry
tk.Label(root,text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
tk.Label(root,text="Login System",
         bg="#0F2027",
         fg="#EAEAEA",
         font=("Courier New", 12)).pack(pady=20)

# Buttons
tk.Button(root,text="Signup",width=15,command=Signup,
          bg="#00C9A7",
          fg="#EAEAEA",
          activebackground="#00B894"
          ).pack(pady=12)
tk.Button(root,text="Login",width=15,command=Login,
          bg="#00C9A7",
          fg="#EAEAEA",
          activebackground="#00B894"
).pack(pady=5)


def home_screen(username):
    home = tk.Toplevel(root)
    home.title(f"Welcome To Clocke \n{username}")
    home.geometry("500x500")
    home.configure(bg="#1E1E2E")

    tk.Label(
        home,
        text=f"Welcome To Clocke, {username}!",
        font=("Segoe UI", 18, "bold"),
        bg="#1E1E2E",
        fg="#FFFFFF"
    ).place(relx=0.5, rely=0.2, anchor="center")

    # CLOCK LABEL (attached to home!)
    clock_Label = tk.Label(
        home,
        font=("Courier New", 30, "bold"),
        bg="lightblue",
        fg="black"
    )
    clock_Label.place(relx=0.5, rely=0.4, anchor="center")

    running = True  # flag to control clock updates
    # store after id
    after_id = None

    def update_clock():
        if not running:
            return  # important!
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        clock_Label.config(text=current_time)
        after_id = home.after(1000, update_clock)

    def Logout():
        nonlocal running
        running = False
        # stop the clock safely
        home.destroy()
        root.deiconify()

    tk.Button(
        home,
        text="Logout",
        width=20,
        command=Logout,
        bg="#00C9A7",
        fg="#EAEAEA"
    ).place(relx=1.0, rely=0.0, anchor="ne", x=-10, y=10)

    # home.protocol("WM_DELETE_WINDOW", Logout) # handle window close
    update_clock()
       


    def to_do_list():   # function that will add to do list to home page
        home.withdraw()

        todo_window = tk.Toplevel(home)
        todo_window.title("To Do List")
        todo_window.geometry("500x500")

        def back_btn():   # ✅ INSIDE
            todo_window.destroy()
            home.deiconify()

        back_button = tk.Button(todo_window, text="⬅ Back", command=back_btn,
            bg="#FF7675",
            fg="white"  ,      )
        back_button.pack(pady=10)
        
        def add_task():
                task = task_entry.get()
                if task != "":
                    with open("to_do.txt", "a") as f:
                        f.write(task + "\n")
                    task_listbox.insert(tk.END, task)
                    task_entry.delete(0, tk.END)


        def delete_task():
                selected = task_listbox.curselection()
                if selected:
                    task_listbox.delete(selected)

        task_listbox = tk.Listbox(todo_window , width=40, height=10)    
        task_listbox.pack(pady=10)

        def view_tasks():
                task_listbox.delete(0, tk.END)   # clear previous tasks
                try:
                    with open("to_do.txt", "r") as f:
                        tasks = f.readlines()

                    if not tasks:
                        task_listbox.insert(tk.END, "No tasks found 📭")
                    else:
                        for i, task in enumerate(tasks, start=1):
                            task_listbox.insert(tk.END, f"{i}. {task.strip()}")

                except FileNotFoundError:
                    task_listbox.insert(tk.END, "No tasks found 📭")


            # Entry box
        task_entry = tk.Entry(todo_window, width=30)
        task_entry.pack(pady=10)

            # Add button
        add_btn = tk.Button(todo_window, text="Add Task", command=add_task)
        add_btn.pack()


        # Delete button
        del_btn = tk.Button(todo_window, text="Delete Task", command=delete_task)
        del_btn.pack()

    
        # view button
        view_btn = tk.Button(todo_window, text="View Tasks", command=view_tasks)
        view_btn.pack(pady=5)

        view_tasks()


            # button  for entering the to do list
    tk.Button(home,text="Your To Do List",width=15,command=to_do_list,
            bg="#00C9A7",
            fg="#EAEAEA",
            activebackground="#00B894"
            ).pack(pady=12)
    


   
root.mainloop()