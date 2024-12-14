class Error(Exception):
    pass

try:raise Error('Error') if 88 > 44 else None
except TypeError: None 

