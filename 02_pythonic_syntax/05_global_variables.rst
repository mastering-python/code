>>> spam = 1
>>> def eggs():
...     print('Spam: %r' % spam)

>>> eggs()
Spam: 1

>>> spam = 1

>>> def eggs():
...     spam += 1
...     print('Spam: %r' % spam)

>>> eggs()
Traceback (most recent call last):
    ...
UnboundLocalError: local variable 'spam' referenced before assignment

