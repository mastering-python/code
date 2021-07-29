Set comprehensions
####################

Example 1
---------

**Basic usage**

.. code-block:: python

    myset = {
        x*y 
        for x in range(3) 
        for y in range(3)}

>>> myset
{0, 1, 2, 4}

**List comp as comparison**

.. code-block:: python

    mylist = [
        x*y 
        for x in range(3) 
        for y in range(3)]

>>> mylist
[0, 0, 0, 0, 1, 2, 0, 2, 4]
