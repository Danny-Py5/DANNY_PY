'''Setting module'''


import tkinter as tk


class Constants:

    def __init__(self):
        
        self.ROOT_WIDTH = 500
        self.ROOT_HEIGHT = 600
        self.ROOT_BG_COLOR = '#444'
        self.DEFAULT_FG = '#FFF'
        self.LIGHT_GREY = 'lightgrey'
        self.INPUT_FRAME_COLOR = '#4E4F60'
        self.LOGIN_BUTTON_FRAME_BG_COLOR = '#395b4f'
        self.DEFAULT_FONT_STYLE = 'Arial 13'
        self.ERROR_FONT = 'Arial 9'

        self.LOGIN_FONT = 'Arial 30 bold'
        self.LOGIN_FONT_COLOR = 'lightpink'
        self.ERROR_MESSAGE_COLOR = '#FFA4A4'


class Setting(Constants):
    '''the base class for the app.'''
    def __init__(self):
        '''class constructor'''
        Constants.__init__(self)
        
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.set_geometry(width=self.ROOT_WIDTH, height=self.ROOT_HEIGHT)
        self.set_color()

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

    def set_color(self):
        self.root.config(bg=self.ROOT_BG_COLOR)

    def destroy_root_widget(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def onclick_close_window(self):
        self.root.destroy()

    def destroy_window(self):
        if tk.messagebox.askyesnocancel('Close','Do you realy want to close this window?'):
            self.root.protocol("WM_DELETE_WINDOW" ,lambda: self.onclick_close_window)

    def newtop_message(self, title, text):
        '''this method is used to display a msg in a pop up mimicking the tkinter messagebox.'''
        width = 300
        height = 250
        x = (self.root.winfo_screenwidth()- width) - 30
        y = (self.root.winfo_screenheight()- height) - 100
        new_top = tk.Toplevel(self.root, bg=self.ROOT_BG_COLOR, width=width, height=height)
        new_top.title(title)
        new_top.resizable(False, False)
        new_top.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        label = tk.Label(new_top, text=text,font='Arial 13 bold', bg=self.ROOT_BG_COLOR, fg='lightgreen')
        label.pack(pady=75)

        ok_btn = tk.Button(new_top, text='Okay',underline=0, bd=0, bg=self.ROOT_BG_COLOR, font=self.DEFAULT_FONT_STYLE, fg='white', activebackground=self.ROOT_BG_COLOR, activeforeground='lightblue')
        ok_btn.pack()
        return new_top, ok_btn, label


if __name__ == '__main__':
    setting = Setting()
    setting.newtop_message('custom messagebox', 'Hello world!')
    
    
