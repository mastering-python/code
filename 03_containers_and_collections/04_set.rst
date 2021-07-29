Sets
#####

Example 1
----------

.. code-block:: python

    sp = set('sp')
    spam = set('spam')
    eggs = set('eggs')

    def print_set(set_):
        'Print set as a string sorted by letters'
        print(''.join(sorted(set_)))

**Set operations**

>>> print_set(spam)
amps
>>> print_set(eggs)
egs
>>> print_set(spam & eggs) # Intersection of spam and eggs
s
>>> print_set(spam | eggs) # Union of spam and eggs
aegmps
>>> print_set(spam ^ eggs) # Symmetric difference of spam and eggs
aegmp
>>> print_set(spam - eggs) # Difference of spam and eggs
amp
>>> print_set(eggs - spam) # Difference of eggs and spam
eg
>>> print(spam > eggs) # Check if eggs is a subset of spam
False
>>> print(eggs > spam) # Check if spam is a subset of eggs
False
>>> print(spam > sp) # Check if sp is a subset of spam
True
>>> print(spam < sp) # Check if spam is a subset of sp
False

Example 2
----------

**Calculating new lists from 2 user sets**

.. code-block:: python

    current_users = set(('a', 'b', 'd',))
    new_users = set(('b', 'c', 'd', 'e',))

>>> to_insert = sorted(new_users - current_users)
['c', 'e']
>>> to_delete = sorted(current_users - new_users)
['a']
>>> unchanged = sorted(new_users & current_users)
['b', 'd']
