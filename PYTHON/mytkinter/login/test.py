class Parent1:
    def __init__(self):
        self.name = 'Parent1 init is called'

class Parent2:
    def __init__(self):
        self.name = 'Parent2 init is called'

class Use(Parent1, Parent2):
    def __init__(self):
        #super(Parent1, self).__init__() # misbehaves
        Parent1.__init__(self) # Normal
        print(self.name)

        Parent2.__init__(self)
        print(self.name)
     
##use = Use()
##print(hasattr(list, 'sort'))

#print(__import__('os').listdir())


a = ''
if a:
    print(a, 'is not None Nor False')
else:
    print(a, 'is None or False')
    
# print(open('account_file.json').read())

# __import__('os').remove('account_file.json')

import hashlib

'''
using hashlib

h = hashlib.sha256(b'hello world')
hash_digest = h.hexdigest()
print(hash_digest)
    ----or-----
h2 = hashlib.new('SHA256')
h2.update(b'asdfasd')
hs = h2.hexdigest()
#print(hs)
'''


#print(hashlib.algorithms_available)


h = hashlib.sha256(b'hello world')
hash_digest = h.hexdigest()
#print(hash_digest)

h2 = hashlib.new('SHA256')
h2.update(b'asdfasd')
hs = h2.hexdigest()
#print(hs)


hh = hashlib.new('SHA256')
psw = b'coder@12345'
hh.update(psw)
real_passward = hh.hexdigest()

hh2 = hashlib.new('SHA256')
psw2 = b'coder@12345'
hh2.update(psw2)
input_passward = hh2.hexdigest()

#print(real_passward == input_passward)


def get_hash(string):
    raw = hashlib.sha256(string.encode())
    return raw.hexdigest()

first_hash = get_hash('Hello world!')
second_hash = get_hash('Hello world!')
#print(first_hash == second_hash)


def _get_hash(*arg):
    encode_list = [hashlib.sha256(i.encode()) for i in arg]
    hexdigest_list = [i.hexdigest() for i in encode_list]
    return hexdigest_list

hex_list = _get_hash('hello1', 'hello')
#print(_get_hash('asdfasd','asdfaasdfa')[0])
_1, _2 = hex_list[0], hex_list[1]
#print(get_hash('hello1') == _1)

import re

search = re.compile('^[0-9]+$')
a = 'match' if search.search('12') else 'not match'
#print(a)

psw = 'ASsdfgs#fd45435@$%#%#%'
psw_match = re.compile('[A-Z]{2}[a-z}+[0-9]+[^a-zA-Z0-9]{3}')
def psss():
    if psw_match.search(psw):
        print('matches passward')
    else:
        print('passward must have 2 uppercase characters,\n at least 1 digits and 3 symbols')

lower = 0
upper = 0 
for i in psw:
    if i.isupper():
        upper += 1
    if i.islower():
        lower += 1

match = [[1 for c in psw if not c.isalpha() and not c.isnumeric()],\
        [1 for c in psw if c.islower()],[1 for c in psw if c.isupper()]]

if not all([len(i) > 2 for i in match]):
    print('error')
else:
    print('good')


    
