Lists
######

Example 1
-----------

**Inserting element to list - O(n)**

.. code-block:: python

    def remove(items, value):
        new_items = []
        found = False
        for item in items:
            # Skip the first item which is equal to value
            if not found and item == value:
                found = True
                continue
            new_items.append(item)
        if not found:
            raise ValueError('list.remove(x): x not in list')
        return new_items

**Deleting element from list - O(n)**

.. code-block:: python

    def insert(items, index, value):
        new_items = []
        for i, item in enumerate(items):
            if i == index:
                new_items.append(value)
            new_items.append(item)
        return new_items

     
>>> items = list(range(10))
>>> items
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> items = remove(items, 5)
>>> items
[0, 1, 2, 3, 4, 6, 7, 8, 9]

>>> items = insert(items, 2, 5)
>>> items
[0, 1, 5, 2, 3, 4, 6, 7, 8, 9]

Example 2
----------

**Removing a set of elements from a list**

.. code-block:: python

    primes = set((1, 2, 3, 5, 7))
    items = list(range(10))
    m = len(primes)
    n = len(items)

**Classic solution - O(m*n)**

.. code-block:: python

    for prime in primes:
        items.remove(prime)

>>> items
[0, 4, 6, 8, 9]

**Removing a set of elements - List comprehension - O(n*1)**

.. code-block:: python

    new_items = [
        item 
        for item in items 
        if item not in primes]

>>> new_items
[0, 4, 6, 8, 9]

**Removing a set of elements - Filter function - O(n*1)**

.. code-block:: python

    new_items = list(filter(
        lambda item: item not in primes, 
        items))

>>> new_items
[0, 4, 6, 8, 9]

Example 3
-----------

.. code-block:: python

    items = range(5)

**Find if the element is in list  - O(n)**

.. code-block:: python

    def in_(items, value):
        for item in items:
            if item == value:
                return True
        return False

>>> in_(items, 3)
True

**Find the minumum element - O(n)**

.. code-block:: python

    def min_(items):
        current_min = items[0]
        for item in items[1:]:
            if current_min > item:
                current_min = item
        return current_min

>>> min_(items)
0

**Find the maximum element - O(n)**

.. code-block:: python

    def max_(items):
        current_max = items[0]
        for item in items[1:]:
            if current_max < item:
                current_max = item
        return current_max

>>> max_(items)
4
