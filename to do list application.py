import tkinter as tk
from tkinter import simpledialog

class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

def toggle_task(event):
    index = listbox.curselection()
    if index:
        task_index = index[0]
        tasks[task_index].completed = not tasks[task_index].completed
        update_listbox()

def add_task():
    description = simpledialog.askstring("Add Task", "Enter task description:")
    if description:
        due_date = simpledialog.askstring("Add Task", "Enter due date:")
        priority = simpledialog.askstring("Add Task", "Enter priority:")
        new_task = Task(description, due_date, priority)
        tasks.append(new_task)
        update_listbox()

def update_task(event):
    index = listbox.curselection()
    if index:
        task_index = index[0]
        task = tasks[task_index]
        description = simpledialog.askstring("Update Task", "Enter new description:", initialvalue=task.description)
        due_date = simpledialog.askstring("Update Task", "Enter new due date:", initialvalue=task.due_date)
        priority = simpledialog.askstring("Update Task", "Enter new priority:", initialvalue=task.priority)

        if description:
            task.description = description
        if due_date:
            task.due_date = due_date
        if priority:
            task.priority = priority

        update_listbox()

def remove_task():
    index = listbox.curselection()
    if index:
        task_index = index[0]
        del tasks[task_index]
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_display = f"[{'X' if task.completed else ' '}] {task.description} - Due: {task.due_date} - Priority: {task.priority}"
        listbox.insert(tk.END, task_display)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Task list
tasks = []

# Create a Listbox to display tasks
listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=30, width=100)
listbox.pack(pady=30)

# Bind double-click event to toggle task completion
listbox.bind("<Double-1>", toggle_task)

# Buttons for task actions
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=10)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
