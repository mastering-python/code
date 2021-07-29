Dict comprehensions
####################

Example 1
---------

**Basic usage**

.. code-block:: python

    mydict = {
        x: x ** 2 
        for x in range(10)}

>>> mydict
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

**Dict comprehensions with condition**

.. code-block:: python

    mydict = {
        x: x ** 2 
        for x in range(10) 
        if x % 2}

>>> mydict
{1: 1, 3: 9, 9: 81, 5: 25, 7: 49}

Example 2
---------

**Nested dict and list comprehensions**

.. code-block:: python

    mydict = {
        x ** 2: [
            y 
            for y in range(x)] 
        for x in range(5)}

>>> mydict
{0: [], 1: [0], 4: [0, 1], 16: [0, 1, 2, 3], 9: [0, 1, 2]}
