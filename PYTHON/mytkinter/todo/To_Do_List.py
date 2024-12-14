
'''
pagenevigatingframe: is placed on the left side of the app that allows nevigation

'''



import tkinter as tk
from tkinter import messagebox as mg
import json 



WIDTH = 500
HEIGHT=500
INPUT_FRAME_COLOR = "azure"
BACKGROUNCOLOUR = "midnightblue"


enable_add_mg = True
enable_empty_mg = True


##def rgb_to_hex(rgb):
##    if len(rgb) == 3:
##        return "#{:02x}{:02x}{02x}".format(*rgb)
##    else:
##        return "white"
    

def enable_add_msg(bool):
    global enable_add_mg

    if bool == False:
        enable_add_mg = False
    elif bool == True:
        enable_add_mg = True

def enable_empty_msg(bool):
    global enable_empty_mg
    
    if bool == True:
        enable_empty_mg = True
    elif bool == False:
        enable_empty_mg = False

     
def add_task():
    new_entry= task_entry.get().title()
    if new_entry:
        list_box.insert(tk.END,new_entry)
        with open("task_list.txt","a") as f:
            f.write(new_entry)
            f.write("\n")

        # delete the entry box
        task_entry.delete(0,"end")
        # show the needful message
        if enable_add_mg == True:
            mg.showinfo("Add task","Task Added!")
    else:
        if enable_empty_mg == True:
            mg.showwarning("Warning","Task Input is\nEmpty")

def on_enter(event):add_task()

def clear_completed_task():
    pass

def clear_completed_task():
    pass

    
def _read():
    '''return a list of tasks in task file'''
    
    with open("task_list.txt","r",encoding="UTF-8") as f:
        all_tasks = f.readlines()
        
        return all_tasks
    
        
def delele_task():
    '''delete selected task from task_file  and GUI interface'''
    selected_indices = list_box.curselection()
    if selected_indices: # will run it item is selected only to prevent IndexError
        selected_task_index = int(selected_indices[0])#[lb.get(index) for index in selected_indices]
        selected_task = list_box.get(selected_task_index)
        
        question = mg.askyesnocancel("Question","Are you sure you want to\ndelete {}?".format(selected_task))
        if question:
            file = "task_list.txt"
            # get all tasks from task file
            with open(file,"r",encoding="UTF-8") as f:
                updated = [val.strip() for val in f if val !="\n"]           
                with open(file,"w",encoding="UTF-8") as f:
                    for val in updated:
                        if val == selected_task:
                            continue
                        f.write(val+"\n")
            
                list_box.delete(selected_task_index)
                mg.showinfo("Info","Task deleted")
            
def on_rightclick(event):print("Hello")
            
# add menu bar
def menubar(root):
    menu_bar = tk.Menu(root)
    option_menu = tk.Menu(menu_bar,tearoff=0)
    setting_menu = tk.Menu(menu_bar,tearoff=0)
    help_menu = tk.Menu(menu_bar,tearoff=0)

    menu_bar.add_cascade(label="Option",menu=option_menu)
    menu_bar.add_cascade(label="Settings",menu=setting_menu)
    menu_bar.add_cascade(label="Help",menu=help_menu)


    setting_menu.add_command(label="Add task without message",command= lambda: enable_add_msg(False))
    setting_menu.add_command(label="Add task with message",command= lambda: enable_add_msg(True))
    setting_menu.add_command(label="Disable entry warning",command= lambda: enable_empty_msg(False))
    setting_menu.add_command(label="Enable entry warning",command=lambda: enable_empty_msg(True))

    option_menu.add_command(label="Close",command=exit)
    root.config(menu=menu_bar)





# --------------------------------
# Page frame used functions
# --------------------------------
def hide_indicator():
    
    personal_list_indicator.config(bg="lightblue")
    quick_list_indicator.config(bg="lightblue")
    
def show_indicator(indicator):
    hide_indicator()
    
    indicator.config(bg=BACKGROUNCOLOUR)
    
