Practicality beats purity
--------------------------

**Not pythonic (Ignores PEP8)**

.. code:: python 

    from spam.eggs.foo.bar import spam, eggs, extra_spam, extra_eggs,
    extra_stuff from spam.eggs.foo.bar import spam, eggs, extra_spam,
    extra_eggs

**Pythonic (Adheres to PEP8)**

    from spam.eggs.foo.bar import spam 
    from spam.eggs.foo.bar import eggs
    from spam.eggs.foo.bar import extra_spam 
    from spam.eggs.foo.bar import extra_eggs 
    from spam.eggs.foo.bar import extra_stuff 
    from spam.eggs.foo.bar import spam
    from spam.eggs.foo.bar import eggs
    from spam.eggs.foo.bar import extra_spam
    from spam.eggs.foo.bar import extra_eggs

**Not Pythonic**

.. code:: python

    from spam_eggs_and_some_extra_spam_stuff import
    my_spam_and_eggs_stuff_which_is_too_long_for_a_line

**Still not pythonic but a better option**

.. code:: python
    
    from spam_eggs_and_some_extra_spam_stuff \
        import my_spam_and_eggs_stuff_which_is_too_long_for_a_line
