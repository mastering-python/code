>>> def filter_modulo(items, modulo):
...     output_items = []
...     for i in range(len(items)):
...         if items[i] % modulo:
...             output_items.append(items[i])
...     return output_items
...

>>> filter_modulo(range(10), 3)
[1, 2, 4, 5, 7, 8]


>>> filter_modulo = lambda i, m: [i[j] for j in range(len(i)) if i[j] % m]

>>> filter_modulo(range(10), 3)
[1, 2, 4, 5, 7, 8]


>>> filter_modulo = lambda items, modulo: [items[i] for i in range(len(items))
...                                        if items[i] % modulo]

>>> filter_modulo(range(10), 3)
[1, 2, 4, 5, 7, 8]


>>> def filter_modulo(items, modulo):
...     for item in items:
...         if item % modulo:
...             yield item
...

>>> list(filter_modulo(range(10), 3))
[1, 2, 4, 5, 7, 8]
