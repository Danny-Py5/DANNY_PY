# use existing code from login project by adding it to path
__import__('sys').path.append('C:/Users/user/Desktop/mytkinter/login')


from login import Login
login = Login()
# close the login window 
login.onclick_close_window()
# refference to methods to be used.
create_frame = login.create_frame
create_label = login.create_label
create_entry_with_label = login.create_entry_with_label
create_label = login.create_label


import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
import sqlite3 as sqlite

#print(colorchooser.askcolor())

__date__ = 'April 3, 2024'
__author__ = 'Daniel Fatokun'
__status__ = "Developing"
__email__ = 'danielolatunde943@gmail.com'


WIDTH = 1100
HEIGHT = 580
WINDOW_BG_COLOR = '#000'
MAIN_FRMAE_BG_COLOR = '#555'
LEFT_MAIN_FRAME_BG_COLOR = '#181533'
RIGHT_MAIN_FRAME_BG_COLOR = '#1a1a1a'
ENTRY_HIGHLIGHT_BG = '#dea630'
ADD_BUTTON_BG = '#666dff'
ADD_BUTTON_AFG = '#041eff'
STATUS_BAR_BG = '#c2c2c2'
RIGHT_FRAME_HIGHLIGHT_BG = '#757575'

LIST_BOX_BG='#222'
SELECT_BG = '#666'


