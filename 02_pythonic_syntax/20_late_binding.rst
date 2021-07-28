Late binding
#############

Example 1
----------

.. code:: python 

    eggs = [
        lambda a: \
        i * a \
        for i in range(3)]


**Expected result**

>>> for egg in eggs: print(egg(5))
0
5
10

**Real result**

>>> for egg in eggs: print(egg(5))
10
10
10

Example 2
----------

.. code:: python 
    
    import functools

    eggs = [
        functools.partial(lambda i, a: i * a, i) 
        for i in range(3)]

>>> for egg in eggs: print(egg(5))
0
5
10
