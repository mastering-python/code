>>> import functools


>>> class Value(object):
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return '<%s[%d]>' % (self.__class__, self.value)


>>> class Spam(Value):
...     def __gt__(self, other):
...         return self.value > other.value
...
...     def __ge__(self, other):
...         return self.value >= other.value
...
...     def __lt__(self, other):
...         return self.value < other.value
...
...     def __le__(self, other):
...         return self.value <= other.value
...
...     def __eq__(self, other):
...         return self.value == other.value


>>> @functools.total_ordering
... class Egg(Value):
...     def __lt__(self, other):
...         return self.value < other.value
...
...     def __eq__(self, other):
...         return self.value == other.value


>>> numbers = [4, 2, 3, 4]
>>> spams = [Spam(n) for n in numbers]
>>> eggs = [Egg(n) for n in numbers]

>>> spams
[<<class '...Spam'>[4]>, <<class '...Spam'>[2]>,
<<class '...Spam'>[3]>, <<class '...Spam'>[4]>]

>>> eggs
[<<class '...Egg'>[4]>, <<class '...Egg'>[2]>,
<<class '...Egg'>[3]>, <<class '...Egg'>[4]>]

>>> sorted(spams)
[<<class '...Spam'>[2]>, <<class '...Spam'>[3]>,
<<class '...Spam'>[4]>, <<class '...Spam'>[4]>]

>>> sorted(eggs)
[<<class '...Egg'>[2]>, <<class '...Egg'>[3]>,
<<class '...Egg'>[4]>, <<class '...Egg'>[4]>]

# Sorting using key is of course still possible and in this case
# perhaps just as easy:
>>> values = [Value(n) for n in numbers]
>>> values
[<<class '...Value'>[4]>, <<class '...Value'>[2]>,
<<class '...Value'>[3]>, <<class '...Value'>[4]>]

>>> sorted(values, key=lambda v: v.value)
[<<class '...Value'>[2]>, <<class '...Value'>[3]>,
<<class '...Value'>[4]>, <<class '...Value'>[4]>]

------------------------------------------------------------------------------

>>> def sort_by_attribute(attr, keyfunc=getattr):
...     def _sort_by_attribute(cls):
...         def __gt__(self, other):
...             return getattr(self, attr) > getattr(other, attr)
...
...         def __ge__(self, other):
...             return getattr(self, attr) >= getattr(other, attr)
...
...         def __lt__(self, other):
...             return getattr(self, attr) < getattr(other, attr)
...
...         def __le__(self, other):
...             return getattr(self, attr) <= getattr(other, attr)
...
...         def __eq__(self, other):
...             return getattr(self, attr) <= getattr(other, attr)
...
...         cls.__gt__ = __gt__
...         cls.__ge__ = __ge__
...         cls.__lt__ = __lt__
...         cls.__le__ = __le__
...         cls.__eq__ = __eq__
...
...         return cls
...     return _sort_by_attribute


>>> class Value(object):
...     def __init__(self, value):
...         self.value = value
...
...     def __repr__(self):
...         return '<%s[%d]>' % (self.__class__, self.value)


>>> @sort_by_attribute('value')
... class Spam(Value):
...     pass


>>> numbers = [4, 2, 3, 4]
>>> spams = [Spam(n) for n in numbers]
>>> sorted(spams)
[<<class '...Spam'>[2]>, <<class '...Spam'>[3]>,
 <<class '...Spam'>[4]>, <<class '...Spam'>[4]>]
