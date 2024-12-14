'''Login Module'''

import tkinter as tk
from setting import Setting


class Login(Setting):
    '''class Loging.
    create the GUI of Login.'''
    
    def __init__(self):
        '''class constructor'''
        #call to super function
        super().__init__()
        self.root.title('Login')
        self.set_geometry(width=self.ROOT_WIDTH, height=self.ROOT_HEIGHT, dx=20, dy=30)

        self.login_frame = self.create_frame(self.root, bg=self.ROOT_BG_COLOR)
        self.create_label(self.login_frame, 'Welcome Back!\nLogin', pady=20, bg=self.ROOT_BG_COLOR, fg=self.LOGIN_FONT_COLOR)
        
        self.input_frame = self.create_frame(self.login_frame, fill=tk.X, bg=self.INPUT_FRAME_COLOR)
        self.user_phone = self.create_entry_with_label(self.input_frame, row=0, islabel=True, label='Phone', column=0, pady=30)
        self.user_passward = self.create_entry_with_label(self.input_frame, row=1, islabel=True, label='Passward', column=0, pady=30)

        self.invalid_details = self.create_status_label(self.login_frame, pady=18)
        
        self.button_frame = self.create_frame(self.login_frame, pady=10, bg=self.LOGIN_BUTTON_FRAME_BG_COLOR, fill=tk.X)
        self.login, self.sign_up = self.create_login_signup_button()
        self.islogin = False

    
    def get_entry_login_value(self):
        num = self.user_phone.get()
        psw = self.user_passward.get()
        return num, psw

    def delete_entry_value(self):
        self.user_phone.delete(0, tk.END)
        self.user_passward.delete(0, tk.END)

    def show_info(self, param:bool, msg=''):
        '''show login error text.'''
        if param:
            self.invalid_details.config(text= msg, fg='lightgreen')
        else:
            self.invalid_details.config(fg=self.LOGIN_FONT_COLOR, text= msg)
        
    def create_frame(self, root, bd=0, side=None, c_span=1, h_background='white', h_thickness=0, expand=False, bg='#fff', isgrid=False, row=0, column=0, pady=0, padx=0, fill=None, width=0, height=0):
        '''create frame with the specify param and pack it by default:
        root, bg='#fff', pady=0, padx=0, fill=None
        - root(window): root for the widget to be placed.
        - bg(hex_str): the background color of the frame.
        - width(int): the width of the frame.
        - height(int): the height of the frame.c_span
        - isgrid(bool): used for placing the widget with grid if it's set to True.
        - row(int): the row of which the widget is placed.
        - column(int): the column of which the widget if placed.
        - c_span(int): columnspan.'''
        frame = tk.Frame(root, bg=bg, highlightbackground=h_background, highlightthickness=h_thickness)
        if width and height:
            frame.pack_propagate(False)
            frame.config(width=width, height=height)
        if isgrid:
            frame.grid(padx=padx, pady=pady, row=row, column=column, sticky=tk.NSEW, columnspan=c_span)
        else:
            frame.pack(fill=fill, side=side, expand=expand or False, pady=pady, padx=padx)
        return frame

    def create_label(self, root, text, isplace=False, x=0, y=0, font=None, bg='white', fg='black', pady=0, padx=0):
        '''create label on specified root with the specified text.
        param:
            root(tk.root|Frame): root where the widget should be placed.
            text(str): text to be displayed.
            pady,padx(int): space around the text in x or y.
            x,y(int): the x and y to be used for place (placing the widget).
            isplace(bool)->False: if set to True, the text will be displayed using .place(x,y)
            font(str): font of the widget eg. "Arial 10 bold".
            bg(str)-> white: the background color of the text.
            fg(str)-> black: the foreground color of the text.'''
        label = tk.Label(root, text=text, font=self.LOGIN_FONT if not font else font, fg=fg, bg=bg)
        label.pack(pady=pady, padx=padx) if not isplace else label.place(x=x, y=y)
        return label

    def create_status_label(self, root, pady=0):
        '''Performs the same function as the create_label() but takes no arg just created for readability
        instead, creat_label should have been used like this self.create_label(root, text)'''
        label = tk.Label(root, text='', font=self.ERROR_FONT, fg=self.LOGIN_FONT_COLOR, bg=self.ROOT_BG_COLOR)
        label.pack(pady=pady)
        return label

    def create_entry_with_label(self, root, highlight_bg='white', highlight_tks=0, font='Arial 13', label_bg=None, entry_bg=None, width=0, islabel=False, label='Name this label', row=None, column=None, pady=None, padx=None):
        '''create entry with a label and pack the entry with grid
        param:
           - islable(bool)-> False: if set to True, it adds a label before the entry else after.
           - label(str)-> '' : text for the label.
           - row,column(int)-> None: row and column of both the label and the entry.
           - pady,padx(int)-> None: pady and padyx for both the label and the entry.
           - width(int)->0: width of the entry
           - label_bg(str): bg color for the label.
           - entry_bg(str): bg color for the entry
           - font(str): font style.'''
        if islabel:
            label = tk.Label(root, text=str(label)+' '*2, bg=label_bg or self.INPUT_FRAME_COLOR, fg=self.DEFAULT_FG, font=font)
            label.grid(row=row, column=column, pady=pady, padx=padx)
        entry = tk.Entry(root, width=width or 25, font=font, bg=entry_bg or self.LIGHT_GREY,
                highlightbackground=highlight_bg, highlightthickness=highlight_tks, bd=0)
        #print(help(entry))
        entry.grid(ipadx=5, ipady=4, row=row, column=column+1, pady=pady, padx=padx) if islabel else entry.pack(pady=pady, padx=padx, ipadx=5, ipady=4)
        entry.focus()
        return entry

    def create_button(self, text=None, bg='white', fg='black', activebg='red', activefg='lightblue', font='Arial 14'):
        button = tk.Button(self.button_frame, underline=0, bd=0, text=str(text), bg=bg, font=font, fg=fg, activebackground=activebg, activeforeground=activefg)
        button.pack()
        return button

    def create_login_signup_button(self):
        login = tk.Button(self.button_frame, bd=0, text='Login', bg='lightblue', font=self.DEFAULT_FONT_STYLE)
        login.grid(row=0, column=0, pady=15, padx=40)
        #create space
        tk.Label(self.button_frame, text=' '*44, bg=self.LOGIN_BUTTON_FRAME_BG_COLOR).grid(row=0, column=1)
        sign_up = tk.Button(self.button_frame, bd=0, text='Sign in', bg='lightblue', font=self.DEFAULT_FONT_STYLE)
        sign_up.grid(row=0, column=2, pady=15, padx=40)
        return login, sign_up


if __name__ == '__main__':
    a = Login()
