>>> class A(object):
...     spam = 1

>>> class B(A):
...     pass

>>> A.spam
1
>>> B.spam
1

>>> A.spam = 2

>>> A.spam
2
>>> B.spam
2

