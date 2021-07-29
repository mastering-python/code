Enums
######

Example 1
----------

**Basic usage**

.. code-block:: python

    import enum

    class Color(enum.Enum):
        red = 1
        green = 2
        blue = 3

>>> Color.red
<Color.red: 1>
>>> Color['red']
<Color.red: 1>
>>> Color(1)
<Color.red: 1>
>>> Color.red.name
'red'
>>> Color.red.value
1
>>> isinstance(Color.red, Color)
True
>>> Color.red is Color['red']
True
>>> Color.red is Color(1)
True

Example 2
----------

**Operations with enums**

.. code-block:: python

    colors = list()
    for item in Color:
        colors.append(item)

>>> colors
[<Color.red: 1>, <Color.green: 2>, <Color.blue: 3>]

.. code-block:: python

    colors = dict()
    colors[Color.green] = 0x00FF00

>>> colors
{<Color.green: 2>: 65280}

Example 3
----------

**Regular Enum**

.. code-block:: python

    import enum

    class Spam(enum.Enum):
        EGGS = 'eggs'

>>> Spam.EGGS == 'eggs'
False

**Enum with str inheritance**

.. code-block:: python

    import enum

    class Spam(str, enum.Enum):
        EGGS = 'eggs'

>>> Spam.EGGS == 'eggs'
True
