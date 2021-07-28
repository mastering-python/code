Errors should never pass silently
----------------------------------

**Non pythonic (Passing an exception silently)**

.. code:: python 

    try:
        value = int(user_input)
    except:
        pass

**Better than former example (Catching a generic exception)**

.. code:: python 

    try:
        value = int(user_input)
    except Exception as e:
        logging.warn('Uncaught exception: {}'.format(e))

**Pythonic (Catching a specific exception)**

.. code:: python 

    try:
        value = int(user_input)
    except ValueError:
        value = 0

**Non pythonic (Catching multiple statements)**

.. code:: python 

    try:
        value = int(user_input)
        value = do_some_processing(value)
        value = do_some_other_processing(value)
    except ValueError:
        value = 0

**Pythonic (Catching one statement)**

.. code:: python 

    try:
        value = int(user_input)
    except ValueError:
        value = 0
    else:
        value = do_some_processing(value)
        value = do_some_other_processing(value)