class ApprenticesDB:

    def __init__(self):
        self.connection = sqlite.connect('apprentices.db')
        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):
        with self.connection:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS apprentice (
                      ID TEXT,
                      firstname TEXT,
                      surname TEXT,
                      age INTEGER,
                      gender TEXT
                ) 
            """)

    def add_apprentice(self, ID=None, f_name:str=None, surname:str=None, age:int=None, gender:str=None):
        # use the with keyword so as to close the db authomatically after the code block
        # is executed otherwise, you will explicitly close like this -> self.connection.close()
        with self.connection:
            self.cursor.execute("INSERT INTO apprentice (ID, firstname, surname, age, gender) VALUES (?, ?, ?, ?, ?)",
                                (ID, f_name.lower(), surname.lower(), age, gender.lower()))
            # no need to commit as the with take care of that
            
    def get_all(self):
        self.cursor.execute('SELECT * FROM apprentice')
        return self.cursor.fetchall()

    def get_byID(self, ID):
        '''get apprentice by id'''
        self.cursor.execute('SELECT * FROM apprentice WHERE ID=:apprn_id',
                            {'apprn_id': ID})
        return self.cursor.fetchall()

    def delete_byID(self, ID):
        '''remove specific apprentice with the given ID'''
        with self.connection:
            self.cursor.execute('DELETE FROM apprentice WHERE ID=:apprn_ID',
                                {'apprn_ID': ID})
        # NO NEED TO COMMIT SINCE 'with' take care of that.
        # e.g self.connection.commit()
    

class Apprentices:
    '''class Apperentices.'''
    
    adb = ApprenticesDB()
    
    def __init__(self):
        '''class constructor'''
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.set_geometry(width=WIDTH, height=HEIGHT)
        self.root.config(bg=WINDOW_BG_COLOR)
        self.root.title('Seudeb Apprentices Management')

        #print([x for x in dir(self.root) if x == 'winfo_height'])

        self.entry_feild = ['ID', 'First Name', 'Surname', 'Age', 'gender']
        
        # create frames.
        self.main_frame = create_frame(self.root, expand=False, width=WIDTH, height=HEIGHT-100,
                                       bg=MAIN_FRMAE_BG_COLOR)
        self.left_main_frame = create_frame(self.main_frame, expand=True, width=WIDTH//3,
                       height=HEIGHT-100, bg=LEFT_MAIN_FRAME_BG_COLOR, isgrid = True, row=0, column=0)
        self.right_main_frame = create_frame(self.main_frame, expand=True, width=WIDTH - (WIDTH//3),
                       height=HEIGHT-100, bg=RIGHT_MAIN_FRAME_BG_COLOR, isgrid = True, row=0, column=1,
                       h_background=RIGHT_FRAME_HIGHLIGHT_BG, h_thickness=2)
        
        self.buttom_main_frame = create_frame(self.main_frame, expand=True, width=WIDTH - (WIDTH//3),
                       height=HEIGHT-100, bg=WINDOW_BG_COLOR, isgrid = True, row=1, column=0, c_span=2)
        for i in range(2):
            self.buttom_main_frame.columnconfigure(i, weight=1)

        # adding widgets to left and right frame
        self.ID = create_entry_with_label(self.left_main_frame, width=12, islabel=True, label='{:<15}'.format('ID:'),
                                            row=0, column=0, pady=10, padx=2, font='Arial 12 bold', label_bg=LEFT_MAIN_FRAME_BG_COLOR,
                                            entry_bg='white', highlight_bg=ENTRY_HIGHLIGHT_BG, highlight_tks=2)
        
        self.f_name = create_entry_with_label(self.left_main_frame, width=12, islabel=True, label='{:<15}'.format('First Name:'),
                                            row=1, column=0, pady=30, padx=5, font='Arial 12 bold', label_bg=LEFT_MAIN_FRAME_BG_COLOR,
                                            entry_bg='white', highlight_bg=ENTRY_HIGHLIGHT_BG, highlight_tks=2)
        
        self.surname = create_entry_with_label(self.left_main_frame, width=12, islabel=True, label='{:<15}'.format('Surname:'),
                                            row=2, column=0, pady=30, padx=5, font='Arial 12 bold', label_bg=LEFT_MAIN_FRAME_BG_COLOR,
                                            entry_bg='white', highlight_bg=ENTRY_HIGHLIGHT_BG, highlight_tks=2)
        
        self.age = create_entry_with_label(self.left_main_frame, width=12, islabel=True, label='{:<15}'.format('Age:'),
                                            row=3, column=0, pady=30, padx=5, font='Arial 12 bold', label_bg=LEFT_MAIN_FRAME_BG_COLOR,
                                            entry_bg='white', highlight_bg=ENTRY_HIGHLIGHT_BG, highlight_tks=2) 

        self.gender = create_entry_with_label(self.left_main_frame, width=12, islabel=True, label='{:<15}'.format('gender:'),
                                            row=4, column=0, pady=30, padx=5, font='Arial 12 bold', label_bg=LEFT_MAIN_FRAME_BG_COLOR,
                                            entry_bg='white', highlight_bg=ENTRY_HIGHLIGHT_BG, highlight_tks=2)
        # store all the entry widget in a tuple for refference
        self.all_entrys = (self.ID, self.f_name, self.surname, self.age, self.gender)
        self.add_button = self.create_button(self.left_main_frame, 'Add Apprentice', row=5, column=0, c_span=2, command=self.on_click_add_button, bg=LEFT_MAIN_FRAME_BG_COLOR, fg=ADD_BUTTON_BG, a_bg=LEFT_MAIN_FRAME_BG_COLOR, a_fg= ADD_BUTTON_AFG)


        # right
        self.toolbar_label = create_label(self.right_main_frame, bg=STATUS_BAR_BG, font=('Helvetica', 13, 'bold'), text=' {:^10}| {:^25}| {:^25}| {:^10}|  {:^15}'.format('ID', 'First Name', 'Surname', 'Age', 'gender'))
        self.list_box = self.create_list_box()

        
        #buttom
        self.delete_button = self.create_button(self.buttom_main_frame, 'Remove Apprentice', row=0, column=0, command=self.on_click_remove, bg='red', fg='white', a_bg='#8e0640', a_fg='white')
        self.update_button = self.create_button(self.buttom_main_frame, 'Update Apprentice', row=0, column=1, command=self.on_click_update, bg='#66db6f', fg='white', a_bg='#42a226', a_fg='white')

        
        
    def empty_all_entrys(self):
        '''delete all entrys value.'''
        for entry in self.all_entrys:
            entry.delete(0, tk.END)
            
    def update_entry(self, event):
        '''update entry with the selected apprentices details'''
        details = self.getlist_box_selection()
        if isinstance(details, list):
            self.empty_all_entrys()
            for index, detail in enumerate(details):
                self.all_entrys[index].insert(0, detail)
        
    def getlist_box_selection(self, is_index=False):
        selected = self.list_box.curselection()
        if selected:
            selected_index = int(selected[0])
            details = self.list_box.get(selected_index).split()
            return selected_index if is_index else details
        else:
            return False

    def is_exist(self, details) -> bool:
        '''check if details already exist.
        return True if apprentice already exists else None.'''
        # get all apprentices
        all_existing_apprn = Apprentices.adb.get_all()
        # loop through all apprn
        for existing_apprn_details in all_existing_apprn:
            # convert all elements of both details and existing details to lower chr
            a = [str(d).lower() for d in existing_apprn_details]
            b = [str(d).lower() for d in details]
            if a == b:
                return True

    def validate_entry(self, entry_details, is_update=False):
        '''run validations on the entrys values to meet some needs.'''
        if self.is_exist(entry_details):  
            if is_update:
                pass
            else:
                messagebox.showwarning('Warning', "Apprentice already exist!")
                return True
        # check for entry that hasn't been filled
        # entry_details param will be a str if not all the entry has been filled
        if isinstance(entry_details, str):
            messagebox.showwarning('Warning', 'Input Apprentice '+entry_details)
            return False
        if Apprentices.adb.get_byID(entry_details[0]):
            return False
            messagebox.showwarning('Warning', 'Apprentice already exist with ID {}'.format(entry_details[0]))
            return False
        if len(entry_details[0]) >=5:
            messagebox.showwarning('Warning', "ID must be less than 5 characters")
            return False
        return True

    def on_click_add_button(self):
        entry_details = self.get_entrys_value()
        if self.validate_entry(entry_details):
            Apprentices.adb.add_apprentice(ID=entry_details[0], f_name=entry_details[1], surname=entry_details[2],
                           age=entry_details[3], gender=entry_details[4])
            self.list_box.insert(tk.END, 
                               ' {:^15}  {:<35}  {:<30}    {:^10}  {:^15}'.format(
                                entry_details[0], entry_details[1].capitalize(), entry_details[2].capitalize(),
                                entry_details[3], entry_details[4].capitalize()
                                )
                )
            messagebox.showinfo('Info', "Apprentices added!")
            # set entry to ''
            for i in self.all_entrys:
                i.delete(0, tk.END)

    def on_click_remove(self):
        details = self.getlist_box_selection()
        if details:
            yes = messagebox.askyesnocancel('Delete', 'Are you sure you want to removed\nthe selected apprentice?')
            if yes:
                selected_apprn = self.getlist_box_selection(is_index=True)
                self.list_box.delete(selected_apprn)
                Apprentices.adb.delete_byID(details[0])
                messagebox.showinfo('Info', 'Apperentice removed')
        else:
            messagebox.showinfo('Info', 'You have not selected any apperentice')

    def on_click_update(self):
        selected_apprn_index = self.getlist_box_selection(is_index=True)
        selected_apprn_detail = self.getlist_box_selection()
        new_details = self.get_entrys_value()
        
        if selected_apprn_index != False:
            if self.validate_entry(new_details, is_update=True):
                self.list_box.delete(selected_apprn_index)
                self.list_box.insert(selected_apprn_index,
                            ' {:^15}  {:<35}  {:<30}    {:^10}  {:^15}'.format(
                            new_details[0], new_details[1].capitalize(),
                            new_details[2].capitalize(),  new_details[3], new_details[4].capitalize()
                        ))
                Apprentices.adb.delete_byID(new_details[0])

    def get_entrys_value(self):
        '''get and return the entrys value.'''
        details = [x.get().strip() for x in self.all_entrys]
        try:
            first_unfilled_index = [i for i, j in enumerate(details) if j ==''][0]
            return self.entry_feild[first_unfilled_index]
        except IndexError:
            # return the filled details since there is no entry that hasn't been filled
            # coz, raising index error implies that all the entry are filled. 
            return details 
        
    def create_list_box(self):
        list_box = tk.Listbox(self.right_main_frame, width=(WIDTH - (WIDTH//3)), selectforeground='cyan',
                                   bg=LIST_BOX_BG, height=HEIGHT, fg="white", selectbackground=SELECT_BG,
                                   font=('Times New Roman', 11, 'bold'), cursor="hand2")
        existing_apprentices = Apprentices.adb.get_all()
        for apprentice in existing_apprentices:
            list_box.insert(tk.END,
                               ' {:^15}  {:<35}  {:<30}    {:^10}  {:^15}'.format(
                                apprentice[0], apprentice[1].capitalize(), apprentice[2].capitalize(),  apprentice[3], apprentice[4].capitalize()
                                ))
        list_box.bind('<Double-1 >', self.update_entry)
        list_box.pack()
        return list_box
        
    def create_button(self, root, text, row=0, column=0, c_span=1, command=None, bg=None, fg=None, a_bg=None, a_fg=None):
        button = tk.Button(root, underline=0, bd=0, text=text, bg=bg or LEFT_MAIN_FRAME_BG_COLOR, fg=fg,
                           activebackground=a_bg or LEFT_MAIN_FRAME_BG_COLOR, activeforeground=a_fg or 'green', font=('constantia', 14, 'bold'),
                           cursor='hand2', command=command)
        button.grid(row=row, column=column, sticky=tk.NSEW, columnspan=c_span, padx=5, pady=10)
        return button
            
    def set_geometry(self, width, height, dx=0, dy=0):
        '''sets the geometry of the window to center of the screen.
        param:
        ------
           - width:(int): the width of the window.
           - height(int): the height of the window.
           - dx(int): to move the window away from the center of the screen in x-axis
           - dy(int): to move the winsow away from the center of the screen in y-axis'''
        self.x = ((self.root.winfo_screenwidth() - width) // 2) - dx
        self.y = ((self.root.winfo_screenheight() - height) // 2) - dy
        self.root.geometry('{}x{}+{}+{}'.format(width, height, self.x, self.y))
         
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    a = Apprentices()
    a.run()

