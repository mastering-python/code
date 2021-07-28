Class Properties
###################

Example 1 
----------

**Incorrect class implementation**

.. code:: python 

    class Spam(object):
        list_ = []
        dict_ = {}
        def __init__(self, key, value):
            self.list_.append(value)
            self.dict_[key] = value
            
            print('List: {} '.format(self.list_))
            print('Dict: {} '.format(self.dict_))

**Expected Result**

>>> Spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> Spam('key 2', 'value 2')
    List: ['value 2']
    Dict: {'key 2': 'value 2'}

**Real Result**

>>> Spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> Spam('key 2', 'value 2')
    List: ['value 1', 'value 2']
    Dict: {'key 1': 'value 1', 'key 2': 'value 2'}

Example 2
----------

**Correct class implementation**

.. code:: python 

    class Spam(object):
        def __init__(self, key, value):
            self.list_ = [key]
            self.dict_ = {key: value}
            print('List: {} '.format(self.list_))
            print('Dict: {} '.format(self.dict_))

**Result**

>>> Spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> Spam('key 2', 'value 2')
    List: ['value 2']
    Dict: {'key 2': 'value 2'}


Example 3
----------

**Class properties are inherited**

.. code:: python 

    class A(object):
        spam = 1

    class B(A):
        pass

>>> A.spam
1
>>> B.spam
1

>>> A.spam = 2

>>> A.spam
2
>>> B.spam
2

