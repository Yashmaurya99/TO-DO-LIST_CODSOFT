import tkinter
import tkinter.messagebox
import pickle

window = tkinter.Tk()
window.title("My To-Do List")

def task_adding():
    todo = entry_task.get()
    if todo != "":
        todo_box.insert(tkinter.END, todo)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Attention!!", message="To add a task, please enter some task!!")

def task_removing():
    try:
        index_todo = todo_box.curselection()[0]
        todo_box.delete(index_todo)
    except IndexError:
        tkinter.messagebox.showwarning(title="Attention!!", message="To delete a task, you must select a task")

def task_load():
    try:
        todo_list = pickle.load(open("task.dat", "rb"))
        todo_box.delete(0, tkinter.END)
        for todo in todo_list:
            todo_box.insert(tkinter.END, todo)
    except FileNotFoundError:
        tkinter.messagebox.showwarning(title="Attention!!", message="Cannot find task.dat")

def task_save():
    todo_list = todo_box.get(0, tkinter.END)
    pickle.dump(todo_list, open("task.dat", "wb"))

list_frame = tkinter.Frame(window)
list_frame.pack()

todo_box = tkinter.Listbox(list_frame, height=20, width=60)
todo_box.pack(side=tkinter.LEFT)

scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT, fill=tkinter.Y)
todo_box.config(yscrollcommand=scroller.set)

entry_task = tkinter.Entry(window, width=70)
entry_task.pack()

add_task_button = tkinter.Button(window, text="CLICK TO ADD TASK", font=("arial", 20, "bold"), background="blue", width=40, command=task_adding)
add_task_button.pack()

delete_task_button = tkinter.Button(window, text="CLICK TO DELETE TASK", font=("arial", 20, "bold"), background="red", width=40, command=task_removing)
delete_task_button.pack()

load_task_button = tkinter.Button(window, text="CLICK TO LOAD TASK", font=("arial", 20, "bold"), background="green", width=40, command=task_load)
load_task_button.pack()

save_task_button = tkinter.Button(window, text="CLICK TO SAVE TASK", font=("arial", 20, "bold"), background="yellow", width=40, command=task_save)
save_task_button.pack()

window.mainloop()
