import os
import tkinter as tk
from tkinter import filedialog


WIDTH = 700
HEIGHT = 800

FILE_NAME = '[New]'

class Text:

    file = ''
    
    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry('{}x{}'.format(WIDTH, HEIGHT))
        self.update_file_name()
        
        self.create_menu()
        
        self.option_frame = self.create_option_frame()
        self.text = tk.Text(self.root, font='Arial 12', width=self.root.winfo_screenwidth(), insertbackground='blue',
                            highlightthickness=1, highlightcolor='#555')
        self.text.bind('<Control-s>', lambda event: self.save())
        self.text.bind('<Control-o>', lambda event: self.open_file())
        self.text.bind('<Control-n>', lambda event: self.create_new_file())
        self.text.pack(expand=True, side=tk.TOP, fill=tk.Y)

        # label =  tk.Label(self.root, text='asdfa').pack()

    def create_new_file(self):
        '''create new window'''
        new = Text()
        new.run()
    
    def read_file(self):
        with open(Text.file, 'r') as f:
            load =  f.read()
        return load
    
    def write_in_file(self, text):
        with open(Text.file, 'w', encoding='UTF-8') as f:
            f.write(text)
            
    def open_file(self):
        opened_file = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            filetypes = [
                    ('Text File', '*.txt'),
                    ('HTML FIle', '*.html'),
                    ('CSS FIle', '*.css'),
                    ('JavaScript File', '*.js'),
                    ('All Files', '*.*')
                ]
            )
        if opened_file:
            Text.file = opened_file
            file_content = self.read_file()
            new_window = Text()
            new_window.update_file_name(Text.file)
            new_window.text.insert(tk.END, file_content)
            new_window.run()
            
    def new_save(self):
        path = filedialog.asksaveasfile(
            initialdir=os.getcwd(),
            defaultextension='.txt',
            filetypes = [
                    ('Text File', '*.txt'),
                    ('HTML FIle', '*.html'),
                    ('CSS FIle', '*.css'),
                    ('JavaScript File', '*.js'),
                    ('All Files', '*.*')
                ]
            )
        if path:
            with open(path.name, 'w', encoding='UTF-8') as f:
                Text.file = path.name
                self.update_file_name(path.name)
            
    def continue_saving(self):
        text_input = self.text.get('1.0', tk.END)
        self.write_in_file(text_input)
            
    def save(self):
        file_name = self.root.title().split(' ')[-1]
        if file_name[0] == '[':
            self.new_save()
        else:
            self.continue_saving()

    def update_file_name(self, file_name=FILE_NAME):
        self.root.title('Text Editor: {}'.format(os.path.basename(file_name)))
        
    def create_menu(self):
        # create a menu bar
        menu = tk.Menu(self.root)
        # create a file menu on the menu bar
        file_menu = tk.Menu(menu, tearoff=0)
        option_menu = tk.Menu(menu, tearoff=0)
        #add cascades on the menu bar
        menu.add_cascade(label="File", menu=file_menu)
        menu.add_cascade(label='Option', menu=option_menu)
        # add command to a specific cascade
        file_menu.add_command(label='New File' + ' '*40 + 'Ctrl+N', command=self.create_new_file)
        file_menu.add_command(label='Save' + ' '*40 + 'Ctrl+S', command=self.save)
        file_menu.add_command(label='Open' + ' '*40 + 'Ctrl+O', command=self.open_file)
        option_menu.add_command(label='Exit', command=self.root.destroy)
        # add to the root
        self.root.config(menu=menu)
        
    def create_option_frame(self):
        frame = tk.Frame(self.root, bg='#a1a1a1')
        frame.pack_propagate(False)
        frame.config(width=self.root.winfo_screenwidth(), height= 100)
        frame.pack(side=tk.TOP)
        return frame
    
    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    t = Text()
    t.run()
