Circular imports
#################

**Will throw circular import error**

*In eggs.py:*

.. code:: python 

    from spam import spam

    def eggs():
        print('This is eggs')
        spam()

*In spam.py:*

.. code:: python 

    from eggs import eggs

    def spam():
        print('This is spam')

    if __name__ == '__main__':
        eggs()

>>> spam()
Traceback (most recent call last):
File "spam.py", line 1, in <module>
...
ImportError: cannot import name 'eggs'

**Will work**

*In eggs.py:*

.. code:: python 

    import spam

    def eggs():
        print('This is eggs')
        spam.spam()

*In spam.py:*

.. code:: python 

    import eggs

    def spam():
        print('This is spam')

    if __name__ == '__main__':
        eggs.eggs()

>>> spam()
This is eggs
This is spam