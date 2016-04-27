>>> import functools


>>> def eggs(function):
...    @functools.wraps(function)
...    def _eggs(*args, **kwargs):
...        print('%r got args: %r and kwargs: %r' % (
...            function.__name__, args, kwargs))
...        return function(*args, **kwargs)
...
...    return _eggs

>>> @eggs
... def spam(a, b, c):
...     return a * b + c


>>> spam(1, 2, 3)
'spam' got args: (1, 2, 3) and kwargs: {}
5
