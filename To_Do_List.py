import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task)
        self.update_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "[Done]" if task['completed'] else "[Not Done]"
            self.task_listbox.insert(tk.END, f"{index}. {task['task']} {status}")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get()
            if new_task:
                self.tasks[selected_index]['task'] = new_task
                self.update_listbox()
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter a new task!")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update!")

    def mark_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]['completed'] = True
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")


if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()