# Page nevigation
def pagenevigatingframe(root):
    '''pagenevigatingframe: placed on the left side of the app that allows nevigation

       child widget:
           - 
           - 
    '''
    global personal_list_indicator,quick_list_indicator
    # used in hide_indicator()
    
    page_frame = tk.Frame(root,highlightbackground=BACKGROUNCOLOUR,highlightthickness=2,
                          bg="lightblue")
    
    quick_list = tk.Button(page_frame,fg=BACKGROUNCOLOUR,bd=0,text="Quick list",font=("Comic Sans MS",10,"bold"),
                           bg="lightblue",command= lambda:show_indicator(quick_list_indicator))
    quick_list.place(x=5,y=100)

    quick_list_indicator = tk.Label(page_frame,text="",bg=BACKGROUNCOLOUR,height=2)
    quick_list_indicator.place(x=1,y=100)

    personal_list = tk.Button(page_frame,fg=BACKGROUNCOLOUR,bd=0,text="Personal",font=("Comic Sans MS",10,"bold"),
                              bg="lightblue",command= lambda:show_indicator(personal_list_indicator))
    personal_list.place(x=5,y=160)

    personal_list_indicator = tk.Label(page_frame,text="",bg="lightblue",height=2)
    personal_list_indicator.place(x=1,y=160)
    
    page_frame.pack_propagate(False)    
    page_frame.config(width=100,height=HEIGHT)
    page_frame.pack(side=tk.LEFT)



### input frame###################################
def inputframe(root):
    
    global task_entry
    
    input_frame = tk.Frame(root,bg=INPUT_FRAME_COLOR,highlightbackground="lightblue",
                           highlightthickness=2)
    
    input_label = tk.Label(input_frame,text="Input:",bg=INPUT_FRAME_COLOR,
                       font=("Helvetica",12))
    input_label.place(x=5,y=5)

    task_entry = tk.Entry(input_frame,highlightbackground="black",
                      highlightthickness=1,bd=0,width=27)
    task_entry.place(x=5,y=55)
    # bind with the Enter Key
    task_entry.bind("<Return>",on_enter)

    add_btn=tk.Button(input_frame,bg=INPUT_FRAME_COLOR,fg="blue",bd=0,text="Add Task",
                      font=("Helvetica",12),command=add_task)
    add_btn.place(x=70,y=100)

    input_frame.pack_propagate(False)
    input_frame.config(width=235,height=150)
    input_frame.pack(side=tk.TOP,padx=5,pady=5)#place(x=5,y=10)
    
############################################




# task frame
def taskframe(root):
    
    global list_box
    
    tasks_frame= tk.Frame(root,bg=INPUT_FRAME_COLOR,highlightbackground="lightblue",
                          highlightthickness=2)

    # task label
    task_label = tk.Label(tasks_frame,text="Tasks\n"+"- "*20,
                      font=("Helvetica",12),bg="azure")
    task_label.pack(side="top",expand=True,fill="both")

    #create list box and load default task
    
    
    list_box = tk.Listbox(tasks_frame,selectmode=tk.SINGLE,width=255,font=("Times New Roman",12))
    list_box.pack(side="top",expand=True,fill="both")
    
    all = _read()
    for task in all:
        if task == "\n":
            continue
        list_box.insert(tk.END,task.strip())    
    tasks_frame.pack_propagate(False)
    tasks_frame.config(width=235,height=150)
    tasks_frame.pack(side=tk.TOP,padx=5)#place(x=255,y=10)
    

# Add the buttons -> (2)buttons clear ans  del
def actionbutton(root):
    delete_btn= tk.Button(root,text="Delete selected task",bd=0,bg=BACKGROUNCOLOUR,fg="lightblue",
                        font=("Helvetica",12),command=delele_task)
    delete_btn.pack()
    
    clear_btn= tk.Button(root,text="Clear completed task",bd=0,bg=BACKGROUNCOLOUR,fg="lightblue",
                     font=("Helvetica",12))
    clear_btn.pack()

    

def on_close(root):
    msg = mg.askyesno("Question","Do you realy want to close the app?")
    if msg:
        root.destroy()

def welcomeinterface(root):
    frame = tk.Frame(root)

    label = tk.Label(frame,text="You are welcome\nI have been expecting you!",
                     fg="lightblue",font=("Arial",15))
    label.pack(side=tk.LEFT)
    close = tk.Button(text="Click me",fg="lightblue",font=("Arial",15),bd=0)

    frame.pack()
    
def main(root):
    '''controls the behaviour and placement of widgets
       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
       
    '''
    root.title("To Do List")
    root.geometry("350x420+900+0")
    root.config(bg="white")#BACKGROUNCOLOUR)
    root.resizable(False,False)

    taskwindow = tk.Frame(root,highlightbackground=BACKGROUNCOLOUR,highlightthickness=2)
    
    taskwindow.pack_propagate(False)
    taskwindow.config(width=250,height=HEIGHT,bg=BACKGROUNCOLOUR)
    taskwindow.pack(side=tk.LEFT)
    
    menubar(root) #placed on the main root
    
    inputframe(taskwindow)

    taskframe(taskwindow)
    actionbutton(taskwindow)

    close = root.protocol("WM_DELETE_WINDOW" ,lambda:on_close(root))
if __name__ == "__main__":
    root=tk.Tk()
    pagenevigatingframe(root)
    main(root)
    root.mainloop()



















