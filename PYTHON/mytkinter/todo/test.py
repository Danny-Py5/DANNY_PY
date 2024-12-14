def delele_task():
    """calls _remove_task() to remove task from task file and also\nremove from list_box interface"""
    selected_indices = list_box.curselection()
    
    if selected_indices: # will run it item is selected only to prevent IndexError
        selected_task_index = int(selected_indices[0])#[lb.get(index) for index in selected_indices]
        selected_task = list_box.get(selected_task_index)
        
        question = mg.askyesnocancel("Question","Are you sure you want to\ndelete {}?".format(selected_task))
        if question:
            file = "task_list.txt"
            updated = []
            with open(file,"r",encoding="UTF-8") as f:
                for val in f:
                    if val == "\n":
                        continue
                    updated.append(val.strip())
                print(updated)
            with open(file,"w",encoding="UTF-8") as f:
                for val in updated:
                    if val == selected_task:
                        continue
                    f.write(val+"\n")
            
            list_box.delete(selected_task_index)
            mg.showinfo("Info","Task deleted")
