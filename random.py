import tkinter as tk
from tkinter import mainloop, messagebox
from loginsys import Signup
from loginsys import Login


# GUI Setup 

# Window setup
root = tk.Tk()
root.title("Login To Clocke")
root.geometry("500x500")
root.configure(bg="lightblue")

# Username Label and Entry
tk.Label(root, text="Login To Clocke", font=("Courier New", 20)).pack(pady=30)
tk.Label(root,text="Username").pack()
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password Label and Entry
tk.Label(root,text="Password").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)
tk.Label(root,text="Login System",
         bg="yellow",
         fg="red",
         font=("Courier New", 12)).pack(pady=20)

# Buttons
tk.Button(root,text="Signup",width=15,command=Signup,
          bg="#00FFFF",
          fg="#BC13FE",
          activebackground="#FFFF33"
          ).pack(pady=12)
tk.Button(root,text="Login",width=15,command=Login,
          bg="green",
          fg="white",
          activebackground="darkgreen"
).pack(pady=5)





# after login main home scrreen
def home_screen(username):
    home = tk.Toplevel(root)
    home.title(f"Welcome To Clocke \n{username}")
    home.geometry("500x500")


    tk.Label(home,
             text=f"Welcome To Clocke,{username}!",
             font=("Courier New", 16),  
                bg="lightblue",     
                fg="darkblue"
             ).pack(pady=30)
    
    def Logout():
        home.destroy()    #closes the main home window
        root.deiconify()   #re-open the login window

    tk.Button(home,text="Logout",width=20,command=Logout,
        bg="#0CBABA",
        fg="#380036",
        activebackground="#0CBABA"
        ).grid(relx=1.0,rely=1.0,anchor="ne",x=-10,y=10)


root.mainloop()

