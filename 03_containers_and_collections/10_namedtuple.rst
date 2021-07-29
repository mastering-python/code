Namedtuples
############

Example 1
----------

**Basic usage**

.. code-block:: python

    import collections

    Point = collections.namedtuple('Point', ['x', 'y', 'z'])
    point_a = Point(1, 2, 3)
    point_b = Point(x=4, z=5, y=6)

>>> point_a
Point(x=1, y=2, z=3)
>>> point_b
Point(x=4, y=6, z=5)

Example 2
----------

>>> x, y, z = point_a

>>> print('X: {}, Y: {}, Z: {}'.format(x, y, z))
X: 1, Y: 2, Z: 3
>>> print('X: {}, Y: {}, Z: {}'.format(point_b.x, point_b.y, point_b.z))
X: 4, Y: 6, Z: 5
