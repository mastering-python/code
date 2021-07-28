Exceptions
###########

**Canonical syntax**

.. code:: python 

    try:
        # do something here
    except (ValueError, TypeError) as e:
        print('Exception: %r' % e)


**Will not work ('e' not saved to a variable outside of 'except' scope)**

.. code:: python 

    def spam(value):
        try:
            value = int(value)
        except ValueError as e:
            print('We caught an exception: {} '.format(e))
        return e


>>> spam('a')
We caught an exception: ValueError("invalid literal for int() with base 10: 'a'",)
Traceback (most recent call last):
...
UnboundLocalError: local variable 'exception' referenced before assignment

**Will work ('e' saved to a variable outside of the 'except' scope)**

.. code:: python 

    def spam(value):
        exception = None
        try:
            value = int(value)
        except ValueError as e:
            exception = e
            print('We caught an exception: {} '.format(exception))
        return exception

>>> spam('a')
'We caught an exception: ValueError("invalid literal for int() with base 10: \'a\'")'
