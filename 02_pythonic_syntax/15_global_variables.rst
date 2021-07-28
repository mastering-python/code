Global variables
#################

Example 1 
----------

**Will work (doesn't modify global variable)**

.. code:: python 

    spam = 1
    def eggs():
        print('Spam: {} '.format(spam))

>>> eggs()
Spam: 1

**Will not work (modify the global variable, making it local)**

.. code:: python 

    spam = 1
    def eggs():
        spam += 1
        print('Spam: {} '.format(spam))

>>> eggs()
Traceback (most recent call last):
    ...
UnboundLocalError: local variable 'spam' referenced before assignment

