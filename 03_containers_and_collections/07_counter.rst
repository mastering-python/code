Counters
#########

Example 1
----------

**Basic usage**

.. code-block:: python

    import collections

    counter = collections.Counter('eggs')

>>> counter
Counter({'g': 2, 'e': 1, 's': 1})

Example 2
----------

**Get the 5 most common keys in the following list**

.. code-block:: python

    import math
    import collections

    counter = collections.Counter()
    for i in range(0, 100000):
        counter[math.sqrt(i) // 25] += 1

>>> for key, count in counter.most_common(5):
...     print('{}: {} '.format((key, count))
11.0: 14375
10.0: 13125
9.0: 11875
8.0: 10625
12.0: 10000

Example 3
----------

**Counter operations*

.. code-block:: python

    import collections

    eggs = collections.Counter('eggs')
    spam = collections.Counter('spam')

    def print_counter(expression, counter):
        sorted_characters = sorted(counter.elements())
        print(expression, ''.join(sorted_characters))

>>> print_counter('eggs:', eggs) 
eggs: eggs
>>> print_counter('spam:', spam)
spam: amps
>>> print_counter('eggs & spam:', eggs & spam) # Intersection
eggs & spam: s
>>> print_counter('spam & eggs:', spam & eggs) # Intersection
spam & eggs: s
>>> print_counter('eggs - spam:', eggs - spam) # Difference
eggs - spam: egg
>>> print_counter('spam - eggs:', spam - eggs) # Difference
spam - eggs: amp
>>> print_counter('eggs + spam:', eggs + spam) # Element-by-element sum
eggs + spam: aeggmpss
>>> print_counter('spam + eggs:', spam + eggs) # Element-by-element sum
spam + eggs: aeggmpss
>>> print_counter('eggs | spam:', eggs | spam) # Union
eggs | spam: aeggmps
>>> print_counter('spam | eggs:', spam | eggs) # Union
spam | eggs: aeggmps
