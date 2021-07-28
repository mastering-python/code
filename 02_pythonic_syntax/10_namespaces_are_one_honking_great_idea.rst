Namespaces are one honking great idea
---------------------------------------

**Not clear**

.. code:: python 
    
    load(fh)

**Clearer than former example**

.. code:: python 
    
    pickle.load(fh)

**May cause confusion with a local class**

.. code:: python 
    
    # Use it as: User
    from django.contrib.auth.models import User 

**Avoids confusion, but can clash with other imports**

.. code:: python 
    
    # Use it as: models.User
    from django.contrib.auth import models

**Best options**

.. code:: python 
    
    # Use it as auth_models.User
    from django.contrib.auth import models as auth_models

    # Use it as auth_models.User
    import django.contrib.auth as auth_models
