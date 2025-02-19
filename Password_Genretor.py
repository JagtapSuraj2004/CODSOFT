import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            messagebox.showerror("Error", "Password length must be greater than 0!")
            return
        password = generate_password(length)
        label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

label_instruction = tk.Label(root, text="Enter the desired length of the password:")
label_instruction.pack(pady=10)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", command=on_generate)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="Generated Password: ")
label_result.pack(pady=10)

root.mainloop()