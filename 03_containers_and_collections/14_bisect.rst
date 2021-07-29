Bisect
#########

Example 1
---------

**Inserting items using the regular sort**

.. code-block:: python

    sorted_list = []
    sorted_list.append(5)  # O(1)
    sorted_list.append(3)  # O(1)
    sorted_list.append(1)  # O(1)
    sorted_list.append(2)  # O(1)
    sorted_list.sort()  # O(n * log(n)) = O(4 * log(4)) = O(8)

>>> sorted_list
[1, 2, 3, 5]

**Inserting items using bisect**

.. code-block:: python

    import bisect

    sorted_list = []
    bisect.insort(sorted_list, 5)  # O(n) = O(1)
    bisect.insort(sorted_list, 3)  # O(n) = O(2)
    bisect.insort(sorted_list, 1)  # O(n) = O(3)
    bisect.insort(sorted_list, 2)  # O(n) = O(4)

>>> sorted_list
[1, 2, 3, 5]

Example 2
---------

**Searching items with bisect**

.. code-block:: python

    import bisect

    sorted_list = [1, 2, 3, 5]
    def contains(sorted_list, value):
        i = bisect.bisect_left(sorted_list, value) # O(log(n))
        return i < len(sorted_list) and sorted_list[i] == value
