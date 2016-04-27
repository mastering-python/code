>>> import abc

>>> class CustomList(abc.ABC):
...     'This class implements a list-like interface'
...     pass

>>> CustomList.register(list)
<class 'list'>

>>> issubclass(list, CustomList)
True
>>> isinstance([], CustomList)
True
>>> issubclass(CustomList, list)
False
>>> isinstance(CustomList(), list)
False

------------------------------------------------------------------------------

>>> import abc

>>> class CustomList(abc.ABC, list):
...     'This class implements a list-like interface'
...     pass

>>> CustomList.register(list)
Traceback (most recent call last):
    ...
RuntimeError: Refusing to create an inheritance cycle

------------------------------------------------------------------------------

>>> import abc

>>> class UniversalClass(abc.ABC):
...    @classmethod
...    def __subclasshook__(cls, subclass):
...        return True


>>> issubclass(list, UniversalClass)
True
>>> issubclass(bool, UniversalClass)
True
>>> isinstance(True, UniversalClass)
True
>>> issubclass(UniversalClass, bool)
False
