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