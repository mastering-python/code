>>> import itertools
>>> list(itertools.islice(itertools.count(), 2, 7))
[2, 3, 4, 5, 6]

------------------------------------------------------------------------------

>>> itertools.count()[:10]
Traceback (most recent call last):
...
TypeError: 'itertools.count' object is not subscriptable

------------------------------------------------------------------------------

itertools.islice(itertools.count(), 10)
