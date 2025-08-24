import tkinter as tk
from tkinter import messagebox

# Filename to store tasks
filename = "tasks.txt"

# Create main window
root = tk.Tk()
root.title("Anu's To-Do List 🤍")
root.geometry("400x500")
root.resizable(False, False)

# List to store tasks
tasks = []

# ---- Functions ----

def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        with open(filename, "a") as file:
            file.write(task + "\n")
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "❌ Please enter a task!")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        tasks.pop(selected_index)
        with open(filename, "w") as file:
            for task in tasks:
                file.write(task + "\n")
    except IndexError:
        messagebox.showwarning("Select Task", "❌ Please select a task to delete!")

# ---- Widgets ----

# Entry box
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=20)

# Add Task Button
add_button = tk.Button(root, text="➕ Add Task", font=("Arial", 12), width=15, command=add_task)
add_button.pack(pady=10)

# Task Listbox (create only ONCE!)
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Delete Task Button
delete_button = tk.Button(root, text="❌ Delete Selected", font=("Arial", 12), width=18, command=delete_task)
delete_button.pack(pady=10)

# ---- Load tasks from file AFTER creating task_listbox ----
try:
    with open(filename, "r") as file:
        for line in file:
            task = line.strip()
            if task:
                tasks.append(task)
                task_listbox.insert(tk.END, task)
except FileNotFoundError:
    open(filename, "w").close()

# ---- Run App ----
root.mainloop()