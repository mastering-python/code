List Comprehensions
####################

Example 1
----------

**Basic usage**

.. code-block:: python

    squares = [
        x ** 2 
        for x in range(10)]

>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

Example 2
----------

**List comp with condition**

.. code-block:: python

    uneven_squares = [
        x ** 2 
        for x in range(10) 
        if x % 2]

>>> uneven_squares
[1, 9, 25, 49, 81]

**Equivalent for loop**

.. code-block:: python

    uneven_squares = []
    for x in range(10):
        if x % 2:
            uneven_squares.append(x ** 2)

>>> uneven_squares
[1, 9, 25, 49, 81]

Example 3
----------

**Flawed implementation (1)**

.. code-block:: python

    import random

    numbers = [
        random.random() 
        for _ in range(10) 
        if random.random() >= 0.5] # doctest: +SKIP
 
>>> numbers
[0.5211948104577864, 0.650010512129705, 0.021427316545174158]

*(1) The fist and last elements don't pass 
through the if condition*

**Correct implementation**

.. code-block:: python

    import random

    numbers = [
        random.random() 
        for _ in range(10)] # doctest: +SKIP

    numbers2 = [
        x 
        for x in numbers 
        if x >= 0.5] # doctest: +SKIP

>>> numbers2
[0.715510247827078, 0.8426277505519564, 0.5071133900377911]

Example 4
----------

**Nested list comp (harder to read)**

.. code-block:: python

    import random

    numbers = [
        x 
        for x in [
            random.random() 
            for _ in range(10)] 
        if x >= 0.5] # doctest: +SKIP

**Nested list comp (incomprehensible)**

.. code-block:: python

    import random

    numbers = [
        x for _ in range(10) 
        for x in [random.random()] 
        if x >= 0.5] # doctest: +SKIP
        
Example 5
----------
        
**A 2-variable list comp**

.. code-block:: python

    numbers = [
        (x, y) 
        for x in range(3) 
        for y in range(3, 5)]

>>> numbers
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]


**Equivalent for loop**

.. code-block:: python

    numbers = []
    for x in range(3):
        for y in range(3, 5):
            numbers.append((x, y))

>>> numbers
[(0, 3), (0, 4), (1, 3), (1, 4), (2, 3), (2, 4)]

Example 6
----------

**Avoid deeply nested list comps, 
since they're hard to read**

.. code-block:: python

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        ]

    temp = [
        item 
        for row in matrix 
        for item in row]

    reshaped_matrix = [
        [
            temp[i*len(matrix) + j]
            for j in range(len(matrix))
        ]
        for i in range(len(matrix[0]))
    ]

>>> import pprint
>>> pprint.pprint(reshaped_matrix, width=40)
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [10, 11, 12]]

