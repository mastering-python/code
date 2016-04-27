>>> import functools


>>> def plus_one(function):
...     @functools.wraps(function)
...     def _plus_one(self, n):
...         return function(self, n + 1)
...     return _plus_one


>>> class Spam(object):
...     @plus_one
...     def get_eggs(self, n=2):
...         return n * 'eggs'


>>> spam = Spam()
>>> spam.get_eggs(3)
'eggseggseggseggs'
