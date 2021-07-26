Explaining PEP8
################

Duck typing
------------

Example 1
..........

**Not recommended (explicit type checking)**

.. code:: python 

    import datetime


    if isinstance(timestamp, (datetime.date, datetime.datetime)):
        filename = '{}.csv'.format(timestamp)
    else:
        raise TypeError('Timestamp {} should be date(time) object, \
            got {}'.format(timestamp, type(timestamp)))

**Recommended (duck type checking)**

.. code:: python 

    import datetime


    timestamp = datetime.date(2000, 10, 5)
    filename = '{}.csv'.format(timestamp)
    print('Filename from date: {}'.format(filename))

    timestamp = '2000-10-05'
    filename = '{}.csv'.format(timestamp)
    print('Filename from str: {}'.format(filename))

Example 2
..........

**Not recommended (explicit type checking)**

.. code:: python 
    
    if isinstance(value, int):

**Recommended (Convert to desired type)**

.. code:: python 
    
    value = int(value)

Example 3
..........

**Not recommended  (check for types)**

.. code:: python 

    import io

    if isinstance(fh, io.IOBase):

**Recommended (check for attributes)**

.. code:: python 
    
    if hasattr(fh, 'read'):

    
Value and identity comparisons
-------------------------------
    
.. code:: python 

    a = 200 + 56
    b = 256
    c = 200 + 57
    d = 257

    print('{} == {}: {}'.format(a, b, a == b))
    print('{} is {}: {}'.format(a, b, a is b))
    print('{} == {}: {}'.format(c, d, c == d))
    print('{} is {}: {}'.format(c, d, c is d)) # Returns False (*)
    
    
**(*) Explanation:**

- Python keeps an internal array of integer objects for all integers 
    between -5 and 256

- That's why it works for 256 but not for 257
    
Loops
------

Example 1
..........

**Not Recommended**

.. code:: python 

    i = 0
    while i < len(my_list):
        item = my_list[i]
        i += 1
        do_something(i, item)

**Recommended**

.. code:: python 

    for i, item in enumerate(my_list):
        do_something(i, item)


Example 2
..........

**Not Recommended**

.. code:: python 

    eggs = [
        is_egg(item) or create_egg(item) 
        for item in list_of_items 
        if egg and hasattr(egg, 'egg_property') and isinstance(egg, Egg)] 

**Recommended**

.. code:: python 

    def to_egg(item):
        return is_egg(item) or create_egg(item)

    def can_be_egg(item):
        has_egg_property = hasattr(egg, 'egg_property')
        is_egg_instance = isinstance(egg, Egg)
        return egg and has_egg_property and is_egg_instance

    eggs = [
        to_egg(item) 
        for item in list_of_items 
        if can_be_egg(item)]

Maximum line length
--------------------

**Not Recommended**

.. code:: python 

    with open('/path/to/some/file/you/want/to/read') as file_1, \
        open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())

**Recommended**

.. code:: python 

    filename_1 = '/path/to/some/file/you/want/to/read'
    filename_2 = '/path/to/some/file/being/written'
    with open(filename_1) as file_1, open(filename_2, 'w') as file_2:
        file_2.write(file_1.read())

    filename_1 = '/path/to/some/file/you/want/to/read'
    filename_2 = '/path/to/some/file/being/written'
    with open(filename_1) as file_1:
        with open(filename_2, 'w') as file_2:
            file_2.write(file_1.read())    