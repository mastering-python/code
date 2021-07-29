Deques
#########

Example 1
----------

**Using a deque as a queue**

.. code-block:: python

    import collections

    queue = collections.deque()
    queue.append(1)
    queue.append(2)

>>> queue
deque([1, 2])
>>> queue.popleft()
1
>>> queue.popleft()
2
>>> queue.popleft()
Traceback (most recent call last):
    ...
IndexError: pop from an empty deque

Example 2
----------

**Using a deque as a stack**

.. code-block:: python

    import collections

    stack = collections.deque()
    stack.append(1)
    stack.append(2)

>>> stack
deque([1, 2])
>>> stack.pop()
2
>>> stack.pop()
1
>>> stack.pop()
Traceback (most recent call last):
    ...
IndexError: pop from an empty deque

Example 3
----------

**Using a deque as a circular queue**

.. code-block:: python

    import collections

    circular = collections.deque(maxlen=3)

>>> for i in range(5):
...     circular.append(i)
...     circular
deque([0], maxlen=3)
deque([0, 1], maxlen=3)
deque([0, 1, 2], maxlen=3)
deque([1, 2, 3], maxlen=3)
deque([2, 3, 4], maxlen=3)
