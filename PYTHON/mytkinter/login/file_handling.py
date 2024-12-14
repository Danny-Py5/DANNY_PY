import os
import json
import hashlib


class FileOperation:
    '''class FileOperation.
    handles the file opetation.'''
    def __init__(self):

        self.FILE = 'account_file.json'

        self.__create_file()

        self.all_acc = self.all_accounts()

    def __create_file(self):
        '''create file to keep all accounts created if self.FILE not in that dir.'''
        if self.FILE not in os.listdir():
            with open(self.FILE, 'w', encoding='UTF-8') as f:
                new = dict()
                json_string = json.dumps(new)
                f.write(json_string)
            
    def all_accounts(self):
        with open(self.FILE, 'r', encoding='UTF-8') as f:
            read = f.read()
            if len(read) <= 0:
                return dict()
            else:
                f.seek(0)
                return json.load(f)

    def write_in_file(self):
        '''write  in file: always in 'w' mode as attr to be written will be updated before writing'''
        with open(self.FILE, 'w', encoding='UTF-8') as f:
            json_string = json.dumps(self.all_acc, indent=4)
            f.write(json_string)

    def get_hash(self, *arg):
        # loop through arg(s) and encode them for hexdigest
        # encode list: a list containing encoded str of each value in arg.
        encode_list = [hashlib.sha256(i.encode()) for i in arg]
        # hexdigest all encoded str in encoded_list.
        hexdigest_list = [i.hexdigest() for i in encode_list]
        return hexdigest_list
    
    def add_account(self, surename, f_name, s_name, p_num, psw):
        hex_list = self.get_hash(psw)
        hashed_psw = hex_list[0]
        user_key = p_num + hashed_psw
        self.all_acc[user_key] = {'surename': surename, 'fname': f_name, 'sname': s_name, 'pnum': p_num, 'psw': hashed_psw}
        self.write_in_file()
        return None
        
    def get_all_accounts(self):
        self.all_user_details = self.all_accounts()
        all_accounts = self.all_user_details
        return all_accounts

if __name__ == '__main__':
    acc = FileOperation()
    acc.add_account('fatokfffun', 'danffiel','olatunde','08165521fasdfa344','2342sdasdfas3sadfa')
    acc.add_account('fatokun', 'daniel','olatunde','08165521fasdfa344','2342sdasdfas3sadfa')
    print(acc.all_accounts())
    #print(acc.get_hash('iasdfasdfasd', '23424'))
##    for (i, j) in acc.get_all_accounts().items():
##        print(i)
##        print()
