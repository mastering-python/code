Modifying while iterating
##########################

**Will not work (only lists can be modified during iteration)**

.. code:: python 

    dict_ = {'spam': 'eggs'}
    list_ = ['spam']
    set_ = {'spam', 'eggs'}

    for key in dict_:
        del dict_[key]

    for item in set_:
        set_.remove(item)

**Will work (converting to list during iteration)**

.. code:: python 

    dict_ = {'spam': 'eggs'}
    list_ = ['spam']
    set_ = {'spam', 'eggs'}

    for key in list(dict_):
        del dict_[key]

    for item in list_:
        list_.remove(item)

    for item in list(set_):
        set_.remove(item)
