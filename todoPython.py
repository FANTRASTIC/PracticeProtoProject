import tkinter as tk
from tkinter import messagebox

class ToDoList:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.tasks = []

        self.task_number = tk.Label(root, text="Tasks: 0")
        self.task_number.pack()

        self.task_entry = tk.Entry(root, width=100)
        self.task_entry.pack()

        self.add_task_button = tk.Button(root, text="Add task", command=self.add_task)
        self.add_task_button.pack()

        self.task_list = tk.Listbox(root, width=100)
        self.task_list.pack()

        self.delete_task_button = tk.Button(root, text="Delete task", command=self.delete_task)
        self.delete_task_button.pack()

        self.strike_task_button = tk.Button(root, text="Strike task", command=self.strike_task)
        self.strike_task_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)
            self.task_number['text'] = f"Tasks: {len(self.tasks)}"
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            self.task_list.delete(task_index)
            self.tasks.pop(task_index)
            self.task_number['text'] = f"Tasks: {len(self.tasks)}"
        except:
            messagebox.showwarning("Warning", "Select a task to delete")

    def strike_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            task = self.tasks[task_index]
            self.tasks[task_index] = f"~~{task}~~"
            self.task_list.delete(task_index)
            self.task_list.insert(task_index, f"~~{task}~~")
        except:
            messagebox.showwarning("Warning", "Select a task to strike")

if __name__ == "__main__":
    root = tk.Tk()
    todo_list = ToDoList(root)
    root.mainloop()








# import tkinter as tk 
# import tkinter.messagebox as tkm


# class ToDoList:
#     def __init__ (self,root):
#         self.root = root
#         self.root.title("Todo List") #sets the window title
#         self.tasks = []

#         #Here is the Task Counter Label use tk.Label with two parameters
#         #also use .pack() so that it is visible in the window
#         self.taskCounter = tk.Label(root, text = 'Task: 0')
#         self.taskCounter.pack()
        
        
#         #Task Input Entry field using tk.Entry with two parameters, width second para
#         #also use .pack() so that it is visible in the window
#         self.inputTask = tk.Entry(root, width = 50)
#         self.inputTask.pack()
        
#         #Task Button, using tk.Button with three parameters, the end parameter is the callback function to self.add_task
#         #also use .pack() so that it is visible in the window
#         self.taskAddButton = tk.Button(root, text = 'Add Task', command = self.addTask)
#         self.taskAddButton.pack()
#         #Task List using tk.Listbox with one parameters
#         #also use .pack() so that it is visible in the window
#         self.taskList = tk.Listbox(root) # listbox shows all the tasks that are added
#         self.taskList.pack()
#         #Delete task Button using tk.Button with three parameters, the end parameter is the callback function to self.delete_task
#         #also use .pack() so that it is visible in the window
#         self.deleteTaskButton = tk.Button(root, text = 'Delete Task', command = self.deleteTask)
#         self.deleteTaskButton.pack()
        
        
#         #Strike task Button using tk.Button with three parameters, the end parameter is the callback function to self.strike_task
#         #also use .pack() so that it is visible in the window
#         self.strikeTaskButton = tk.Button(root, text = 'Strike Task', command = self.strikeTask)
#         self.strikeTaskButton.pack()
#         #Functionality Methods
#         #add_task
#         def addTask(self):
#             pass
#         #delete_task
#         def deleteTask(self):
#             pass

#         #strike_task
#         def strikeTask(self):
#             pass
        
        
#         if __name__ == "__main__":
#             root = tk.Tk()
#             ToDoList(root)
#             root.mainloop()