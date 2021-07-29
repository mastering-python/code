OrderedDicts
#############

Example 1
----------

**Basic Usage**

.. code-block:: python

    import collections

    spam = collections.OrderedDict()
    spam['b'] = 27
    spam['c'] = 32
    spam['a'] = 16

>>> spam
OrderedDict([('b', 2), ('c', 3), ('a', 1)])

>>> for key, value in spam.items():
...     key, value
('b', 2)
('c', 3)
('a', 1)

Example 2
----------

**Ordered by keys**

.. code-block:: python

    eggs = collections.OrderedDict(sorted(spam.items()))

>>> eggs
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
