# import random
# import string

# print("Welcome to Password Generator App!")

# length = int(input("Enter the length Of Password: "))

# longs = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(length):
#     password += random.choice(longs)

# print(f"Your Generated Password is: {password}")

import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    length = int(entry.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    for i in range(length):
        password += random.choice(characters)
    
    result_label.config(text=password)

# Create window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Title Label
title_label = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16))
title_label.pack(pady=10)

# Entry box
entry = tk.Entry(root)
entry.pack(pady=5)

entry.insert(0, "8")  # default length

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run window
root.mainloop()