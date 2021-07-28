Readability counts
-------------------

**Not very readable**

.. code:: python 

    fib=lambda n:reduce(lambda x,y:(x[0]+x[1],x[0]),[(1,1)]*(n-2))[0]

**More readable**

.. code:: python 

    def fib(n):
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
