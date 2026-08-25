from logging import root
import tkinter as tk
import datetime

# root = tk.Tk()
# root.title("This Shit off")
# root.geometry("400x400")

# title_label = tk.Label(root, text="🔐 Password Generator", font=("Times New Roman", 16))
# title_label.pack(pady=10)

# rott = tk.Toplevel(root)
# rott.title("Password Result")
# rott.geometry("400x1000")

# tit_label = tk.Label(rott, text="Nenrings", font=("Courier New", 16))
# tit_label.pack(pady=10)

# reo = tk.Toplevel(rott)
# reo.title("Nemasis")
# reo.geometry("900x900")

# root.mainloop()

roiot = tk.Tk()
roiot.geometry("400x400")


# clock label
clock_Label = tk.Label(
    roiot,
    font=("Courier New", 30, "bold"),
    bg="lightblue",
    fg="black"
)
clock_Label.place(relx=0.5,rely=0.4, anchor="center")

def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock_Label.config(text=current_time)
    clock_Label.after(1000, update_clock)

update_clock()
roiot.mainloop()

