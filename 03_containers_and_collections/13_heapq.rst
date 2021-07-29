Heapqs
#########

**Basic Usage**

.. code-block:: python

    import heapq

    heap = [1, 3, 5, 7, 2, 4, 3]
    heapq.heapify(heap)

>>> heap
[1, 2, 3, 7, 3, 4, 5]

**Removing the top of the tree 
to get the sorted version of the list**

>>> while heap:
...     heapq.heappop(heap), heap
(1, [2, 3, 3, 7, 5, 4])
(2, [3, 3, 4, 7, 5])
(3, [3, 5, 4, 7])
(3, [4, 5, 7])
(4, [5, 7])
(5, [7])
(7, [])

