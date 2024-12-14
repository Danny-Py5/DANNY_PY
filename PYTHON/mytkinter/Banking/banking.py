import json
import datetime
import os
        

class Banking:
    FILE = 'account_file.json'
    def __init__(self):
        self._create_file()
        
        self.all_accounts = self.load_accounts()
    
    def load_accounts(self):
        with open(Banking.FILE, 'r') as f:
            try:
                return json.load(f)
            except Exception as e:
                # that means the file is empty or it content not a json type
                return dict()

    def _create_file(self):
        '''create file to keep all accounts created if self.FILE not in that dir.'''
        if self.FILE not in os.listdir():
            with open(self.FILE, 'w', encoding='UTF-8') as f:
                new = dict()
                json_string = json.dumps(new)
                f.write(json_string)
                
    def _write_to_file(self):
        with open(Banking.FILE, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(self.all_accounts, indent=4))
            
    def is_exist_account(self, acc_num) -> bool:
        return str(acc_num) in self.all_accounts.keys()


class Account(Banking):

    def __init__(self, account_number=None):
        super().__init__()
        
        self.acc_num = account_number
        
        self._validate_acc_num()

    def _validate_acc_num(self):
        if self.acc_num is not None and not self.is_exist_account(self.acc_num):
            raise ValueError('Invalid account num:', self.acc_num)

    def create_account(self, name:str, age:int, psw:int, acc_num:int, initial_depo:int):
        assert str(acc_num) not in self.all_accounts.keys(), 'account already exist'
        #print(type(acc_num), [type(x) for x in self.all_accounts.keys()])
        with open(self.FILE, 'a',) as f:
            account = {
                'name':name,
                'age':age,
                'pasword':psw,
                'account_number':acc_num,
                'initial_deposit':initial_depo,
                'balance': 0,
                'history': []
                }
            self.all_accounts[acc_num] = account
            self._write_to_file()
            
        return 'Account Created!'

    def deposit(self, amount, ffrom=None) -> int:
        '''deposit money and return balance'''
        if self.acc_num is not None:
            initially_deposited = self.all_accounts[str(self.acc_num)]['initial_deposit']
            self.all_accounts[str(self.acc_num)]['balance'] += amount + initially_deposited
            self.all_accounts[str(self.acc_num)]['initial_deposit'] = 0

            #re-write the updated balances
            self._write_to_file()
            #print(self.all_accounts.get(str(self.acc_num)))

            self._update_history('Deposit', ffrom=ffrom, to='main account')
            return self.all_accounts[str(self.acc_num)]['balance']
        return False

    def withdraw(self, amount):
        if self.acc_num is not None:
            self.all_accounts[str(self.acc_num)]['balance'] -= amount
            self.all_accounts[str(self.acc_num)]['initial_deposit'] = 0

            #re-write the updated balances
            self._write_to_file()
            
            self._update_history('Withdraw', tfrom='Main account')
            return self.all_accounts[str(self.acc_num)]['balance']
        return False


    def check_balance(self):
        return self.all_accounts[str(self.acc_num)]['balance'] \
               if self.acc_num is not None else False
        
    
    def _update_history(self, ttype, tfrom=None, to=None):
        '''
           ttype(str): transaction type: 
        '''
        date = datetime.datetime.today().strftime('%d-%m-%Y')
        time = datetime.datetime.today().strftime('%I:%m%p')

        history = [ttype, {
                'date': date,
                'time': time,
                'from': tfrom,
                'to': to,
            }]
        
        self.all_accounts[str(self.acc_num)]['history'].append(history)
        #re-write to file to keep changes
        self._write_to_file()



def main():
    bnk = Account(45244543)
##  print(bnk.create_account('daniel ola', 20, 12345, 45244543, 100))
    #print(bnk.deposit(7000))
    #print(bnk.withdraw(350))
##    print(bnk.check_balance())
##    print(bnk._update_history('deposit'))

if __name__ == '__main__':
    main()
            
            

    
            

    
