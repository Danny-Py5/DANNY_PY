'''LoginSystem Module.

this module uses the login system before it can be reashed
although the module might have noting in it interface but
just for me to practice login system to showcase my
knowledge.

Little Tooltip About the LoginSystem:
-----------------------------
Login Button: If user have no account or the login details is
not correct, an error message is displayed else the login frame
will be destroyed after some minutes and the main LoginSystem will show.

Sign up Button: If the button is clicked, create account window
will be displayed for user to create new account.


I don't place widget on the root directly but create a frame for each
LoginSystem and place widget on it after which the previous frame on the
root would have been destroyed.

lines of code with other imported defined module -->> 656 and above'''


# In this project, I used '...' for comment instead of #...
# because i hate when comment shows read. I prefer green

__author__ = 'DannyPy FD'
__date__ = 'Feb 10 2024'
__status__ = 'Developing'

__version__ = '0.1.0'


import tkinter as tk
import re
import random 
from setting import Setting
from login import Login
from file_handling import FileOperation
from create_account import CreateAccount
from verify_account import VerifyAccount

              
class LoginSystem(Login):
    '''Class LoginSystem
    Adds functionalities to the created interfaces Login, Create
    Account, Verify Account and later call the main app'''
    
    file = FileOperation()
    
    def __init__(self, main_app):
        '''class constructor
        :param
            LoginSystem(callable): the main LoginSystem to be called after loging-in
        '''

        self.app = main_app
        
        self.login()
        self.sign_in()

    def call_main_app(self):
        '''call the main application(app) after some seconds.'''
        # Finally, call the main application 
        self.root.after(7000, self.app)

    @classmethod
    def _validate(cls, p_num, psw):
        '''Validate user login inputs.
        param:
        ------
           - p_num(str): phone number of user.
           - psw(str): user passward.
        attr:
        -----
           - user_key(str): user phone number + user hashed passward; (_psw).
        return
        ------
            True, True if login details are correct.'''
        all_accounts = LoginSystem.file.get_all_accounts()
        try:
            _psw = LoginSystem.file.get_hash(psw)[0]
            # added in try...except purposely if posible IndexError is raises.
        except IndexError: return False, False
        
        user_key = p_num + _psw
        "if user_key is not in all_account, it raises KeyError; catch it by using try"
        try:
            if all_accounts[user_key]['pnum'] == p_num and all_accounts[user_key]['psw'] == _psw:    
                return True, True
        except KeyError:
            return False, ''
        
    def try_login(self):
        '''Allow login.
        allow action on the Login login-button and check if inputed
        details is valid that is; already have account: logginable.'''
        p_num, psw = self.get_entry_login_value()
        'check if user already have an account: logginable'
        is_valid = self._validate(p_num, psw)
        if is_valid[0]:
            self.show_info(True, 'Please wait...')  # Login
            self.call_main_app()
            
        elif not all([char.isdigit() for char in p_num]):
            self.show_info(False, 'Phone number must be digits.')
        elif p_num == '' and psw == '':
            self.show_info(False, 'Fill all entry please.')
        elif p_num and psw == '':
            self.show_info(False, 'Input Passward please.')
        elif psw and p_num == '':
            self.show_info(False, 'Input phone number please.')
        else:
            self.show_info(False, 'Passward not correct. Input correct passward please\n---or--\n\nSignup')  # Login

    def login(self):
        '''add command to the login button.
        triggered thecall_main_app try_login func to check input.'''
        super().__init__()
        'add a command to the login button'
        self.login.config(command=self.try_login)
        'bind to Return key'
        self.user_passward.bind('<Return>', self.on_return)

    def on_return(self, event):
        '''call try_login when return key is clicked;
        performs the login button function.'''
        self.try_login()


    def validate_psw_phone(self, new_account_object, psw, phone):
        '''make sure passward have at least 2 (upper,lower,digits and symbols),
        and make sure phone number is digts and has len of 11.
        param:
        -----
           - new_account_object(obj): object of the CreateAccount class.
           - psw(str): user passward.
           - phone: user phone number. 
        returns:
        -------
            False, psw: if craiterials not ment in passward else True.
            False, phone: if not all char in phone number isdigit else True.'''
        psw_match = [[1 for c in psw if not c.isalpha() and not c.isnumeric()],\
                    [1 for c in psw if c.islower()], [1 for c in psw if c.isupper()]]
        if not all([len(i) > 1 for i in psw_match]):
            return False, 'psw'
        elif not all([i.isdigit() for i in phone]) or not len(phone) >= 11:
            return False, 'phone'
        else:
            return True, True

    def del_new_top(self, ok_button, new_top):
        'delete the newtop when the the ok button is clicked'
        ok_button.config(command=new_top.destroy)
        
    def send_verification_code(self, send_code=False):
        '''show popup containg the verification number.'''
        global code
        code = random.choice(list(range(1000, 9999, 7)))
        new_top, ok_button, label = self.newtop_message(title='Verification Code:', text='Please wait while \nverification code is sent...')
        if send_code:
            new_top.after(3000)
            label.config(text=str(code))
        self.del_new_top(ok_button, new_top)

    def verify_account(self, verify_account_obj, get_signin_values=None):
        '''compares user input verification code to the one sent on popup
        param:
        -----
            verify_account_obj(object): object of he the cerification account.
            code(int): code being sent to in a popup. -> global
        returns: True if user_input_code == sent_code else False'''
        
        user_input_code = verify_account_obj.entry.get()
        sent_code = code # global in self.send_verification_code()
        if user_input_code == str(sent_code):
            'Add user details to json file'
            verify_account_obj.status_label.config(fg='lightgreen', text='\n\nPlease Wait...')
            surename, f_name, s_name, p_num, psw = get_signin_values()
            LoginSystem.file.add_account(surename, f_name, s_name, p_num, psw)
            self.call_main_app()
        else:
            verify_account_obj.status_label.config(fg=self.ERROR_MESSAGE_COLOR, text='\n\nPlease input the correct verification code')

    def check_already_have_account(self, p_num, psw):
        '''checks account already exist while creating new.'''
        all_accounts = LoginSystem.file.get_all_accounts()
        _psw = LoginSystem.file.get_hash(psw)[0]
        user_key = p_num + _psw
        for key in all_accounts:
            if key == user_key:
                return False
        else:
            return True
    
    def __add_new_account(self, new_account_object=None):
        '''add user details when the sign in button is clicked using the
        verify_account method to add the details after user input
        verification code matches the sent one. #LoginSystem.verify_account.__doc__
        param:
            new_account: instance of CreateAccount.'''
        if new_account_object is None:
            return
        surename, f_name, s_name, p_num, psw = new_account_object.get_entry_signin_values()
        if not self.check_already_have_account(p_num, psw):
            new_account_object.show_status(False, 'You already have an account please login.')
            return 
        # run validation on psw and p_num
        if all(['' not in [surename, f_name, s_name, p_num, psw]]):
            is_valid = self.validate_psw_phone(new_account_object, psw, p_num)
            if not is_valid[0] and is_valid[1] == 'psw': 
                new_account_object.show_status(False, 'passward must have at least 2 upper and lower case characters,\nand at least 2 digits, and 2 symbols')
                return 
            elif not is_valid[0] and is_valid[1] == 'phone':
                new_account_object.show_status(False, 'Phone number must be digit and be a valid number.')
                return 
            else:
                #new_account_object.show_status(True, 'Please wait while verification code is sent...')       
                verify_account = VerifyAccount()
                self.send_verification_code()
                verify_account.send_code_button.config(command=lambda: self.send_verification_code(send_code=True))
                verify_account.verify_button.config(command=lambda:self.verify_account(verify_account, new_account_object.get_entry_signin_values))
        else:
            new_account_object.show_status(False, 'Fill all the entry please.')
            
    def create_new_account(self):
        '''instantiate the CreateAccount interface when the
        sign in button is clicked.'''
        'close the login window.'
        # self.onclick_close_window()  # Setting
        new_account = CreateAccount()
        'add command to the sign in button'
        new_account.sign_in.config(command=lambda: self.__add_new_account(new_account))

        #new_account.back.config(command=self.onclick_close_window)
        
    def sign_in(self):
        self.sign_up.config(command=self.create_new_account)
        
    def run(self):
        self.root.mainloop()


def main():
    from myapp import MyApp
    
    ls = LoginSystem(MyApp)
    ls.run()


if __name__ == '__main__':
    main()
    







