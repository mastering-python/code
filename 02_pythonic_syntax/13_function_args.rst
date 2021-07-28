Function arguments
###################

Example 1
----------

**Incorrect function implementation**

.. code:: python 

    def spam(key, value, list_=[], dict_={}):
        list_.append(value)
        dict_[key] = value
        print('List: {}'.format(list_))
        print('Dict: {}'.format(dict_))

**Expected Result**

>>> spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> spam('key 2', 'value 2')
    List: ['value 2']
    Dict: {'key 2': 'value 2'}

**Real Result**

>>> spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> spam('key 2', 'value 2')
    List: ['value 1', 'value 2']
    Dict: {'key 1': 'value 1', 'key 2': 'value 2'}

Example 2
----------

**Correct function implementation**

.. code:: python 

    def spam(key, value, list_=None, dict_=None):
        if list_ is None: list_ = []
        if dict_ is None: dict_ = {}
        list_.append(value)
        dict_[key] = value

**Result**

>>> spam('key 1', 'value 1')
    List: ['value 1']
    Dict: {'key 1': 'value 1'}
>>> spam('key 2', 'value 2')
    List: ['value 2']
    Dict: {'key 2': 'value 2'}
