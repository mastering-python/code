Tuples
#######

Example 1
-----------

**Using tuples as dict keys**

.. code-block:: python

    spam = 1, 2, 3
    eggs = 4, 5, 6

    data = dict()
    data[spam] = 'spam'
    data[eggs] = 'eggs'

>>> import pprint  # Using pprint for consistent and sorted output
>>> pprint.pprint(data)
{(1, 2, 3): 'spam', (4, 5, 6): 'eggs'}

Example 2
----------

**Using nested tuples as dict keys**

.. code-block:: python

    spam = 1, 'abc', (2, 3, (4, 5)), 'def'
    eggs = 4, (spam, 5), 6

    data = dict()
    data[spam] = 'spam'
    data[eggs] = 'eggs'

>>> import pprint  # Using pprint for consistent and sorted output
>>> pprint.pprint(data)
{(1, 'abc', (2, 3, (4, 5)), 'def'): 'spam',
(4, ((1, 'abc', (2, 3, (4, 5)), 'def'), 5), 6): 'eggs'}

Example 3
----------

**Assign using tuples on both sides**

.. code-block:: python
    
    a, b, c = 1, 2, 3

>>> a
1
>>> b
2
>>> a
3

**Assign a tuple to a single variable**

.. code-block:: python
    
    spam = a, (b, c)

>>> spam
(1, (2, 3))

**Unpack a tuple to two variables**

>>> a, b = spam
>>> a
1
>>> b
(2, 3)

Example 4
-----------

**Unpack with variable length objects which actually 
assigns as a list, not a tuple**

.. code-block:: python
    
    spam, *eggs = 1, 2, 3, 4

>>> spam
1
>>> eggs
[2, 3, 4]

**Unpack a list to a tuple**

.. code-block:: python

    a, b, c = eggs

>>> c
4

**Using ranges instead of fixed numbers**

.. code-block:: python
    
    spam, *eggs = range(10)

>>> spam
0
>>> eggs
[1, 2, 3, 4, 5, 6, 7, 8, 9]

**Which works both ways**

.. code-block:: python

    a, b, *c = a, *eggs

>>> a
2

>>> a, b
(2, 1)
>>> c
[2, 3, 4, 5, 6, 7, 8, 9]

Example 5
-----------

**Using tuples as function arguments**

.. code-block:: python

    def eggs(*args):
        print('args:', args)

>>> eggs(1, 2, 3)
args: (1, 2, 3)

**Using tuples as return values**

.. code-block:: python
    
    def spam_eggs():
        return 'spam', 'eggs'

>>> spam, eggs = spam_eggs()
>>> print('spam: {}, eggs: {}'.format((spam, eggs)))
spam: spam, eggs: eggs

