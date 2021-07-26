Explicit is better than implicit
---------------------------------

**Not explicit**

.. code:: python 

    from spam import *
    from eggs import *


    some_function()


**More explicit**

.. code:: python 

    import spam
    import eggs


    spam.some_function()
    eggs.some_function()
