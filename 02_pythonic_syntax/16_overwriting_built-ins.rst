Overwriting BIFs
#################

Example 1 
----------

**Not recommended**

list = [1, 2, 3]

**Recommended**

list_ = [1, 2, 3]

Example 2
----------

**Trying to overwrite list keyword**

>>> list = list((1, 2, 3))
>>> list
[1, 2, 3]

>>> list((4, 5, 6))
Traceback (most recent call last):
...
TypeError: 'list' object is not callable

**Trying to overwrite import keyword**

>>> import = 'Some import'
Traceback (most recent call last):
...
SyntaxError: invalid syntax