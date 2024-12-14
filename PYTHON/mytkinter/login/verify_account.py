import tkinter as tk
from login import Login
from setting import Setting


class VerifyAccount(Login, Setting):
    '''class VerifyAccount\nCreate Verify Account interface.'''
    def __init__(self):
        '''class constructor.'''
        # call to Setting constructor to use it attrs
        Setting.__init__(self)

        self.root.title('Verify Account')
        self.set_geometry(width=self.ROOT_WIDTH, height=self.ROOT_HEIGHT, dx=-20, dy=-40)

        self.verification_frame = self.create_frame(self.root, bg=self.ROOT_BG_COLOR)
        self.create_label(self.verification_frame, 'Verify Account',pady=20, bg=self.ROOT_BG_COLOR, fg=self.LOGIN_FONT_COLOR)

        self.create_label(self.verification_frame, text='Input verification code:', font='Arial 10 bold', pady=60, fg=self.LIGHT_GREY, bg=self.ROOT_BG_COLOR)
        
        self.input_frame = self.create_frame(self.verification_frame, bg=self.INPUT_FRAME_COLOR, pady=10, fill=tk.X)
        self.entry = self.create_entry_with_label(self.input_frame, row=0, column=0, pady=5)
        self.entry.focus()

        self.send_code_button = self.create_get_code_again_button()
        self.verify_button = self.create_verify_button()

        self.status_label = self.create_label(self.verification_frame, text='', font=self.ERROR_FONT, bg=self.ROOT_BG_COLOR, pady=0, padx=0)

        
    def create_get_code_again_button(self):
        again_btn = tk.Button(self.verification_frame, text='Resend code', underline=0, bd=0, bg=self.ROOT_BG_COLOR, font=self.DEFAULT_FONT_STYLE, fg='gray', activebackground=self.ROOT_BG_COLOR, activeforeground='lightblue')
        again_btn.pack(expand=True)
        return again_btn

    def create_verify_button(self):
        btn = tk.Button(self.verification_frame, text='verify', underline=0, bd=0, bg=self.ROOT_BG_COLOR, font=self.DEFAULT_FONT_STYLE, fg='gray', activebackground=self.ROOT_BG_COLOR, activeforeground='lightblue')
        btn.pack(expand=True)
        return btn
            

if __name__ == '__main__':
    v = VerifyAccount()
