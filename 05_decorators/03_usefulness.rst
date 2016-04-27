>>> def spam(eggs):
...     return 'spam' * (eggs % 5)
...
>>> output = spam(3)

------------------------------------------------------------------------------

>>> def spam(eggs):
...     output = 'spam' * (eggs % 5)
...     print('spam(%r): %r' % (eggs, output))
...     return output
...
>>> output = spam(3)
spam(3): 'spamspamspam'

------------------------------------------------------------------------------

>>> import functools


>>> def debug(function):
...     @functools.wraps(function)
...     def _debug(*args, **kwargs):
...         output = function(*args, **kwargs)
...         print('%s(%r, %r): %r' % (function.__name__, args, kwargs, output))
...         return output
...     return _debug
...
>>>
>>> @debug
... def spam(eggs):
...     return 'spam' * (eggs % 5)
...
>>> output = spam(3)
spam((3,), {}): 'spamspamspam'
