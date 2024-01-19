import tkinter as tk
import customtkinter as ctk

def add_todo():
    task = open('task.txt', 'a+')
    todo = task_todo.get()
    todo = str(todo)
    if len(todo) != 0:
        task.write('\n'+todo)
        checkbox_label = ctk.CTkCheckBox(frame_todo, text=todo, width=400, checkbox_width=20, checkbox_height=20)
        checkbox_label.pack()

    else:
        print("pls type something")

    task.close()

def reset_todo():
    for w in frame_todo.winfo_children():
        w.destroy()


app = ctk.CTk()

app.title("TODO List")

app.geometry("500x500")
ctk.set_appearance_mode("system")

heading = ctk.CTkLabel(app, text="TODO List", width=500, pady=10, font=("Helvetica", 20)).pack()


addbutton = ctk.CTkButton(app, text="Add", command=add_todo)
addbutton.place(relx=0.05, rely=0.1, anchor='nw')

clearbutton = ctk.CTkButton(app, text="Clear")
clearbutton.place(relx=0.5, rely=0.1, anchor='n')

resetbutton = ctk.CTkButton(app, text="Reset", command=reset_todo)
resetbutton.place(relx=0.95, rely=0.1, anchor='ne')

task_todo = ctk.CTkEntry(app, placeholder_text="Enter your Task ToDo", width=450)
task_todo.place(relx=0.5, rely=0.18, anchor='n')

frame_todo = ctk.CTkScrollableFrame(app, width=450, height=350)
frame_todo.place(relx=0.5, rely=0.25, anchor='n')

task = open("task.txt", 'a+')
t_list = []
for i in task:   # not working
    print(i)
    t_list.append(i)
task.close()
print(t_list)
for i in t_list:
    checkbox_label = ctk.CTkCheckBox(frame_todo, text=i, width=4000, checkbox_width=20, checkbox_height=20)
    checkbox_label.pack()

app.mainloop()
