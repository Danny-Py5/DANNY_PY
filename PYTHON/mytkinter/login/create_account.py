import tkinter as tk
from login import Login
from setting import Setting


class CreateAccount(Login, Setting):
    '''class create account.
    create Create Account interface.'''
    def __init__(self):
        # call the Setting __init__ attr 
        Setting.__init__(self)
        self.root.title('Create Account')
        
        self.create_label(self.root, 'Login', pady=30, bg=self.ROOT_BG_COLOR, fg=self.LOGIN_FONT_COLOR)
        self.input_frame = self.create_frame(self.root, bg=self.INPUT_FRAME_COLOR, pady=40, fill=tk.X)
        self.surename = self.create_entry_with_label(self.input_frame, row=0, islabel=True, label='Surename:', column=0, pady=5)

        self.f_name = self.create_entry_with_label(self.input_frame, row=1, islabel=True, label='First Name:', column=0, pady=5)

        self.s_name = self.create_entry_with_label(self.input_frame, row=2, islabel=True, label='Second Name:', column=0, pady=5)

        self.p_num = self.create_entry_with_label(self.input_frame, row=4, islabel=True, label='Phone:', column=0, pady=5)

        self.psw = self.create_entry_with_label(self.input_frame, row=3, islabel=True, label='Passward:', column=0, pady=5)

        self.status = self.create_status_label(self.root)
        
        self.button_frame = self.create_frame(self.root, fill=tk.X, bg=self.LOGIN_BUTTON_FRAME_BG_COLOR)
        self.sign_in = self.create_button('Sign in', bg=self.LOGIN_BUTTON_FRAME_BG_COLOR, fg='lightpink')
        #self.back = self._back() #self.create_label(self.root, '<', isplace=True, x=0, y=500, bg=self.ROOT_BG_COLOR, fg=self.LOGIN_FONT_COLOR)

    def _back(self):
        btn = self.create_button(text='<', bg=self.LOGIN_BUTTON_FRAME_BG_COLOR, fg='lightpink', activebg=self.LOGIN_BUTTON_FRAME_BG_COLOR, activefg='lightblue')
        return btn

    def get_entry_signin_values(self):
        surename = self.surename.get().lower()
        f_name = self.f_name.get().lower()
        s_name = self.s_name.get().lower()
        p_num = self.p_num.get()
        psw = self.psw.get()
        return surename, f_name, s_name, p_num, psw

    def show_status(self, param:bool, text=None, fg=None):
        if param:
            self.status.config(text=text if text else '', fg=fg if fg else 'lightgreen')
        else:
            self.status.config(text=text if text else 'Error:', fg=fg if fg else self.ERROR_MESSAGE_COLOR)


if __name__ == '__main__':
    c = CreateAccount()
    
