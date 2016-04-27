>>> import ctypes


>>> class Spam(ctypes.Structure):
...     _fields_ = [
...         ('spam', ctypes.c_int),
...         ('eggs', ctypes.c_double),
...     ]
... 
>>> spam = Spam(123, 456.789)
>>> spam.spam
123
>>> spam.eggs
456.789

